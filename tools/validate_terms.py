"""Detect superseded terms in current GEWINN material without scanning history."""

from __future__ import annotations

import argparse
import fnmatch
import re
import xml.etree.ElementTree as element_tree
import zipfile
from dataclasses import dataclass
from pathlib import Path

try:
    from .common import ROOT
except ImportError:  # Script execution
    from common import ROOT

OBSOLETE_TERMS = (
    "Arms Training",
    "Mastery:",
    "Weapon Scale",
    "Draw Scale",
    "Cut DR",
    "Point DR",
    "Crush DR",
    "Pistol-proof",
    "Musket-proof",
    "Growth-eligible Stress",
    "Source Strain",
    "Relic Strain",
    "Prepared Load",
    "Arcane Circle",
    "Holy Circle",
    "Transcendent Exertion",
)
REQUIRED_CURRENT_TERMS = (
    "Slashing",
    "Piercing",
    "Bludgeoning",
    "Shot",
    "Burning",
    "Shocking",
    "Toxic",
    "Freezing",
    "Proofed",
    "weight only",
    "Reload N",
    "recharge wound",
)
SCAN_ROOTS = ("manuscript/source", "data", "manuscript/generated", "manuscript/reference")
TEXT_EXTENSIONS = {".csv", ".md", ".txt", ".yaml", ".yml", ".json"}


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    term: str


def load_allowlist(path: Path) -> set[tuple[str, str]]:
    allowed: set[tuple[str, str]] = set()
    if not path.exists():
        return allowed
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            raise ValueError(f"{path}:{number}: allowlist requires path, term, and reason")
        allowed.add((parts[0], parts[1]))
    return allowed


def text_from_docx(path: Path) -> str:
    with zipfile.ZipFile(path) as document:
        xml = document.read("word/document.xml")
    root = element_tree.fromstring(xml)
    paragraphs: list[str] = []
    for paragraph in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
        paragraphs.append(
            "".join(
                node.text or ""
                for node in paragraph.iter(
                    "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"
                )
            )
        )
    return "\n".join(paragraphs)


def read_scan_text(path: Path) -> str | None:
    if path.suffix.casefold() in TEXT_EXTENSIONS:
        return path.read_text(encoding="utf-8-sig")
    if path.suffix.casefold() == ".docx":
        return text_from_docx(path)
    return None


def collect_findings(root: Path, allowlist: set[tuple[str, str]]) -> list[Finding]:
    findings: list[Finding] = []
    for relative_root in SCAN_ROOTS:
        directory = root / relative_root
        if not directory.is_dir():
            raise FileNotFoundError(f"required scan directory is missing: {relative_root}")
        for path in sorted(candidate for candidate in directory.rglob("*") if candidate.is_file()):
            text = read_scan_text(path)
            if text is None:
                continue
            relative = path.relative_to(root).as_posix()
            for term in OBSOLETE_TERMS:
                if any(
                    fnmatch.fnmatch(relative, pattern) and term == allowed_term
                    for pattern, allowed_term in allowlist
                ):
                    continue
                for match in re.finditer(re.escape(term), text, flags=re.IGNORECASE):
                    findings.append(Finding(relative, text.count("\n", 0, match.start()) + 1, term))
    return findings


def required_terms_missing(root: Path) -> list[str]:
    combined: list[str] = []
    for relative_root in SCAN_ROOTS:
        for path in (root / relative_root).rglob("*"):
            if path.is_file():
                text = read_scan_text(path)
                if text is not None:
                    combined.append(text)
    searchable = "\n".join(combined).casefold()
    return [term for term in REQUIRED_CURRENT_TERMS if term.casefold() not in searchable]


def validate_terms(
    root: Path = ROOT, *, strict: bool = False, allowlist_path: Path | None = None
) -> tuple[list[Finding], list[Finding], list[str]]:
    allowlist = load_allowlist(allowlist_path or root / "tools/term_allowlist.tsv")
    expected: list[Finding] = []
    current: list[Finding] = []
    for finding in collect_findings(root, allowlist):
        if finding.path.startswith("manuscript/source/"):
            expected.append(finding)
        else:
            current.append(finding)
    return expected, current, required_terms_missing(root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict", action="store_true", help="treat unmigrated manuscript debt as failure"
    )
    parser.add_argument("--allowlist", type=Path, default=ROOT / "tools/term_allowlist.tsv")
    arguments = parser.parse_args(argv)
    try:
        expected, current, missing = validate_terms(
            strict=arguments.strict, allowlist_path=arguments.allowlist
        )
    except (OSError, ValueError, zipfile.BadZipFile) as error:
        print(f"BOOTSTRAP INFRASTRUCTURE FAILURE: {error}")
        return 2

    if expected and not arguments.strict:
        print("EXPECTED MIGRATION DEBT (unmigrated manuscript source):")
        print("\n".join(f"- {item.path}:{item.line}: {item.term}" for item in expected))
    if missing and not arguments.strict:
        print("EXPECTED MIGRATION DEBT (current terms absent until migration):")
        print("- " + ", ".join(missing))
    if current:
        print("CURRENT-DATA FAILURE (obsolete term outside the unmigrated source):")
        print("\n".join(f"- {item.path}:{item.line}: {item.term}" for item in current))
    if arguments.strict and (expected or missing):
        print("STRICT FAILURE (migration debt remains):")
        print("\n".join(f"- {item.path}:{item.line}: {item.term}" for item in expected))
        if missing:
            print("- missing required current terms: " + ", ".join(missing))
    if current or (arguments.strict and (expected or missing)):
        return 1
    if not expected and not missing:
        print("Term validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Print the canonical manuscript and migration status without mutating files."""

def main() -> int:
    print("Canonical manuscript: manuscript/source/GEWINN_v2.5.docx")
    print("Migration status: not applied; read migration/v2.5-current/ before migration work")
    print("Numerical data: data/equipment/ and data/magic/")
    print("Manuscript status file: manuscript/source/MANUSCRIPT_STATUS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

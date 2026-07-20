"""A deterministic infrastructure smoke test, not a GEWINN balance model."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run(config_path: Path) -> dict[str, int | str]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    seed = int(config["seed"])
    trials = int(config["trials"])
    randomizer = random.Random(seed)
    samples = [randomizer.randint(1, 6) for _ in range(trials)]
    table_bytes = (ROOT / "data/equipment/melee_weapons.csv").read_bytes()
    return {
        "id": str(config["id"]),
        "seed": seed,
        "trials": trials,
        "sample_total": sum(samples),
        "data_hash_prefix": hashlib.sha256(table_bytes).hexdigest()[:12],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    arguments = parser.parse_args(argv)
    print(json.dumps(run(arguments.config), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

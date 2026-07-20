from pathlib import Path

from simulations.src.smoke import run


def test_smoke_simulation_is_reproducible() -> None:
    config = Path(__file__).resolve().parents[1] / "simulations/configs/smoke.json"
    assert run(config) == run(config)

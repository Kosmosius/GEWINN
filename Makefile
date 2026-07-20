PYTHON ?= python

.PHONY: bootstrap check lint test validate generate sim-smoke sim-full status

bootstrap:
	$(PYTHON) -m venv .venv
	./.venv/Scripts/python.exe -m pip install --upgrade pip
	./.venv/Scripts/python.exe -m pip install -e ".[dev]"

check: lint test generate validate sim-smoke

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

validate:
	$(PYTHON) tools/validate_manifest.py
	$(PYTHON) tools/validate_csv_schema.py
	$(PYTHON) tools/validate_slots.py
	$(PYTHON) tools/validate_kits.py
	$(PYTHON) tools/validate_terms.py

generate:
	$(PYTHON) tools/generate_tables.py

sim-smoke:
	$(PYTHON) simulations/src/smoke.py --config simulations/configs/smoke.yaml

sim-full:
	@echo "No maintained full rules simulation is registered yet. See simulations/README.md."

status:
	$(PYTHON) tools/status.py

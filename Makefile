MAIN=pac-man.py
VENV=.venv
PY=$(VENV)/bin/python3
PIP=$(VENV)/bin/pip
PDB=-m pdb
CONFIG=config.txt
DEPS=requirements.txt

.PHONY: install run debug clean lint lint-strict venv

run: install
	$(PY) $(MAIN) $(CONFIG)

install: venv
	$(PIP) install -r $(DEPS)

venv:
	python3 -m venv $(VENV)

debug:
	$(PY) $(PDB) $(MAIN)

clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf $(VENV)

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

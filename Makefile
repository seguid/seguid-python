SHELL=bash

all: test install

install:
	python -m pip install .

test:
	python -m pytest

check-cli:
	module load CBI bats-core bats-assert bats-file; \
	(cd tests/; bats *.bats)

coverage:
	python -m pytest --cov=src/

coverage-html:
	pytest --cov=src/ --cov-report=html; xdg-open htmlcov/index.html

cleanup:
	find . -type d -name "__pycache__" -exec rm -rf {} + || true
	[[ -d .pytest_cache ]] && rm -rf .pytest_cache || true
	[[ -f .coverage  ]] && rm .coverage || true
	[[ -d htmlcov ]] && rm -rf htmlcov || true

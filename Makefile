SHELL=bash

all: install check check-cli


#---------------------------------------------------------------
# Install package
#---------------------------------------------------------------
install-deps:
	python -m pip install pytest pydivsufsort

install:
	python -m pip install .


#---------------------------------------------------------------
# Build documentation (drop?!?)
#---------------------------------------------------------------
docs:
	cd docs; \
	make

#---------------------------------------------------------------
# Check package
#---------------------------------------------------------------
check:
	python -m pytest


#---------------------------------------------------------------
# Estimate test code coverage
#---------------------------------------------------------------
coverage:
	python -m pytest --cov=src/

coverage-html:
	pytest --cov=src/ --cov-report=html; xdg-open htmlcov/index.html


#---------------------------------------------------------------
# Check CLI using 'seguid-tests' test suite
#---------------------------------------------------------------
check-cli: Makefile.seguid-tests tests/cli.bats
	make MAKE="$(MAKE) -f Makefile.seguid-tests" -f Makefile.seguid-tests check-cli/seguid-python

Makefile.seguid-tests: 
	curl -H "Cache-Control: no-cache" -L -o "$@" https://raw.githubusercontent.com/seguid/seguid-tests/main/Makefile

tests/cli.bats:
	curl -H "Cache-Control: no-cache" -L -o "$@" https://raw.githubusercontent.com/seguid/seguid-tests/main/tests/cli.bats

update-seguid-tests:
	rm -f Makefile.seguid-tests
	$(MAKE) Makefile.seguid-tests
	rm -f tests/cli.bats
	$(MAKE) tests/cli.bats


#---------------------------------------------------------------
# Miscellaneous
#---------------------------------------------------------------
cleanup:
	find . -type d -name "__pycache__" -exec rm -rf {} + || true
	[[ -d .pytest_cache ]] && rm -rf .pytest_cache || true
	[[ -f .coverage  ]] && rm .coverage || true
	[[ -d htmlcov ]] && rm -rf htmlcov || true

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
# Miscellaneous
#---------------------------------------------------------------
cleanup:
	find . -type d -name "__pycache__" -exec rm -rf {} + || true
	[[ -d .pytest_cache ]] && rm -rf .pytest_cache || true
	[[ -f .coverage  ]] && rm .coverage || true
	[[ -d htmlcov ]] && rm -rf htmlcov || true

#---------------------------------------------------------------
# Check CLI using 'seguid-tests' test suite
#---------------------------------------------------------------
seguid-tests:
	git clone --branch=ldseguid-semicolon --depth=1 https://github.com/seguid/seguid-tests.git

check-cli: seguid-tests
	cd "$<" && git pull && make check-cli/seguid-python

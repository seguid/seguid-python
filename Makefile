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
add-submodules:
	git submodule add https://github.com/seguid/seguid-tests seguid-tests

seguid-tests:
	cd seguid-tests && git pull origin main
	git submodule init
	git submodule update

check-cli: seguid-tests
	$(MAKE) -C seguid-tests check-cli/seguid-python

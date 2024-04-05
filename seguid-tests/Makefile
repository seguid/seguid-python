SHELL=bash
BATS_SUPPORT_VERSION=0.3.0
BATS_ASSERT_VERSION=2.1.0
BATS = bats/bin/bats

all: check-cli/seguid-javascript check-cli/seguid-python check-cli/seguid-r

check-cli: assert-CLI_CALL assert-bats
	cd tests && $(BATS) *.bats

assert-CLI_CALL:
	[[ -n "${CLI_CALL}" ]] || { >&2 echo "ERROR: CLI_CALL is not specified"; exit 1; }

assert-bats:
	git submodule init
	git submodule update
	cd tests && command -v "${BATS}" || { >&2 echo "ERROR: bats is not installed"; exit 1; }


check-cli/seguid-javascript:
	$(MAKE) check-cli CLI_CALL="npx seguid" 

check-cli/seguid-python:
	$(MAKE) check-cli CLI_CALL="python -m seguid" 

check-cli/seguid-r:
	$(MAKE) check-cli CLI_CALL="Rscript --no-init-file -e seguid::seguid --args"

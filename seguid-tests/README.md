[![JavaScript CLI checks](https://github.com/seguid/seguid-tests/actions/workflows/check-cli-javascript.yml/badge.svg)](https://github.com/seguid/seguid-tests/actions/workflows/check-cli-javascript.yml)
[![Python CLI checks](https://github.com/seguid/seguid-tests/actions/workflows/check-cli-python.yml/badge.svg)](https://github.com/seguid/seguid-tests/actions/workflows/check-cli-python.yml)
[![R CLI checks](https://github.com/seguid/seguid-tests/actions/workflows/check-cli-r.yml/badge.svg)](https://github.com/seguid/seguid-tests/actions/workflows/check-cli-r.yml)


# seguid-tests: Test Suite for SEGUID Implementations

This repository provides as set of unit tests for validating current
and to-be-release SEGUID implementations. Currently, it provides tests
via the command-line interface (CLI). As long as the implementation
complies with the offical SEGUID v2 CLI, these tests should cover all
SEGUID v2 requirements.


## Testing a command-line interface

To test the command-line interface of a specific implementation, use
format:

```sh
$ make check-cli CLI_CALL="cmd <options>" 
```

where `"cmd <options>"` is the command with options use to call the
SEGUID CLI.  For example, the CLI of the Python **seguid** package is
called using the format:

```sh
$ python -m seguid ...
```

Thus, to test this interface, call:

```sh
$ make check-cli CLI_CALL="python -m seguid" 
```

A pre-defined short version of this is:

```sh
$ make check-cli/seguid-python
```

Similarly, for the CLI of the R **seguid** package, use:


```sh
$ make check-cli CLI_CALL="Rscript -e seguid::seguid --args" 
```

or short:

```sh
$ make check-cli/seguid-r
```


For the Javascript **seguid** package, use:


```sh
$ make check-cli CLI_CALL="npx seguid" 
```

or short:

```sh
$ make check-cli/seguid-javascript
```



## Requirements

The CLI checks are implemented in Bash and Bats (Bash Automated
Testing System):

* Bash
* [bats-core]

[bats-core]: https://bats-core.readthedocs.io/en/stable/


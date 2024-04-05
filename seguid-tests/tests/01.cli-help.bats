#!/usr/bin/env bats

setup() {
    load "test_helper/bats-support/load"
    load "test_helper/bats-assert/load"

    read -r -a cli_call <<< "${CLI_CALL:?}"
    echo "cli_call: [n=${#cli_call[@]}] ${cli_call[*]}"
}

## --------------------------------------------------------
## Help and version
## --------------------------------------------------------
@test "Session information" {
    version=$("${cli_call[@]}" --version)
    >&3 echo "Version: ${version}"
    >&3 echo "CLI call: [n=${#cli_call[@]}] ${cli_call[*]}"
    >&3 echo "LC_COLLATE: ${LC_COLLATE:-<not set>}"
}

@test "<CLI call> --version" {
    run "${cli_call[@]}" --version
    assert_success
    ## Assert numeric x.y.z format
    assert_output --regexp "[[:digit:]]+([.][[:digit:]]+)$"
}

@test "<CLI call> --help" {
    run "${cli_call[@]}" --help
    assert_success
    # assert_output --partial "seguid"
    assert_output --partial "--version"
    assert_output --partial "--help"
    assert_output --regexp "[Uu]sage:"
}

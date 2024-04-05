#!/usr/bin/env bats

setup() {
    load "test_helper/bats-support/load"
    load "test_helper/bats-assert/load"

    read -r -a cli_call <<< "${CLI_CALL:?}"
    echo "cli_call: [n=${#cli_call[@]}] ${cli_call[*]}"
}


## --------------------------------------------------------
## SEGUID v1
## --------------------------------------------------------
@test "<CLI call> <<< 'ACGT'" {
    run "${cli_call[@]}" <<< 'ACGT'
    assert_success
    assert_output "seguid=IQiZThf2zKn/I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=seguid <<< 'ACGT'" {
    run "${cli_call[@]}" --type=seguid <<< 'ACGT'
    assert_success
    assert_output "seguid=IQiZThf2zKn/I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=seguid <<< 'A' (single-symbol input)" {
    run "${cli_call[@]}" --type=seguid <<< 'A'
    assert_success
    assert_output "seguid=bc1M4j2I4u6VaLpUbAB8Y9kTHBs"
}

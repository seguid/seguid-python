#!/usr/bin/env bats

setup() {
    load "test_helper/bats-support/load"
    load "test_helper/bats-assert/load"

    read -r -a cli_call <<< "${CLI_CALL:?}"
    echo "cli_call: [n=${#cli_call[@]}] ${cli_call[*]}"
}


## --------------------------------------------------------
## Lexicographic ordering in current locale
## --------------------------------------------------------
@test "<CLI call> --type=csseguid --alphabet='0,A' <<< '0A' with current LC_COLLATE" {
    local alphabet seq truth
    seq="0A"
    alphabet="0,A"
    truth=$("${cli_call[@]}" --type=lsseguid --alphabet="${alphabet}" <<< "${seq}")
    truth=${truth/lsseguid=/csseguid=}
    echo "truth=${truth:?}"
    locale -a | grep "${LC_COLLATE}"
    cmd="echo 'LC_COLLATE=${LC_COLLATE:-<not set>}'; ${cli_call[*]} --type=csseguid --alphabet='${alphabet}' <<< '${seq}'"
    echo "cmd=${cmd}"
    run bash -c "${cmd}"
    assert_success
    assert_output --partial "LC_COLLATE=${LC_COLLATE}"
    assert_output --partial "${truth}"
}

@test "<CLI call> --type=csseguid --alphabet='0,a' <<< '0a' with current LC_COLLATE" {
    local alphabet seq truth
    seq="0a"
    alphabet="0,a"
    truth=$("${cli_call[@]}" --type=lsseguid --alphabet="${alphabet}" <<< "${seq}")
    truth=${truth/lsseguid=/csseguid=}
    echo "truth=${truth:?}"
    locale -a | grep "${LC_COLLATE}"
    cmd="echo 'LC_COLLATE=${LC_COLLATE:-<not set>}'; ${cli_call[*]} --type=csseguid --alphabet='${alphabet}' <<< '${seq}'"
    echo "cmd=${cmd}"
    run bash -c "${cmd}"
    assert_success
    assert_output --partial "LC_COLLATE=${LC_COLLATE}"
    assert_output --partial "${truth}"
}

@test "<CLI call> --type=csseguid --alphabet='A,a' <<< 'Aa' with current LC_COLLATE" {
    local alphabet seq truth
    seq="Aa"
    alphabet="A,a"
    truth=$("${cli_call[@]}" --type=lsseguid --alphabet="${alphabet}" <<< "${seq}")
    truth=${truth/lsseguid=/csseguid=}
    echo "truth=${truth:?}"
    locale -a | grep "${LC_COLLATE}"
    cmd="echo 'LC_COLLATE=${LC_COLLATE:-<not set>}'; ${cli_call[*]} --type=csseguid --alphabet='${alphabet}' <<< '${seq}'"
    echo "cmd=${cmd}"
    run bash -c "${cmd}"
    assert_success
    assert_output --partial "LC_COLLATE=${LC_COLLATE}"
    assert_output --partial "${truth}"
}

@test "<CLI call> --type=csseguid --alphabet='T,Z' <<< 'TZ' with current LC_COLLATE" {
    local alphabet seq truth
    seq="TZ"
    alphabet="T,Z"
    truth=$("${cli_call[@]}" --type=lsseguid --alphabet="${alphabet}" <<< "${seq}")
    truth=${truth/lsseguid=/csseguid=}
    echo "truth=${truth:?}"
    locale -a | grep "${LC_COLLATE}"
    cmd="echo 'LC_COLLATE=${LC_COLLATE:-<not set>}'; ${cli_call[*]} --type=csseguid --alphabet='${alphabet}' <<< '${seq}'"
    echo "cmd=${cmd}"
    run bash -c "${cmd}"
    assert_success
    assert_output --partial "LC_COLLATE=${LC_COLLATE}"
    assert_output --partial "${truth}"
}

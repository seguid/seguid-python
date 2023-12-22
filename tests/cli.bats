#!/usr/bin/env bats

setup() {
    load "${BATS_SUPPORT_HOME:?}/load.bash"
    load "${BATS_ASSERT_HOME:?}/load.bash"

    cli_call=(python -m seguid)

}


## --------------------------------------------------------
## Help and version
## --------------------------------------------------------
@test "<CLI call> --version" {
    run "${cli_call[@]}" --version
    assert_success
    ## Assert numeric x.y.z format
    assert_output --regexp "\b[[:digit:]]+([.][[:digit:]]+)$"
}

@test "<CLI call> --help" {
    run "${cli_call[@]}" --help
    assert_success
    assert_output --partial "seguid"
    assert_output --partial "--version"
    assert_output --partial "--help"
    assert_output --regexp "[Uu]sage:"
    assert_output --regexp "[Oo]ptions:"
}



## --------------------------------------------------------
## Succesfully cases
## --------------------------------------------------------
@test "<CLI call> <<< \"ACGT\"" {
    run "${cli_call[@]}" <<< "ACGT"
    assert_success
    assert_output "seguid:IQiZThf2zKn/I1KtqStlEdsHYDQ"
}


@test "<CLI call> --type=seguid <<< \"ACGT\"" {
    run "${cli_call[@]}" --type=seguid <<< "ACGT"
    assert_success
    assert_output "seguid:IQiZThf2zKn/I1KtqStlEdsHYDQ"
}


@test "<CLI call> --type=slseguid <<< \"ACGT\"" {
    run "${cli_call[@]}" --type=slseguid <<< "ACGT"
    assert_success
    assert_output "slseguid:IQiZThf2zKn_I1KtqStlEdsHYDQ"
}


@test "<CLI call> --type=scseguid <<< \"ACGT\"" {
    run "${cli_call[@]}" --type=scseguid <<< "ACGT"
    assert_success
    assert_output "scseguid:IQiZThf2zKn_I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=scseguid <<< \"CGTA\" (rotation invariant)" {
    run "${cli_call[@]}" --type=scseguid <<< "CGTA"
    assert_success
    assert_output "scseguid:IQiZThf2zKn_I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=scseguid <<< \"GTAC\" (rotation invariant)" {
    run "${cli_call[@]}" --type=scseguid <<< "GTAC"
    assert_success
    assert_output "scseguid:IQiZThf2zKn_I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=dlseguid <<< \$'AACGT\\nTTGCA'" {
    run "${cli_call[@]}" --type=dlseguid <<< $'AACGT\nTTGCA'
    assert_success
    assert_output "dlseguid:tYeHZYwxQGDHTqGDcrebERag0AU"
}

@test "<CLI call> --type=dcseguid <<< \$'AACGT\\nTTGCA'" {
    run "${cli_call[@]}" --type=dcseguid <<< $'AACGT\nTTGCA'
    assert_success
    assert_output "dcseguid:tYeHZYwxQGDHTqGDcrebERag0AU"
}

@test "<CLI call> --type=dcseguid <<< \$'CGTAA\\nGCATT' (rotation invariant)" {
    run "${cli_call[@]}" --type=dcseguid <<< $'CGTAA\nGCATT'
    assert_success
    assert_output "dcseguid:tYeHZYwxQGDHTqGDcrebERag0AU"
}

@test "<CLI call> --type=dcseguid <<< \$'GTAAC\\nCATTG' (rotation invariant)" {
    run "${cli_call[@]}" --type=dcseguid <<< $'GTAAC\nCATTG'
    assert_success
    assert_output "dcseguid:tYeHZYwxQGDHTqGDcrebERag0AU"
}

@test "<CLI call> --type=dcseguid <<< \$'GTTAC\\nCAATG' (strand symmetry)" {
    run "${cli_call[@]}" --type=dcseguid <<< $'GTTAC\nCAATG'
    assert_success
    assert_output "dcseguid:tYeHZYwxQGDHTqGDcrebERag0AU"
}

@test "<CLI call> --type=dlseguid <<< \$'-CGT\\nTGCA'" {
    run "${cli_call[@]}" --type=dlseguid <<< $'-CGT\nTGCA'
    assert_success
    assert_output "dlseguid:MpPe6pJoya3CoRh3BAw2qgEOcKI"
}

@test "<CLI call> --type=dlseguid <<< \$'-CGT\nTGC-'" {
    run "${cli_call[@]}" --type=dlseguid <<< $'-CGT\nTGC-'
    assert_success
    assert_output "dlseguid:a_o4Ga8vQrhlvI_zkjUg0uu6obA"
}


## --------------------------------------------------------
## Corner cases (single-symbol input)
## --------------------------------------------------------
@test "<CLI call> --type=seguid <<< \"\" (single-symbol input)" {
    run "${cli_call[@]}" --type=seguid <<< "A"
    assert_success
    assert_output "seguid:bc1M4j2I4u6VaLpUbAB8Y9kTHBs"
}

@test "<CLI call> --type=slseguid <<< \"\" (single-symbol input)" {
    run "${cli_call[@]}" --type=slseguid <<< "A"
    assert_success
    assert_output "slseguid:bc1M4j2I4u6VaLpUbAB8Y9kTHBs"
}

@test "<CLI call> --type=scseguid <<< \"\" (single-symbol input)" {
    run "${cli_call[@]}" --type=scseguid <<< "A"
    assert_success
    assert_output "scseguid:bc1M4j2I4u6VaLpUbAB8Y9kTHBs"
}

@test "<CLI call> --type=dlseguid <<< \$'A\nT' (single-symbol input)" {
    run "${cli_call[@]}" --type=dlseguid <<< $'A\nT'
    assert_success
    assert_output "dlseguid:S4AfmFCoHYVrWNQ_d7-lVVF2t20"
}

@test "<CLI call> --type=dcseguid <<< \$'A\nT' (single-symbol input)" {
    run "${cli_call[@]}" --type=dcseguid <<< $'A\nT'
    assert_success
    assert_output "dcseguid:S4AfmFCoHYVrWNQ_d7-lVVF2t20"
}


## --------------------------------------------------------
## Empty input is assume to be a user error
## --------------------------------------------------------
@test "<CLI call> --type=seguid <<< \"\" (empty input)" {
    run "${cli_call[@]}" --type=seguid <<< ""
    assert_failure
}

@test "<CLI call> --type=slseguid <<< \"\" (empty input)" {
    run "${cli_call[@]}" --type=slseguid <<< ""
    assert_failure
}

@test "<CLI call> --type=scseguid <<< \"\" (empty input)" {
    run "${cli_call[@]}" --type=scseguid <<< ""
    assert_failure
}

@test "<CLI call> --type=dlseguid <<< \"\" (empty input)" {
    run "${cli_call[@]}" --type=dlseguid <<< ""
    assert_failure
}

@test "<CLI call> --type=dcseguid <<< \"\" (empty input)" {
    run "${cli_call[@]}" --type=dcseguid <<< ""
    assert_failure
}


## --------------------------------------------------------
## Too many lines of input data
## --------------------------------------------------------
@test "<CLI call> --type=seguid <<< \$'ACTG\\nTGCA' (too many lines)" {
    run "${cli_call[@]}" --type=seguid <<< $'ACTG\nTGCA'
    assert_failure
}

@test "<CLI call> --type=slseguid <<< \$'ACTG\nTGCA' (too many lines)" {
    run "${cli_call[@]}" --type=slseguid <<< $'ACTG\nTGCA'
    assert_failure
}

@test "<CLI call> --type=dlseguid <<< \$'ACTG\\nTGCA\\nTGCA' (too many lines)" {
    run "${cli_call[@]}" --type=dlseguid <<< $'ACTG\nTGCA\nTGCA'
    assert_failure
}

@test "<CLI call> --type=dcseguid <<< \$'ACTG\\nTGCA\\nTGCA' (too many lines)" {
    run "${cli_call[@]}" --type=dcseguid <<< $'ACTG\nTGCA\nTGCA'
    assert_failure
}



## --------------------------------------------------------
## Failing cases
## --------------------------------------------------------
@test "<CLI call> <<< \"aCGT\" gives error (invalid character)" {
    run "${cli_call[@]}" <<< "aCGT"
    assert_failure
}

@test "<CLI call> <<< \" ACGT\" gives error (invalid character)" {
    run "${cli_call[@]}" <<< " ACGT"
    assert_failure
}

@test "<CLI call> --type=dlseguid <<< \$' ACGT\\nTGCA' gives error (invalid character)" {
    run "${cli_call[@]}" --type=dlseguid <<< $' ACGT\nTGCA '
    assert_failure
}

@test "<CLI call> --type=dlseguid <<< \$'ACGT\\nTGC' gives error (unbalanced lengths)" {
    run "${cli_call[@]}" --type=dlseguid <<< $'ACGT\nTGC'
    assert_failure
}

@test "<CLI call> --type=dlseguid <<< \$'ACGT\\nTGCC' gives error (incompatible sequences)" {
    run "${cli_call[@]}" --type=dlseguid <<< $'ACGT\nTGCC'
    assert_failure
}


## --------------------------------------------------------
## RNA
## --------------------------------------------------------
@test "<CLI call> --table=rna <<< \"ACGU\"" {
    skip "To be implemented"
    run "${cli_call[@]}" --table=rna <<< "ACGU"
    assert_success
    assert_output "seguid:LLaWk2Jb8NGt20QXhgm+cSVat34"
}


@test "<CLI call>--type=seguid --table=rna <<< \"ACGU\"" {
    skip "To be implemented"
    run "${cli_call[@]}" --type=seguid --table=rna <<< "ACGU"
    assert_success
    assert_output "seguid:LLaWk2Jb8NGt20QXhgm+cSVat34"
}


@test "<CLI call> --type=slseguid --table=rna <<< \"ACGU\"" {
    skip "To be implemented"
    run "${cli_call[@]}" --type=slseguid --table=rna <<< "ACGU"
    assert_success
    assert_output "slseguid:LLaWk2Jb8NGt20QXhgm-cSVat34"
}


@test "<CLI call> --type=scseguid --table=rna <<< \"ACGU\"" {
    skip "To be implemented"
    run "${cli_call[@]}" --type=scseguid --table=rna <<< "ACGU"
    assert_success
    assert_output "scseguid:LLaWk2Jb8NGt20QXhgm-cSVat34"
}

@test "<CLI call> --type=dlseguid --table=rna <<< \$'AACGU\\nUUdTGCA'" {
    skip "To be implemented"
    run "${cli_call[@]}" --type=dlseguid --table=rna <<< $'AACGU\nUUGCA'
    assert_success
    assert_output "dlseguid:r61AxqwrG01x8RpNluuRlfoL9VY"
}

@test "<CLI call> --type=dcseguid --table=rna <<< \$'AACGU\\nUUGCA'" {
    skip "To be implemented"
    run "${cli_call[@]}" --type=dcseguid --table=rna <<< $'AACGU\nUUGCA'
    assert_success
    assert_output "dcseguid:r61AxqwrG01x8RpNluuRlfoL9VY"
}

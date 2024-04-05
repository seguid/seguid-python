#!/usr/bin/env bats

setup() {
    load "test_helper/bats-support/load"
    load "test_helper/bats-assert/load"

    read -r -a cli_call <<< "${CLI_CALL:?}"
    echo "cli_call: [n=${#cli_call[@]}] ${cli_call[*]}"
}


## --------------------------------------------------------
## lsseguid()
## --------------------------------------------------------
@test "<CLI call> --type=lsseguid <<< 'ACGT'" {
    run "${cli_call[@]}" --type=lsseguid <<< 'ACGT'
    assert_success
    assert_output "lsseguid=IQiZThf2zKn_I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=lsseguid <<< 'A' (single-symbol input)" {
    run "${cli_call[@]}" --type=lsseguid <<< 'A'
    assert_success
    assert_output "lsseguid=bc1M4j2I4u6VaLpUbAB8Y9kTHBs"
}


## --------------------------------------------------------
## ldsseguid()
## --------------------------------------------------------
@test "<CLI call> --type=ldseguid <<< \$'AACGT\nTTGCA'" {
    run "${cli_call[@]}" --type=ldseguid <<< $'AACGT\nTTGCA'
    assert_success
    assert_output "ldseguid=5fHMG19IbYxn7Yr7_sOCkvaaw7U"
}

@test "<CLI call> --type=ldseguid <<< 'AACGT;ACGTT'" {
    run "${cli_call[@]}" --type=ldseguid <<< 'AACGT;ACGTT'
    assert_success
    assert_output "ldseguid=5fHMG19IbYxn7Yr7_sOCkvaaw7U"
}

@test "<CLI call> --type=ldseguid <<< \$'ACGTT\nTGCAA' (strand symmetry)" {
    truth=$("${cli_call[@]}" --type=ldseguid <<< $'AACGT\nTTGCA')
    run "${cli_call[@]}" --type=ldseguid <<< $'ACGTT\nTGCAA'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=ldseguid <<< 'ACGTT;AACGT' (strand symmetry)" {
    truth=$("${cli_call[@]}" --type=ldseguid <<< 'AACGT;ACGTT')
    run "${cli_call[@]}" --type=ldseguid <<< 'ACGTT;AACGT'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=ldseguid <<< \$'-CGT\nTGCA'" {
    run "${cli_call[@]}" --type=ldseguid <<< $'-CGT\nTGCA'
    assert_success
    assert_output "ldseguid=PVID4ZDkJEzFu2w2RLBCMQdZgvE"
}

@test "<CLI call> --type=ldseguid <<< '-CGT;ACGT'" {
    run "${cli_call[@]}" --type=ldseguid <<< '-CGT;ACGT'
    assert_success
    assert_output "ldseguid=PVID4ZDkJEzFu2w2RLBCMQdZgvE"
}

@test "<CLI call> --type=ldseguid <<< \$'-CGT\nTGC-'" {
    run "${cli_call[@]}" --type=ldseguid <<< $'-CGT\nTGC-'
    assert_success
    assert_output "ldseguid=s_nCUnQCNz7NjQQTOBmoqIvXexA"
}

@test "<CLI call> --type=ldseguid <<< '-CGT;-CGT'" {
    run "${cli_call[@]}" --type=ldseguid <<< '-CGT;-CGT'
    assert_success
    assert_output "ldseguid=s_nCUnQCNz7NjQQTOBmoqIvXexA"
}

@test "<CLI call> --type=ldseguid <<< \$'--TTACA\nCTAATG-'" {
    run "${cli_call[@]}" --type=ldseguid <<< $'--TTACA\nCTAATG-'
    assert_success
    assert_output "ldseguid=4RNiS6tZ_3dnHmqD_15_83vEqKQ"
}

@test "<CLI call> --type=ldseguid <<< '--TTACA;-GTAATC'" {
    run "${cli_call[@]}" --type=ldseguid <<< '--TTACA;-GTAATC'
    assert_success
    assert_output "ldseguid=4RNiS6tZ_3dnHmqD_15_83vEqKQ"
}

@test "<CLI call> --type=ldseguid <<< \$'A\nT' (single-symbol input)" {
    run "${cli_call[@]}" --type=ldseguid <<< $'A\nT'
    assert_success
    assert_output "ldseguid=ydezQsYTZgUCcb3-adxMaq_Xf8g"
}

@test "<CLI call> --type=ldseguid <<< 'A;T' (single-symbol input)" {
    run "${cli_call[@]}" --type=ldseguid <<< 'A;T'
    assert_success
    assert_output "ldseguid=ydezQsYTZgUCcb3-adxMaq_Xf8g"
}


## --------------------------------------------------------
## csseguid()
## --------------------------------------------------------
@test "<CLI call> --type=csseguid <<< 'ACGT'" {
    run "${cli_call[@]}" --type=csseguid <<< 'ACGT'
    assert_success
    assert_output "csseguid=IQiZThf2zKn_I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=csseguid <<< 'CGTA' (rotation invariant)" {
    truth=$("${cli_call[@]}" --type=csseguid <<< 'ACGT')
    run "${cli_call[@]}" --type=csseguid <<< 'CGTA'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=csseguid <<< 'GTAC' (rotation invariant)" {
    truth=$("${cli_call[@]}" --type=csseguid <<< 'ACGT')
    run "${cli_call[@]}" --type=csseguid <<< 'GTAC'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=csseguid <<< 'A' (single-symbol input)" {
    run "${cli_call[@]}" --type=csseguid <<< 'A'
    assert_success
    assert_output "csseguid=bc1M4j2I4u6VaLpUbAB8Y9kTHBs"
}


## --------------------------------------------------------
## cdseguid()
## --------------------------------------------------------
@test "<CLI call> --type=cdseguid <<< \$'AACGT\nTTGCA'" {
    run "${cli_call[@]}" --type=cdseguid <<< $'AACGT\nTTGCA'
    assert_success
    assert_output "cdseguid=5fHMG19IbYxn7Yr7_sOCkvaaw7U"
}

@test "<CLI call> --type=cdseguid <<< 'AACGT;ACGTT'" {
    run "${cli_call[@]}" --type=cdseguid <<< 'AACGT;ACGTT'
    assert_success
    assert_output "cdseguid=5fHMG19IbYxn7Yr7_sOCkvaaw7U"
}

@test "<CLI call> --type=cdseguid <<< \$'CGTAA\nGCATT' (rotation invariant)" {
    run "${cli_call[@]}" --type=cdseguid <<< $'CGTAA\nGCATT'
    assert_success
    assert_output "cdseguid=5fHMG19IbYxn7Yr7_sOCkvaaw7U"
}

@test "<CLI call> --type=cdseguid <<< 'CGTAA;TTACG' (rotation invariant)" {
    run "${cli_call[@]}" --type=cdseguid <<< 'CGTAA;TTACG'
    assert_success
    assert_output "cdseguid=5fHMG19IbYxn7Yr7_sOCkvaaw7U"
}

@test "<CLI call> --type=cdseguid <<< \$'GTAAC\nCATTG' (rotation invariant)" {
    truth=$("${cli_call[@]}" --type=cdseguid <<< $'CGTAA\nGCATT')
    run "${cli_call[@]}" --type=cdseguid <<< $'GTAAC\nCATTG'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=cdseguid <<< 'GTAAC;GTTAC' (rotation invariant)" {
    truth=$("${cli_call[@]}" --type=cdseguid <<< 'CGTAA;TTACG')
    run "${cli_call[@]}" --type=cdseguid <<< 'GTAAC;GTTAC'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=cdseguid <<< \$'GTTAC\nCAATG' (strand symmetry)" {
    truth=$("${cli_call[@]}" --type=cdseguid <<< $'CGTAA\nGCATT')
    run "${cli_call[@]}" --type=cdseguid <<< $'GTTAC\nCAATG'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=cdseguid <<< 'GTTAC;GTAAC' (strand symmetry)" {
    truth=$("${cli_call[@]}" --type=cdseguid <<< 'CGTAA;TTACG')
    run "${cli_call[@]}" --type=cdseguid <<< 'GTTAC;GTAAC'
    assert_success
    assert_output "${truth}"
}

@test "<CLI call> --type=cdseguid <<< \$'A\nT' (single-symbol input)" {
    run "${cli_call[@]}" --type=cdseguid <<< $'A\nT'
    assert_success
    assert_output "cdseguid=ydezQsYTZgUCcb3-adxMaq_Xf8g"
}

@test "<CLI call> --type=cdseguid <<< 'A;T' (single-symbol input)" {
    run "${cli_call[@]}" --type=cdseguid <<< 'A;T'
    assert_success
    assert_output "cdseguid=ydezQsYTZgUCcb3-adxMaq_Xf8g"
}


## --------------------------------------------------------
## Output forms
## --------------------------------------------------------
@test "<CLI call> --type=seguid --alphabet='{DNA}' --form='long' <<< 'ACGT'" {
    run "${cli_call[@]}" --type=seguid --alphabet='{DNA}' --form='long' <<< 'ACGT'
    assert_success
    assert_output "seguid=IQiZThf2zKn/I1KtqStlEdsHYDQ"
}

@test "<CLI call> --type=seguid --alphabet='{DNA}' --form='short' <<< 'ACGT'" {
    run "${cli_call[@]}" --type=seguid --alphabet='{DNA}' --form='short' <<< 'ACGT'
    assert_success
    assert_output "IQiZTh"
}

@test "<CLI call> --type=seguid --alphabet='{DNA}' --form='both' <<< 'ACGT'" {
    run "${cli_call[@]}" --type=seguid --alphabet='{DNA}' --form='both' <<< 'ACGT'
    assert_success
    assert_output "IQiZTh seguid=IQiZThf2zKn/I1KtqStlEdsHYDQ"
}



## --------------------------------------------------------
## Alphabet: DNA
## --------------------------------------------------------
@test "<CLI call> --type=seguid --alphabet='{DNA}' <<< 'ACGT'" {
    run "${cli_call[@]}" --type=seguid --alphabet='{DNA}' <<< 'ACGT'
    assert_success
    assert_output "seguid=IQiZThf2zKn/I1KtqStlEdsHYDQ"
}


## --------------------------------------------------------
## Alphabet: RNA
## --------------------------------------------------------
@test "<CLI call> --alphabet='{RNA}' <<< 'ACGU'" {
    run "${cli_call[@]}" --alphabet='{RNA}' <<< 'ACGU'
    assert_success
    assert_output "seguid=LLaWk2Jb8NGt20QXhgm+cSVat34"
}

@test "<CLI call> --type=seguid --alphabet='{RNA}' <<< 'ACGU'" {
    run "${cli_call[@]}" --type=seguid --alphabet='{RNA}' <<< 'ACGU'
    assert_success
    assert_output "seguid=LLaWk2Jb8NGt20QXhgm+cSVat34"
}

@test "<CLI call> --type=lsseguid --alphabet='{RNA}' <<< 'ACGU'" {
    run "${cli_call[@]}" --type=lsseguid --alphabet='{RNA}' <<< 'ACGU'
    assert_success
    assert_output "lsseguid=LLaWk2Jb8NGt20QXhgm-cSVat34"
}

@test "<CLI call> --type=csseguid --alphabet='{RNA}' <<< 'ACGU'" {
    run "${cli_call[@]}" --type=csseguid --alphabet='{RNA}' <<< 'ACGU'
    assert_success
    assert_output "csseguid=LLaWk2Jb8NGt20QXhgm-cSVat34"
}

@test "<CLI call> --type=ldseguid --alphabet='{RNA}' <<< \$'AACGU\nUUGCA'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet='{RNA}' <<< $'AACGU\nUUGCA'
    assert_success
    assert_output "ldseguid=x5iCPrq2tytNXOWgZroz1u6AN2Y"
}

@test "<CLI call> --type=ldseguid --alphabet='{RNA}' <<< 'AACGU;ACGUU'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet='{RNA}' <<< 'AACGU;ACGUU'
    assert_success
    assert_output "ldseguid=x5iCPrq2tytNXOWgZroz1u6AN2Y"
}

@test "<CLI call> --type=cdseguid --alphabet='{RNA}' <<< \$'AACGU\nUUGCA'" {
    run "${cli_call[@]}" --type=cdseguid --alphabet='{RNA}' <<< $'AACGU\nUUGCA'
    assert_success
    assert_output "cdseguid=x5iCPrq2tytNXOWgZroz1u6AN2Y"
}

@test "<CLI call> --type=cdseguid --alphabet='{RNA}' <<< 'AACGU;ACGUU'" {
    run "${cli_call[@]}" --type=cdseguid --alphabet='{RNA}' <<< 'AACGU;ACGUU'
    assert_success
    assert_output "cdseguid=x5iCPrq2tytNXOWgZroz1u6AN2Y"
}


## --------------------------------------------------------
## Alphabet: protein
## --------------------------------------------------------
## Source: http://bioinformatics.anl.gov/seguid/ftp.aspx
@test "<CLI call> --alphabet='{protein}' <<< 'PQITLWQRPIATIKVGGQLKEALLDTGADDTVLEEMNLPGRWKPKLIGGIGGFVKVRQYDQIPIEICGHQAIGTVLVGPTPANIIGRNLLTQIGCTLNF'" {
    run "${cli_call[@]}" --alphabet='{protein}' <<< 'PQITLWQRPIATIKVGGQLKEALLDTGADDTVLEEMNLPGRWKPKLIGGIGGFVKVRQYDQIPIEICGHQAIGTVLVGPTPANIIGRNLLTQIGCTLNF'
    assert_success
    assert_output "seguid=N4/z+gxAPfkFozbb3f3vStDB/5g"
}

@test "<CLI call> --alphabet='{protein}' <<< 'MTEYKLVVVGAGGVGKSALTIQLTQNHFVDEYDPTIE'" {
    run "${cli_call[@]}" --alphabet='{protein}' <<< 'MTEYKLVVVGAGGVGKSALTIQLTQNHFVDEYDPTIE'
    assert_success
    assert_output "seguid=PdwDBhhFjE6qlPmSWCJCOjKIDeA"
}

@test "<CLI call> --alphabet='{protein}' <<< 'ARDNAKNTLYLQMSRLRSEDTAMYYCAR'" {
    run "${cli_call[@]}" --alphabet='{protein}' <<< 'ARDNAKNTLYLQMSRLRSEDTAMYYCAR'
    assert_success
    assert_output "seguid=IdtGC8ZYgDbkA0i4u4n0tiAQwng"
}



## --------------------------------------------------------
## Use checksums as filenames
## --------------------------------------------------------
@test "<CLI call> --type='lsseguid' <<< 'GATTACA' checksum can be used as a filename" {
    seq="GATTACA"
    ## Comment:
    ## The   SEGUID check is seguid=tp2jzeCM2e3W4yxtrrx09CMKa/8
    ## The slSEGUID check is seguid=tp2jzeCM2e3W4yxtrrx09CMKa_8
    td=$(mktemp -d)
    filename=$("${cli_call[@]}" --type='lsseguid' <<< "${seq}")
    pathname="${td}/${filename}"
    echo "${seq}" > "${pathname}"
    [[ -f "${pathname}" ]]
    run cat "${pathname}"
    assert_success
    assert_output "${seq}"
    rm "${pathname}"
    rmdir "${td}"
}

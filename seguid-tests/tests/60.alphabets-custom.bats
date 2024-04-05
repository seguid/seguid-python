#!/usr/bin/env bats

setup() {
    load "test_helper/bats-support/load"
    load "test_helper/bats-assert/load"

    read -r -a cli_call <<< "${CLI_CALL:?}"
    echo "cli_call: [n=${#cli_call[@]}] ${cli_call[*]}"
}


## --------------------------------------------------------
## Alphabet: custom
## --------------------------------------------------------
@test "<CLI call> --alphabet='AU,CG' <<< 'ACGU'" {
    run "${cli_call[@]}" --alphabet='AU,CG' <<< 'ACGU'
    assert_success
    assert_output "seguid=LLaWk2Jb8NGt20QXhgm+cSVat34"
}

@test "<CLI call> --type=seguid --alphabet='AT,CG' <<< 'ACGT'" {
    run "${cli_call[@]}" --type=seguid --alphabet='AT,CG' <<< 'ACGT'
    assert_success
    assert_output "seguid=IQiZThf2zKn/I1KtqStlEdsHYDQ"
}

@test "<CLI call> --alphabet='A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y' <<< 'ARDNAKNTLYLQMSRLRSEDTAMYYCAR'" {
    run "${cli_call[@]}" --alphabet='A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y' <<< 'ARDNAKNTLYLQMSRLRSEDTAMYYCAR'
    assert_success
    assert_output "seguid=IdtGC8ZYgDbkA0i4u4n0tiAQwng"
}

# Expanded epigenetic alphabet per Viner et al. (2024)
@test "<CLI call> --type=lsseguid --alphabet='{DNA},m1,h2,f3,c4' <<< 'AmT2C'" {
    run "${cli_call[@]}" --type=lsseguid --alphabet="{DNA},m1,h2,f3,c4" <<< 'AmT2C'
    assert_success
    assert_output "lsseguid=MW4Rh3lGY2mhwteaSKh1-Kn2fGA"
}

# Expanded epigenetic alphabet per Viner et al. (2024)
@test "<CLI call> --type=ldseguid --alphabet='{DNA},m1,h2,f3,c4' <<< \$'AmT2C\nT1AhG'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet="{DNA},m1,h2,f3,c4" <<< $'AmT2C\nT1AhG'
    assert_success
    assert_output "ldseguid=bFZedILTms4ORUi3SSMfU0FUl7Q"
}

# Expanded epigenetic alphabet per Viner et al. (2024)
@test "<CLI call> --type=ldseguid --alphabet='{DNA},m1,h2,f3,c4' <<< 'AmT2C;GhA1T'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet="{DNA},m1,h2,f3,c4" <<< 'AmT2C;GhA1T'
    assert_success
    assert_output "ldseguid=bFZedILTms4ORUi3SSMfU0FUl7Q"
}

# Ambigous expanded epigenetic alphabet per Viner et al. (2024)
@test "<CLI call> --type=ldseguid --alphabet='{DNA},m1,h2,f3,c4,w6,x7,y8,z9' <<< \$'AmT2C\nT1AhG'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet="{DNA},m1,h2,f3,c4,w6,x7,y8,z9" <<< $'AAAhyAmA\nTTT28T1T'
    assert_success
    assert_output "ldseguid=7-4HH4Evl9RhN0OzTK18QPoqjWo"
}

# Ambigous expanded epigenetic alphabet per Viner et al. (2024)
@test "<CLI call> --type=ldseguid --alphabet='{DNA},m1,h2,f3,c4,w6,x7,y8,z9' <<< 'AAAhyAmA;T1T82TTT'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet="{DNA},m1,h2,f3,c4,w6,x7,y8,z9" <<< 'AAAhyAmA;T1T82TTT'
    assert_success
    assert_output "ldseguid=7-4HH4Evl9RhN0OzTK18QPoqjWo"
}

# Non-bijective complementary alphabets
@test "<CLI call> --alphabet='{DNA},AU' <<< 'ACGTU'" {
    run "${cli_call[@]}" --alphabet='{DNA},AU' <<< 'ACGTU'
    assert_success
    assert_output "seguid=w13LHbo0Y8FHo+vaowojJkwh9nY"
}

# Non-bijective complementary alphabets
@test "<CLI call> --type=ldseguid --alphabet='{DNA},AU' <<< \$'AAT\nTUA'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet='{DNA},AU' <<< $'AAT\nTUA'
    assert_success
    assert_output "ldseguid=fHXyliATc43ySIxHY2Zjlepnupo"
}

# Non-bijective complementary alphabets
@test "<CLI call> --type=ldseguid --alphabet='{DNA},AU' <<< 'AAT;AUT'" {
    run "${cli_call[@]}" --type=ldseguid --alphabet='{DNA},AU' <<< 'AAT;AUT'
    assert_success
    assert_output "ldseguid=fHXyliATc43ySIxHY2Zjlepnupo"
}

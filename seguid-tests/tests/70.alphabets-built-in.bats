#!/usr/bin/env bats

setup() {
    load "test_helper/bats-support/load"
    load "test_helper/bats-assert/load"

    read -r -a cli_call <<< "${CLI_CALL:?}"
    echo "cli_call: [n=${#cli_call[@]}] ${cli_call[*]}"
}

assert_symbols_in_alphabet() {
  local name set symbols
  name="${1:?}"
  set="${2:?}"
  symbols=${set//,/}
  "${cli_call[@]}" --alphabet="${name}" <<< "${symbols}"
}

letters=({a..z})
LETTERS=({A..Z})
digits=({0..9})
alpha=("${letters[@]}" "${LETTERS[@]}")
alnum=("${alpha[@]}" "${digits[@]}")

assert_symbols_not_in_alphabet() {
  local name set symbol
  name="${1:?}"
  set="${2:?}"
  set="$(sed 's/,//g' <<< "${set}")"
  echo "Set: ${set}"
  echo "Test symbols: [n=${#alnum[@]}] ${alnum[*]}"
  for symbol in "${alnum[@]}"; do
    if grep -q "${symbol}" <<< "${set}"; then
      continue
    fi
    echo "Symbol: '${symbol}'"
    if "${cli_call[@]}" --alphabet="${name}" <<< "${symbol}" 2> /dev/null; then
      fail "Alphabet '${name}' does not support symbol '${symbol}'"
    fi
  done
}



## --------------------------------------------------------
## Predefined alphabets
## --------------------------------------------------------
dna="CG,AT"
rna="CG,AU"
protein="A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,O,U"
dna_extended="CG,AT,WW,SS,MK,RY,BV,DH,VB,NN"
rna_extended="CG,AU,WW,SS,MK,RY,BV,DH,VB,NN"
protein_extended="A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,B,O,U,J,Z,X"

@test "<CLI call> --alphabet=\"{DNA}\" <<< '...'" {
  assert_symbols_in_alphabet "{DNA}" "${dna}"
  assert_symbols_not_in_alphabet "{DNA}" "${dna}"
}

@test "<CLI call> --alphabet=\"{RNA}\" <<< '...'" {
  assert_symbols_in_alphabet "{RNA}" "${rna}"
  assert_symbols_not_in_alphabet "{RNA}" "${rna}"
}

@test "<CLI call> --alphabet=\"{protein}\" <<< '...'" {
  assert_symbols_in_alphabet "{protein}" "${protein}"
  assert_symbols_not_in_alphabet "{protein}" "${protein}"
}

@test "<CLI call> --alphabet=\"{DNA-extended}\" <<< '...'" {
  assert_symbols_in_alphabet "{DNA-extended}" "${dna_extended}"
  assert_symbols_not_in_alphabet "{DNA-extended}" "${dna_extended}"
}

@test "<CLI call> --alphabet=\"{RNA-extended}\" <<< '...'" {
  assert_symbols_in_alphabet "{RNA-extended}" "${rna_extended}"
  assert_symbols_not_in_alphabet "{RNA-extended}" "${rna_extended}"
}

@test "<CLI call> --alphabet=\"{protein-extended}\" <<< '...'" {
  assert_symbols_in_alphabet "{protein-extended}" "${protein_extended}"
  assert_symbols_not_in_alphabet "{protein-extended}" "${protein_extended}"
}

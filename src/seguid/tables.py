#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition of Complementary DNA Symbols
COMPLEMENT_ALPHABET_DNA = {"G": "C", "A": "T", "C": "G", "T": "A"}


# Definition of Complementary RNA Symbols
COMPLEMENT_ALPHABET_RNA = {"G": "C", "A": "U", "C": "G", "U": "A"}


# Definition of Complementary IUPAC Ambigous DNA Symbols
"""
The alphabet below was adapted from Cornish-Bowden, 1985:

======== ================== ============ ======================================
Symbol   Meaning            Complement   Origin of designation
======== ================== ============ ======================================
 G        G                  C            Guanine
 A        A                  T            Adenine
 T        T                  A            Thymine
 C        C                  G            Cytosine
 R        A or G             Y            puRine
 Y        C or T             R            pYrimidine
 M        A or C             K            aMino
 K        G or T             M            Ketone
 S        C or G             S            Strong interaction (3 H bonds)
 W        A or T             W            Weak interaction (2 H bonds)
 H        A or C or T        D            not-G, H (follows G in the alphabet)
 B        C or G or T        V            not-A, B follows A
 V        A or C or G        B            not-T (not-U), V follows U
 D        A or G or T        H            not-C, D follows C
 N        G or A or T or C   N            aNy
======== ================== ============ ======================================


Cornish-Bowden, A. (1985). Nomenclature for incompletely specified
bases in nucleic acid sequences: recommendations 1984.
Nucleic Acids Research, 13(9), 3021–3030.
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC341218
"""

COMPLEMENT_ALPHABET_DNA_IUPAC = {
    **COMPLEMENT_ALPHABET_DNA,
    **{
        "B": "V",
        "D": "H",
        "H": "D",
        "K": "M",
        "M": "K",
        "S": "S",
        "R": "Y",
        "V": "B",
        "Y": "R",
        "W": "W",
        "N": "N",
    }
}

COMPLEMENT_ALPHABET_RNA_IUPAC = {
    **COMPLEMENT_ALPHABET_RNA,
    **{
        "B": "V",
        "D": "H",
        "H": "D",
        "K": "M",
        "M": "K",
        "S": "S",
        "R": "Y",
        "V": "B",
        "Y": "R",
        "W": "W",
        "N": "N",
    }
}

# Definition of a the IUPAC Protein Symbols
# values are empty strings since there is no concept of complementarity
# for proteins
ALPHABET_PROTEIN = {
    "A": "",
    "C": "",
    "D": "",
    "E": "",
    "F": "",
    "G": "",
    "H": "",
    "I": "",
    "K": "",
    "L": "",
    "M": "",
    "N": "",
    "P": "",
    "Q": "",
    "R": "",
    "S": "",
    "T": "",
    "V": "",
    "W": "",
    "Y": ""
}


ALPHABET_PROTEIN_IUPAC = {
    **ALPHABET_PROTEIN,
    **{
      "B": "",
      "J": "",
      "X": "",
      "Z": ""
    }
}
        

alphabet_categories = {
            "{DNA}": COMPLEMENT_ALPHABET_DNA,
      "{DNA-IUPAC}": COMPLEMENT_ALPHABET_DNA_IUPAC,
            "{RNA}": COMPLEMENT_ALPHABET_RNA,
      "{RNA-IUPAC}": COMPLEMENT_ALPHABET_RNA_IUPAC,
        "{protein}": ALPHABET_PROTEIN,
  "{protein-IUPAC}": ALPHABET_PROTEIN_IUPAC
}


def tablefactory(argument: str):
    # argument = "{protein},X,Z"
    # argument = "{DNA},BV,VB,DH,HD,KM,MK,NN,SS,WW"
    # argument = "AT,TA,CG,GC"
    # argument = 'A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y'
    tb, *ext = [e for e in argument.split(",")]
    try:
        alphabet = alphabet_categories[tb]
    except KeyError:
        if len(tb) == 1:
            alphabet = {tb[0]: ""}
        elif len(tb) == 2:
            alphabet = {tb[0]: tb[1]}
        else:
            raise ValueError(
                "First element not an alphabet category, symbol or basepair."
            )

    ## Here 'alphabet' is a dictionary
    if ext and all(len(e) == 1 for e in ext):
        assert set(alphabet.values()) == {""}  # extension is an alphabet
        for k in ext:
            if k in alphabet.values():
                raise ValueError("Detected duplicated symbol in alphabet: %s" % k)
            else:
                alphabet[k] = ""
    elif ext and all(len(e) == 2 for e in ext):
        # assert_alphabet                      # extension is a translation alphabet
        for k, v in ext:
            if k in alphabet.keys():
                ## Append symbol to already existing mapping, if not already done
                if not v in alphabet[k]:
                    alphabet[k] = str(alphabet[k]) + v
            else:
                alphabet[k] = v
    return alphabet

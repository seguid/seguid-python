#!/usr/bin/env python3
# -*- coding: utf-8 -*-

alphabets = {
               "{DNA}": "GC,AT",
               "{RNA}": "GC,AU",
      "{DNA-extended}": "GC,AT,BV,DH,KM,SS,RY,WW,NN",
      "{RNA-extended}": "GC,AU,BV,DH,KM,SS,RY,WW,NN",
           "{protein}": "A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,O,U",
  "{protein-extended}": "A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,O,U,B,J,X,Z"
}

def tablefactory(argument: str):
    # argument = "{protein},X,Z"
    # argument = "{DNA},BV,DH,KM,NN,SS,WW"
    # argument = "AT,CG"
    # argument = 'A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y'
    for name in alphabets.keys():
        argument = argument.replace(name, alphabets[name])

    n_expected=-1
    alphabet = {}
    for spec in argument.split(","):
        n=len(spec)
        if n_expected < 0:
            n_expected = n
        else:
            assert n == n_expected
        if n == 1:
            alphabet[spec] = ""
        elif n == 2:
            if spec[0] in alphabet.keys():
                alphabet[spec[0]] = alphabet[spec[0]] + spec[1]
            else:
                alphabet[spec[0]] = spec[1]
            if spec[1] in alphabet.keys():
                alphabet[spec[1]] = alphabet[spec[1]] + spec[0]
            else:
                alphabet[spec[1]] = spec[0]
        else:
            raise ValueError("Unknown alphabet specification: %s" % spec)
        
    return alphabet

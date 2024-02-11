#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid.asserts import assert_anneal
from seguid.asserts import assert_in_alphabet
from seguid.asserts import assert_alphabet

def test_assert_in_alphabet():
    """docstring."""
    seq = "ABCDEFGH"
    alphabet = {'A', 'C', 'G', 'T'}

    assert_in_alphabet("ACGT", alphabet = alphabet)
    assert_in_alphabet("AAAA", alphabet = alphabet)
    assert_in_alphabet("", alphabet = alphabet)

    try:
        assert_in_alphabet("x", alphabet = alphabet)
        print("Should not be reached")
    except ValueError:
        pass

    try:
        assert_in_alphabet("ACGTx", alphabet = alphabet)
        print("Should not be reached")
    except ValueError:
        pass


def test_assert_alphabet():
    """docstring."""
    assert_alphabet(str.maketrans("GATC", "CTAG"))

    try:
        assert_alphabet(str.maketrans("GATx", "CTAG"))
        print("Should not be reached")
    except ValueError:
        pass


def test_assert_anneal():

    tuples = (("AT", "TA", 1),
              ("CTATAG", "AT", -2),
              ("AT", "CTATAG", 2),
              ("AT", "AT", 0))

    for watson, crick, overhang in tuples:
        assert_anneal(watson, crick, overhang)

    tuples = (("AT", "CG", 1),
              ("CTATAG", "AT", -3),
              ("AT", "CTATAG", 1))

    for watson, crick, overhang in tuples:
        with pytest.raises(ValueError):
            assert_anneal(watson, crick, overhang)

    with pytest.raises(AssertionError):
        assert_anneal("AT", "AT", 4)

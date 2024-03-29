#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid._asserts import assert_in_alphabet
from seguid._asserts import assert_alphabet
from seguid._asserts import assert_complementary


def test_assert_in_alphabet():
    """docstring."""
    seq = "ABCDEFGH"
    alphabet = {"A", "C", "G", "T"}

    assert_in_alphabet("ACGT", alphabet=alphabet)
    assert_in_alphabet("AAAA", alphabet=alphabet)
    assert_in_alphabet("", alphabet=alphabet)

    try:
        assert_in_alphabet("x", alphabet=alphabet)
        print("Should not be reached")
    except ValueError:
        pass

    try:
        assert_in_alphabet("ACGTx", alphabet=alphabet)
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


def test_assert_complementary():
    """docstring."""

    watson = "ACGT"
    crick = "ACGT"
    alphabet = "{DNA}"
    assert_complementary(watson, crick, alphabet=alphabet)

    watson = "ACGU"
    crick = "ACGU"
    alphabet = "{RNA}"
    assert_complementary(watson, crick, alphabet=alphabet)

    watson = "-CGT"
    crick = "ACG-"
    alphabet = "{DNA}"
    assert_complementary(watson, crick, alphabet=alphabet)

    watson = "AT"
    crick = "AT"
    alphabet = "{DNA}"
    assert_complementary(watson, crick, alphabet=alphabet)

    watson = "AT"
    crick = "AT"
    alphabet = "{RNA}"
    try:
        assert_complementary(watson, crick, alphabet=alphabet)
        print("Should not be reached")
    except ValueError:
        pass

    watson = "AT"
    crick = "AT"
    alphabet = "{protein}"
    try:
        assert_complementary(watson, crick, alphabet=alphabet)
        print("Should not be reached")
    except AssertionError:
        pass

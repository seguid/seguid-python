#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid._manip import rotate
from seguid._manip import rotate_to_min
from seguid.config import set_min_rotation
from seguid.config import _min_rotation


def test_sort_order():

    from string import printable

    assert "".join(sorted(printable)) == (
        '\t\n\x0b\x0c\r !"'
        "#$%&'"
        "()*+,-./0123456789:;<=>?@"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "[\\]^_`"
        "abcdefghijklmnopqrstuvwxyz"
        "{|}~"
    )


def test_rotate():
    """docstring."""
    seq = "ACGTAACCGGTT"
    n = len(seq)
    assert rotate(seq, 0) == seq
    assert rotate(seq, n) == rotate(seq, 0)
    assert rotate(seq, 2 * n) == rotate(seq, 0)
    assert rotate(seq, n - 1) == rotate(seq, -1)

    assert rotate("", 0) == ""
    assert rotate("", 1) == ""


def test_min_rotation_pydivsufsort():
    """Tests for the pydivsufsort min_rotation"""
    set_min_rotation("pydivsufsort")
    assert _min_rotation("") == 0
    assert _min_rotation("Aa") == 0
    assert rotate_to_min("taaa") == "aaat"
    assert rotate_to_min("abaabaaabaababaaabaaababaab") == "aaabaaababaababaabaaabaabab"
    assert rotate_to_min("abaabaaabaababaaabaaaBabaab") == "Babaababaabaaabaababaaabaaa"
    set_min_rotation("built-in")


def test_min_rotation_built_in():
    set_min_rotation("built-in")
    assert _min_rotation("Aa") == 0
    assert rotate_to_min("TAAA") == "AAAT"
    assert rotate_to_min("ACAACAAACAACACAAACAAACACAAC") == "AAACAAACACAACACAACAAACAACAC"
    assert _min_rotation("") == 0

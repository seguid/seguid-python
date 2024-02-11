#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid.asserts import assert_alphabet

from seguid.tables import COMPLEMENT_ALPHABET_DNA
from seguid.tables import COMPLEMENT_ALPHABET_RNA
from seguid.tables import COMPLEMENT_ALPHABET_IUPAC
from seguid.tables import ALPHABET_IUPAC_PROTEIN


def test_complementary_alphabets():
    """docstring."""
    assert_alphabet(COMPLEMENT_ALPHABET_DNA)
    assert_alphabet(COMPLEMENT_ALPHABET_RNA)
    assert_alphabet(COMPLEMENT_ALPHABET_IUPAC)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid.asserts import assert_alphabet
from seguid.tables import tablefactory

def test_tablefactory():
    """docstring."""
    assert_alphabet(tablefactory("{DNA}"))
    assert_alphabet(tablefactory("{RNA}"))
    assert_alphabet(tablefactory("{DNA-IUPAC}"))
    assert_alphabet(tablefactory("{RNA-IUPAC}"))
    tablefactory("{protein}")
    tablefactory("{protein-IUPAC}")

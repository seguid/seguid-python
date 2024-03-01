#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid._asserts import assert_alphabet
from seguid._tables import tablefactory

def test_tablefactory():
    """docstring."""
    assert_alphabet(tablefactory("{DNA}"))
    assert_alphabet(tablefactory("{RNA}"))
    assert_alphabet(tablefactory("{DNA-extended}"))
    assert_alphabet(tablefactory("{RNA-extended}"))
    tablefactory("{protein}")
    tablefactory("{protein-extended}")

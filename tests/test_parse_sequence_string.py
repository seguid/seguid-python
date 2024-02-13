#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid.reprutils import parse_sequence_string


def test_parse_sequence_string():
    """docstring."""
    
    spec = "TATGCC\nATACGG"
    type2, specification, watson, crick = parse_sequence_string(spec)
    assert type2 == "ds"
    assert specification == spec
    assert watson == "TATGCC"
    assert crick == "GGCATA"
    
    spec = "-TATGCC\nCATACG-"
    type2, specification, watson, crick = parse_sequence_string(spec)
    assert type2 == "ds"
    assert specification == spec
    assert watson == "-TATGCC"
    assert crick == "-GCATAC"
    
    spec = "TATGCC--\n-TACGGGG"
    type2, specification, watson, crick = parse_sequence_string(spec)
    assert type2 == "ds"
    assert specification == spec
    assert watson == "TATGCC--"
    assert crick == "GGGGCAT-"
    
    spec = "TATGCC--\n--ACGGGG"
    type2, specification, watson, crick = parse_sequence_string(spec)
    assert type2 == "ds"
    assert specification == spec
    assert watson == "TATGCC--"
    assert crick == "GGGGCA--"

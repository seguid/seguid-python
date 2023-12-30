#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid.asserts import assert_table

from seguid.tables import COMPLEMENT_TABLE_DNA
from seguid.tables import COMPLEMENT_TABLE_RNA
from seguid.tables import COMPLEMENT_TABLE_IUPAC
from seguid.tables import TABLE_IUPAC_PROTEIN


def test_complementary_tables():
    """docstring."""
    assert_table(COMPLEMENT_TABLE_DNA)
    assert_table(COMPLEMENT_TABLE_RNA)
    assert_table(COMPLEMENT_TABLE_IUPAC)

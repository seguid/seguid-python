#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid.reprutils import tuple_from_repr
from seguid.reprutils import repr_from_tuple


def test_tuple_from_repr():
    """docstring."""

    rpr = """
      -TATGCC
      CATACG-
    """

    assert tuple_from_repr(rpr) == ("TATGCC", "GCATAC", 1)

    rpr = """
       TATGCC--
       -TACGGGG
    """

    assert tuple_from_repr(rpr) == ("TATGCC", "GGGGCAT", -1)

    rpr = """   # Source code comments like this one are not allowed
        TATGCC
        ATACGG
    """

    with pytest.raises(ValueError):
        tuple_from_repr(rpr)

    rpr = """
       TATGCC--
       --ACGGGG
    """

    assert tuple_from_repr(rpr) == ("TATGCC", "GGGGCA", -2)

    rpr = """
       TATGCC
       ATACGG
    """

    assert tuple_from_repr(rpr) == ('TATGCC', 'GGCATA', 0)

    rpr_should_err = """
       - TGCC
       ATACGG
    """

    with pytest.raises(ValueError):
        tuple_from_repr(rpr_should_err)

    rpr_should_err = """
        -TGCC
       ATACGG
    """

    with pytest.raises(ValueError):
        tuple_from_repr(rpr_should_err)

    rpr_should_err = """
      ---TGCC
       ATACGG
    """

    with pytest.raises(ValueError):
        tuple_from_repr(rpr_should_err)

    rpr_should_err = """
      ---TGCC
      -ATACGG
    """
    with pytest.raises(AssertionError):
        tuple_from_repr(rpr_should_err)

    rpr_should_err = """
       TATGCC-
       ATACGG-
    """
    with pytest.raises(AssertionError):
        tuple_from_repr(rpr_should_err)


def test_repr_from_tuple():
    assert repr_from_tuple(*("TATGCC", "GGGGCA", -2)) == "TATGCC--\n--ACGGGG"

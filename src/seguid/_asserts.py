#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from seguid._tables import tablefactory
import seguid._manip
from string import ascii_letters
from string import digits
import re


def assert_in_alphabet(seq: str, alphabet: set):

    assert isinstance(seq, str), "Argument 'seq' must be an string"
    assert isinstance(alphabet, set), "Argument 'alphabet' must be a set"
    assert len(alphabet) > 0, "Argument 'alphabet' must not be empty"
    assert not alphabet - (
        set(ascii_letters) | set(digits) | set("-\n;")
    ), "Only A-Z a-z allowed"
    first = list(alphabet)[0]
    assert isinstance(first, str), "Argument 'alphabet' should contain 'str' elements"

    # Nothing to do?
    if len(seq) == 0:
        return

    unknown = set(c for c in seq if c not in (k for k in alphabet))

    if unknown:
        missing = " ".join(unknown)
        missing = repr(missing)  ## escape '\n', '\t', ...
        raise ValueError("Detected symbols " f"{missing} in not in the 'alphabet'")


def assert_alphabet(alphabet: dict):
    assert isinstance(alphabet, dict), "Argument 'alphabet' must be a dict"
    keys = alphabet.keys()
    values = alphabet.values()
    if isinstance(next(iter(values)), str):
        values2 = set()
        for value in values:
            for ch in value:
                values2.add(ch)
        values = values2

    # Assert that the set of values are also in the set of keys
    unknown = set(str(k) for k in keys if str(k) not in (str(v) for v in values))

    if unknown:
        missing = " ".join(unknown)
        missing = repr(missing)  ## escape '\n', '\t', ...
        raise ValueError(
            f"Detected keys ({missing}) in 'alphabet' that are not in the values"
        )


# def assert_checksum(checksum):
#     checksum = "cdseguid:AWD-dt5-TEua8RbOWfnctJIu9nA"
#     mobj = re.match("(?:|sl|sc|ds|dc)seguid:(.+)", checksum)
#     assert len(mobj.group(1)) == 27
#     b64 = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_-')
#     assert set(mobj.group(1)).issubset(b64)


def reverse(seq) -> str:
    """Reverses a DNA sequence"""
    assert isinstance(seq, str), "Argument 'seq' must be an string"
    return seq[::-1]


def assert_complementary(
    watson: str, crick: str, alphabet: dict
):
    ## Validate 'alphabet':
    tb = tablefactory(alphabet)
    keys = tb.keys()
    values = tb.values()

    ## FIXME: Does this really work? See next line.
    assert len(tb.values()) > 1, "Was a single-stranded alphabet used by mistake?"
    assert (
        len(next(iter(values))) == 1
    ), "Was a single-stranded alphabet used by mistake?"
    assert_alphabet(tb)

    if not "-" in keys:
        tb["-"] = "-"
        keys = tb.keys()
        values = tb.values()

    ## Validate 'watson' and 'crick':
    assert len(watson) == len(crick)
    assert_in_alphabet(watson, alphabet=set(keys))
    assert_in_alphabet(crick, alphabet=set(keys))
    crick = reverse(crick)

    for kk in range(0, len(watson)):
        #        print(str(kk) + ": " + watson[kk] + "-" + crick[kk])
        if watson[kk] == "-" or crick[kk] == "-":
            continue
        set_kk = tb[watson[kk]]
        if not crick[kk] in set_kk:
            raise ValueError(
                "Non-complementary basepair (%s,%s) detected at position %d"
                % (watson[kk], crick[kk], kk + 1)
            )

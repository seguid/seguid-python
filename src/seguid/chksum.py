#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
seguid.

The seguid module provides four functions for calculations of SEGUID checksums
for biological sequences with varying topologies

lsseguid (s)ingle-stranded (l)inear SEGUID
csseguid (s)ingle-stranded (c)ircular SEGUID
ldseguid (d)ouble-stranded (l)inear SEGUID
cdseguid (d)ouble-stranded (c)ircular SEGUID

Some auxillary functions are also provided.

The functions can be made to work without external dependencies, but
csseguid and cdseguid are considerably faster with pydivsufsort installed.

"""

import hashlib
import base64

from seguid.manip import rc
from seguid.manip import rotate_to_min

# from seguid.manip import linearize_circular_dsDNA
# from seguid.tables import COMPLEMENT_TABLE_DNA
from seguid.tables import tablefactory
from seguid.asserts import assert_in_alphabet
from seguid.asserts import assert_anneal
from seguid.reprutils import repr_from_tuple

seguid_prefix: str = "seguid-"
lsseguid_prefix: str = "lsseguid-"
csseguid_prefix: str = "csseguid-"
ldseguid_prefix: str = "ldseguid-"
cdseguid_prefix: str = "cdseguid-"
b64alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_-")


def _seguid(seq: str, table: str = "{DNA}", encoding: callable = base64.standard_b64encode) -> str:
    assert callable(encoding)
    assert seq, "A sequence must not be empty"
    assert_in_alphabet(seq, alphabet=set(tablefactory(table).keys()))
    m = hashlib.sha1()
    m.update(seq.encode("ASCII").upper())
    hs = encoding(m.digest())
    csum = f"{hs.decode('ASCII').rstrip('=')}"
    assert len(csum) == 27
    assert set(csum).issubset(b64alphabet)
    return csum


def seguid(seq: str, table: str = "{DNA}") -> str:
    """SEGUID checksum for protein or single stranded linear DNA.

    OBSOLETE, use lsseguid instead.

    Given a nucleotide or amino-acid sequence `seq`, the function returns
    a string containing the SEquence Globally Unique IDentifier (SEGUID).

    The optional ´encoding` argument expects a function accepting a
    byte string an returning another byte string. Several such functions are
    available from the standard library:

    https://docs.python.org/3/library/base64.html

    The SEGUID is defined as the Base64 encoded sha1 checksum calculated for
    the sequence in upercase with the trailing "=" character removed. This
    means that upper or lower case symbols in `seq` do not affect the result.

    The resulting string is not url-safe as the Base64 encoding it potentially
    produces / and + characters, carrying special meaning in a Uniform Resource
    Locator (URL). It can also not be used as an identifier or variable name in
    programming languanges such as Python.

    This implementation follows the original SEGUID definition by
    Babnigg et al. 2006. For more information:

    Babnigg, G., & Giometti, C. S. (2006). A database of unique protein
    sequence identifiers for proteome studies. Proteomics, 6(16), 4514–4522.
    https://doi.org/10.1002/pmic.200600032

    The checksum is prefixed with "seguid-"

    Examples
    --------
    >>> seguid("AT")
    'seguid-Ax/RG6hzSrMEEWoCO1IWMGska+4'
    """
    return seguid_prefix + _seguid(seq, table=table, encoding=base64.standard_b64encode)


def lsseguid(seq: str, table: str = "{DNA}") -> str:
    """SEGUID checksum for single stranded linear DNA (slSEGUID).

    Identical to the seguid function except for that the '+' and '/' characters
    of standard Base64 encoding are replaced by '-' and '_', respectively
    following the standard in RFC 4648 section 5.

    The base64.urlsafe_b64encode from the Python standard libary is used.

    This checksum is applicable to single stranded linear DNA sequences.
    Can also be used for protein sequences.

    The checksum is prefixed with "lsseguid-"

    Examples
    --------
    >>> lsseguid("AT")
    'lsseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
    """
    return lsseguid_prefix + _seguid(seq, table=table, encoding=base64.urlsafe_b64encode)


def csseguid(seq: str, table: str = "{DNA}") -> str:
    r"""SEGUID checksum for single stranded circular DNA (csSEGUID).

    The csSEGUID is the lsSEGUID checksum calculated for the lexicographically
    smallest string rotation of a ssDNA sequence.

    Only defined for circular sequences.

    The srfun argument has to take a string as an argument and
    return another string.

    The checksum is prefixed with "csseguid-"

    Examples
    --------
    >>> csseguid("ATTT")
    'csseguid-ot6JPLeAeMmfztW1736Kc6DAqlo'
    >>> lsseguid("ATTT")
    'lsseguid-ot6JPLeAeMmfztW1736Kc6DAqlo'
    >>> csseguid("TTTA")
    'csseguid-ot6JPLeAeMmfztW1736Kc6DAqlo'
    >>> lsseguid("TTTA")
    'lsseguid-8zCvKwyQAEsbPtC4yTV-pY0H93Q'
    """
    return csseguid_prefix + _seguid(rotate_to_min(seq), table=table, encoding=base64.urlsafe_b64encode)


def ldseguid(watson: str, crick: str, overhang: int, table: str = "{DNA}") -> str:
    r"""SEGUID checksum for double stranded linear DNA (ldSEGUID).

    Calculates the ldSEGUID checksum for a dsDNA sequence defined by two
    strings representing the upper (Watson) and lower (Crick) strand
    complementary DNA strands and an integer value describing the stagger
    between the two strands in the 5' (left) end of the molecule.

    The overhang is defined as the amount of 3' overhang at the start side
    of the molecule. A molecule with 5' overhang has a negative
    overhang value.

    See examples below:

    ::


        dsDNA       overhang

        --nnn...    2
        nnnnn...

        -nnnn...    1
        nnnnn...

        nnnnn...    0
        nnnnn...

        nnnnn...   -1
        -nnnn...

        nnnnn...   -2
        --nnn...


    The algorithm first selects the lexicographically smallest
    of the top or bottom strands.

    For positive overhang, the top strand is is left padded with the number
    of hyphen characters (ASCII 45) indicated by the overhang value.

    For negative overhang the reverse of the bottom strand is similarly padded.

    The string pair is similarly padded on the other side, so that two eaqual
    length strings are formed.

    The two string are joined, separated by a line break (ASCII 10) and the
    lsSEGUID function is used on the resulting string.

    ::

        dsDNA       overhang  ldSEGUID

        -TATGCC     1        Jv9Z9JJ0IYnG-dTPBGwhDyAqnmU
         |||||
        catacg-

        -gcatac     1        Jv9Z9JJ0IYnG-dTPBGwhDyAqnmU
         |||||
        CCGTAT-

    For the linear dsDNA sequence defined by Watson = "TATGCC", Crick ="gcatac"
    and overhang = 1 (see figures above), The "gcatac" strand is selected as
    "gcatac" < "TATGCC".

    Overhang is positive, so the first strand is padded to "-gcatac".

    A string is constructed like so:
    ::

        "-gcatac" + chr(10) + "CCGTAT-"

    The checksum is prefixed with "ldseguid-"

    Examples
    --------
    >>> ldseguid("TATGCC", "GCATAC", 1)
    'ldseguid-E7YtPGWjj3qCaPzWurlYBaJy_X4'
    >>> ldseguid("GCATAC", "TATGCC", 1)
    'ldseguid-E7YtPGWjj3qCaPzWurlYBaJy_X4'
    """
    assert watson, "Watson sequence must not be empty"
    assert crick, "Crick sequence must not be empty"

    tb = tablefactory(table)

    assert len(set(tb.values())) > 1, "Was a protein table used by mistake?"
    assert_anneal(watson, crick, overhang, table=tb)

    w, c, o = min(
        (watson, crick, overhang),
        (crick, watson, len(watson) - len(crick) + overhang),
    )

    msg = repr_from_tuple(watson=w, crick=c, overhang=o, table=tb, space="-")

    extable = table + ",--,\n\n"

    return ldseguid_prefix + _seguid(msg, table=extable, encoding=base64.urlsafe_b64encode)


def cdseguid(watson: str, crick: str, table: str = "{DNA}") -> str:
    """SEGUID checksum for double stranded circular DNA (dcSEGUID).

    The dcSEGUID is the slSEGUID checksum calculated for the lexicographically
    smallest string rotation of a dsDNA sequence. Only defined for circular
    sequences.

    The checksum is prefixed with "cdseguid-"
    """
    assert watson, "Watson sequence must not be empty"
    assert crick, "Crick sequence must not be empty"

    tb = tablefactory(table)

    assert len(set(tb.values())) > 1, "Was a protein table used by mistake?"
    assert len(watson) == len(crick)

    assert_anneal(watson, crick, 0, table=tb)

    watson_min = rotate_to_min(watson)
    crick_min = rotate_to_min(crick)

    # Keep the "minimum" of the two variants
    if watson_min < crick_min:
        w = watson_min
    else:
        w = crick_min

    return (
        cdseguid_prefix + ldseguid(watson=w, crick=rc(w, table=tb), overhang=0, table=table)[len(ldseguid_prefix) :]
    )


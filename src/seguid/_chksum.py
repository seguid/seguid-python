#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
seguid.

The seguid module provides four functions for calculations of SEGUID checksums
for biological sequences with varying topologies

lsseguid (l)inear   (s)ingle-stranded SEGUID
csseguid (c)ircular (s)ingle-stranded SEGUID
ldseguid (l)inear   (d)ouble-stranded SGUID
cdseguid (c)ircular (d)ouble-stranded SEGUID

Some auxillary functions are also provided.

The functions can be made to work without external dependencies, but
csseguid and cdseguid are considerably faster with pydivsufsort installed.

"""

import hashlib
import base64

from seguid._manip import reverse
from seguid._manip import rotate
from seguid._manip import rotate_to_min

from seguid._tables import tablefactory
from seguid._asserts import assert_in_alphabet
from seguid._asserts import assert_complementary

seguid_prefix: str = "seguid="
lsseguid_prefix: str = "lsseguid="
csseguid_prefix: str = "csseguid="
ldseguid_prefix: str = "ldseguid="
cdseguid_prefix: str = "cdseguid="
b64alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/_-")
short = 6


def _seguid(
    seq: str,
    alphabet: str = "{DNA}",
    encoding: callable = base64.standard_b64encode,
) -> str:
    assert callable(encoding)
    assert seq, "A sequence must not be empty"
    assert_in_alphabet(seq, alphabet=set(tablefactory(alphabet).keys()))
    m = hashlib.sha1()
    m.update(seq.encode("ASCII"))
    hs = encoding(m.digest())
    csum = f"{hs.decode('ASCII').rstrip('=')}"
    assert len(csum) == 27
    assert set(csum).issubset(b64alphabet)
    return csum


def _form(prefix, csum, form):
    longform = ""
    shortform = ""
    if form != "short":
        longform = prefix + csum
    if form != "long":
        shortform = csum[:short]
    return " ".join((shortform, longform)).strip()


def seguid(seq: str, alphabet: str = "{DNA}", form: str = "long") -> str:
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

    The checksum is prefixed with "seguid="

    Examples
    --------
    >>> seguid("AT")
    'seguid=Ax/RG6hzSrMEEWoCO1IWMGska+4'
    """
    return _form(
        seguid_prefix,
        _seguid(seq, alphabet=alphabet, encoding=base64.standard_b64encode),
        form,
    )


def lsseguid(seq: str, alphabet: str = "{DNA}", form: str = "long") -> str:
    """SEGUID checksum for single stranded linear DNA (slSEGUID).

    Identical to the seguid function except for that the '+' and '/' characters
    of standard Base64 encoding are replaced by '-' and '_', respectively
    following the standard in RFC 4648 section 5.

    The base64.urlsafe_b64encode from the Python standard libary is used.

    This checksum is applicable to single stranded linear DNA sequences.
    Can also be used for protein sequences.

    The checksum is prefixed with "lsseguid="

    Examples
    --------
    >>> lsseguid("AT")
    'lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
    """
    return _form(
        lsseguid_prefix,
        _seguid(seq, alphabet=alphabet, encoding=base64.urlsafe_b64encode),
        form,
    )


def csseguid(seq: str, alphabet: str = "{DNA}", form: str = "long") -> str:
    r"""SEGUID checksum for single stranded circular DNA (csSEGUID).

    The csSEGUID is the lsSEGUID checksum calculated for the lexicographically
    smallest string rotation of a ssDNA sequence.

    Only defined for circular sequences.

    The checksum is prefixed with "csseguid="

    Examples
    --------
    >>> csseguid("ATTT")
    'csseguid=ot6JPLeAeMmfztW1736Kc6DAqlo'
    >>> lsseguid("ATTT")
    'lsseguid=ot6JPLeAeMmfztW1736Kc6DAqlo'
    >>> csseguid("TTTA")
    'csseguid=ot6JPLeAeMmfztW1736Kc6DAqlo'
    >>> lsseguid("TTTA")
    'lsseguid=8zCvKwyQAEsbPtC4yTV-pY0H93Q'
    """
    return _form(
        csseguid_prefix,
        _seguid(
            rotate_to_min(seq), alphabet=alphabet, encoding=base64.urlsafe_b64encode
        ),
        form,
    )


def ldseguid(
    watson: str, crick: str, alphabet: str = "{DNA}", form: str = "long"
) -> str:
    r"""SEGUID checksum for double stranded linear DNA (ldSEGUID).

    Calculates the ldSEGUID checksum for a dsDNA sequence defined by two
    strings representing the upper (Watson) and the complementary (Crick) DNA strands.
    Optional ssDNA regions in the ends are indicated by a dash "-" in eather strand.
    Watson and Crick strands are always equal in length.

    The algorithm first selects the lexicographically smallest of the Watson and Crick strands.

    The two string are joined 5'-3', separated by a semicolon ";" and the lsSEGUID function
    is used on the resulting string.

    ::

        dsDNA    ldSEGUID

        -TATGCC  ldseguid=rr65d6AYuP-CdMaVmdw3L9FPt6I
         |||||
        CATACG-

        -GCATAC  ldseguid=rr65d6AYuP-CdMaVmdw3L9FPt6I
         |||||
        CCGTAT-

    For the linear dsDNA sequence defined by watson = "-TATGCC", crick ="-GCATAC"
    (see figures above), The "-GCATAC" strand is selected since lexicographically,
    "-GCATAC" < "-TATGCC".

    A string is constructed like so:
    ::

        "-GCATAC" + ";" + "-TATGCC"

    The checksum is prefixed with "ldseguid="

    Examples
    --------
    >>> ldseguid("-TATGCC", "-GCATAC")
    'ldseguid=rr65d6AYuP-CdMaVmdw3L9FPt6I'
    >>> ldseguid("-GCATAC", "-TATGCC")
    'ldseguid=rr65d6AYuP-CdMaVmdw3L9FPt6I'
    """
    assert watson, "Watson sequence must not be empty"
    assert crick, "Crick sequence must not be empty"
    assert len(watson) == len(crick)
    assert_complementary(watson, crick, alphabet=alphabet)

    tb = tablefactory(alphabet)
    assert len(set(tb.values())) > 1, "Was a single-stranded alphabet used by mistake?"

    exalphabet = alphabet + ",--,;;"

    if watson < crick:
        spec = watson + ";" + crick
    else:
        spec = crick + ";" + watson

    return _form(
        ldseguid_prefix,
        _seguid(spec, alphabet=exalphabet, encoding=base64.urlsafe_b64encode),
        form,
    )


def cdseguid(
    watson: str, crick: str, alphabet: str = "{DNA}", form: str = "long"
) -> str:
    """SEGUID checksum for double stranded circular DNA (dcSEGUID).

    The dcSEGUID is the slSEGUID checksum calculated for the lexicographically
    smallest string rotation of a dsDNA sequence. Only defined for circular
    sequences.

    The checksum is prefixed with "cdseguid="
    """
    from seguid.config import _min_rotation

    assert watson, "Watson sequence must not be empty"
    assert crick, "Crick sequence must not be empty"
    assert len(watson) == len(crick)
    assert_complementary(watson, crick, alphabet=alphabet)

    amount_watson = _min_rotation(watson)
    watson_min = rotate(watson, amount=amount_watson)
    amount_crick = _min_rotation(crick)
    crick_min = rotate(crick, amount=amount_crick)

    # Keep the "minimum" of the two variants
    if watson_min < crick_min:
        w = watson_min
        c = rotate(crick, amount=-amount_watson)
    else:
        w = crick_min
        c = rotate(watson, amount=-amount_crick)

    return _form(
        cdseguid_prefix,
        ldseguid(watson=w, crick=c, alphabet=alphabet, form="long")[
            len(ldseguid_prefix) :
        ],
        form,
    )

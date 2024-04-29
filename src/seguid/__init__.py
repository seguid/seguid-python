#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SEGUID checksums for linear, circular, single- and double-stranded sequences
----------------------------------------------------------------------------

================ ============== ====================
 Topology         Strandedness   Function
================ ============== ====================
 **l**\ inear     **s**\ ingle     ``lsseguid()``
 **c**\ ircular   **s**\ ingle     ``csseguid()``
 **l**\ inear     **d**\ ouble     ``ldseguid()``
 **c**\ ircular   **d**\ ouble     ``cdseguid()``
================ ============== ====================

Four SEGUID v2 checksum functions for biological sequences with linear or circular
topology and a single or two complementary strands.

A detailed description of the algorithms can be found in Pereira et al. (2024).
Implementations of these functions in other programming languages cand be found
at `seguid.org <https://www.seguid.org/>`_.

The function ``seguid()`` that calculates checksum according to the original SEGUID v1 specification (Babnigg & Giometti, 2006)
is also provided.

This package works without external dependencies, but ``csseguid()`` and ``cdseguid()``
can be made faster by installing `pydivsufsort <https://pypi.org/project/pydivsufsort/>`_, provides a faster implementation of the algorithm for finding the
`smallest string rotation <https://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation>`_.


Usage
-----

.. code-block:: python

    lsseguid(seq, alphabet="{DNA}", form="long")

    csseguid(seq, alphabet="{DNA}", form="long")

    ldseguid(watson, crick, alphabet="{DNA}", form="long")

    cdseguid(watson, crick, alphabet="{DNA}", form="long")

    seguid(seq, alphabet="{DNA}", form="long")


Function arguments
------------------

**seq** (string)
The sequence for which the checksum should be calculated. The sequence may only comprise of symbols in the
alphabet specified by the alphabet argument.

**watson, crick** (strings)
Two reverse-complementary DNA sequences. Both sequences should be specified in the 5'-to-3' direction.

**alphabet** (string)
The type of sequence used. If ``"{DNA}"`` (default), then the input is a DNA sequence. If ``"{RNA}"``, then the
input is an RNA sequence. If ``"{protein}"``, then the input is an amino-acid sequence. If ``"{DNA-extended}"``
or ``"{RNA-extended}"``, then the input is a DNA or RNA sequence specified an extended set of symbols, including
IUPAC symbols (4). If ``"{protein-extended}"``, then the input is an amino-acid sequence with an extended set
of symbols, including IUPAC symbols (5). A custom alphabet may also be used. A non-complementary alphabet
is specified as a comma-separated set of single symbols, e.g. ``"X,Y,Z"``. A complementary alphabet is specified
as a comma-separated set of paired symbols, e.g. ``"AT,CG"``. It is also possible to extend a pre-defined
alphabet, e.g. ``"{DNA},XY"``.

**form** (string)
How the checksum is presented. If ``"long"`` (default), the full-length checksum is returned. If ``"short"``,
the short, six-digit checksum is returned. If ``"both"``, both the short and the long checksums are returned.


Value
-----

The SEGUID functions return a single string, if form is either ``"long"`` or ``"short"``. If form
is ``"both"``, then a tuple of two strings is returned, where the first component holds the ``"short"``
checksum and the second the ``"long"`` checksum. The long checksum, without the prefix, is a string with 27
characters. The short checksum, without the prefix, is the first six characters of the long checksum.
All long checksums are prefixed with a label indicating which SEGUID method was used. Except for ``seguid()``,
which uses Base64 encoding, all functions produce checksums using the Base64url encoding
("Base 64 Encoding with URL and Filename Safe Alphabet").


Base64 and Base64url encodings
------------------------------

The Base64url encoding is the Base64 encoding with non-URL-safe characters substituted with URL-safe ones (Josefsson, 2006).
Specifically, the plus symbol (``+``) is replaced by the minus symbol (``-``), and the forward slash (``/``) is replaced
by the underscore symbol (``_``).

The Base64 checksum used for the original SEGUID checksum is not guaranteed to contain symbols
that can safely be used as-is in a Uniform Resource Locator (URL). Specifically, it may consist of forward
slashes (``/``) and plus symbols (``+``), which are characters that carry special meaning in a URL. For the same
reason, a Base64 checksum cannot safely be used as a file or directory name, because it may have a forward slash.

The checksum returned is always 27-character long. This is because the SHA-1 hash (6) is 160-bit long
(20 bytes), which result in the encoded representation always end with a padding character (``=``) so that the
length is a multiple of four character. We relax this requirement, by dropping the padding character.





References
----------

1. G Babnigg & CS Giometti, A database of unique protein sequence identifiers for proteome studies. Proteomics. 2006 Aug;6(16):4514-22, `doi:10.1002/pmic.200600032 <https://doi.org/10.1002/pmic.200600032>`_.

2. H Pereira, PC Silva, WM Davis, L Abraham, G Babnigg, H Bengtsson & B Johansson, SEGUID v2: Extending SEGUID Checksums for Circular, Linear, Single- and Double-Stranded Biological Sequences, bioRxiv, `doi:10.1101/2024.02.28.582384 <https://doi.org/10.1101/2024.02.28.582384>`_.

3. S Josefsson, The Base16, Base32, and Base64 Data Encodings, RFC 4648, October 2006, `doi:10.17487/RFC4648 <https://doi.org/10.17487/RFC4648>`_.

4. Wikipedia article 'Nucleic acid notation', February 2024, https://en.wikipedia.org/wiki/Nucleic_acid_notation.

5. Wikipedia article 'Amino acids', February 2024, https://en.wikipedia.org/wiki/Amino_acid.

6. Wikipedia article 'SHA-1' (Secure Hash Algorithm 1), December 2023, https://en.wikipedia.org/wiki/SHA-1.

"""

try:
    # importlib only avaliable in Python 3.8 and up
    from importlib.metadata import version as _version
except ModuleNotFoundError:
    try:
        # pkg_resources avaliable in Python 3.6-3.7 from setuptools =< 59.6.0
        import pkg_resources
    except ModuleNotFoundError:
        __version__ = "0.0.0"
    else:
        __version__ = pkg_resources.get_distribution(__package__).version
else:
    __version__ = _version(__package__)

from seguid._chksum import seguid
from seguid._chksum import lsseguid
from seguid._chksum import csseguid
from seguid._chksum import ldseguid
from seguid._chksum import cdseguid

__all__ = ["seguid", "lsseguid", "csseguid", "ldseguid", "cdseguid"]

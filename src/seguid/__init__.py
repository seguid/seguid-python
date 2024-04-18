#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The seguid module provides four functions for calculations of SEGUID checksums
for biological sequences with varying topologies:

 * lsseguid: (l)inear   (s)ingle-stranded SEGUID
 * csseguid: (c)ircular (s)ingle-stranded "
 * ldseguid: (l)inear   (d)ouble-stranded "
 * cdseguid: (c)ircular (d)ouble-stranded "

A detailed description of the algorithms can be found in Pereira et al. 2024.
Implementations of these functions in other programming languages cand be found
at `seguid.org <https://www.seguid.org/>`_.

The original seguid function (Babnigg & Giometti, 2006) is also provided along
with some auxillary functions.

This package works without external dependencies, but csseguid and cdseguid
can be made considerably faster by installing `pydivsufsort <https://pypi.org/project/pydivsufsort/>`_
since a faster algorithm for finding the `smallest string
rotation <https://en.wikipedia.org/wiki/Lexicographically_minimal_string_rotation>`_ is provided.

References
==========

* Pereira, Humberto, Paulo César Silva, Wayne M Davis, Louis Abraham, Gyorgy Babnigg,
  Henrik Bengtsson, and Bjorn Johansson. 2024. “SEGUID v2: Extending SEGUID Checksums
  for Circular, Linear, Single- and Double-Stranded Biological Sequences.” bioRxiv.
  https://doi.org/10.1101/2024.02.28.582384.

* Babnigg, G., & Giometti, C. S. (2006). A database of unique protein
  sequence identifiers for proteome studies. Proteomics, 6(16), 4514–4522.
  https://doi.org/10.1002/pmic.200600032

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

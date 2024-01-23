#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid import lsseguid
from seguid import csseguid
from seguid import ldseguid
from seguid import cdseguid


def _test_speed():
    import timeit

    dna500 = """\
    CAGTGAAATCAGAACCCATGAGGGCGGACGAGTCATATCC
    GGTATTAGAGATTTATACAGTCTGGACACCTAGCGAACCG
    ACTTGAACCACCAGGATTGAAGACGAAACCTTAGAGTATA
    GTAATGCCGTACGTGTCGGGGCCCACGCATCTAGGACAGG
    ATCGCATGATGGTGGTTTTAGTTGCCGTTGTACCGGATTT
    CTTAGTAGTATAAGCATGAGGATAAGTGAAACCGGGTGAA
    GGTGGTTTGTGTGAGTGCCTAATAGTCCGACTCCCCGAGG
    GGAGTAGGCACTGCCTTCAGCGTTCAGTTATTGAGCACGT
    CCGCCCGGCGAAAGATGGCTTTGAGCTCCACTGACAGCCA
    GGGACCGCGTGCATGAGGCTAGAGCAGAGTCGTTGACAGT
    GAGATTAGATTGATCATTTTTATCTGAAACGGCAGCATAC
    CGACAGTTGTTCTCAAGCAAAGTGGTCTTGCCTAGATTCA
    ATATTGCCCACAATCAGCTC""".replace(
        "\n", ""
    )

    print("pure Python : ", end="")
    print(
        timeit.timeit(
            "cseguid(dna500, minrotation=min_rotation)",
            globals=globals(),
            number=1000,
        )
    )
    print("pydivsufsort: ", end="")
    print(timeit.timeit("cseguid(dna500)", globals=globals(), number=1000))

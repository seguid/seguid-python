#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from seguid import slseguid
from seguid import scseguid
from seguid import dlseguid
from seguid import dcseguid


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

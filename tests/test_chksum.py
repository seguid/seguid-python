#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from pathlib import Path
from hashlib import sha1
from base64 import urlsafe_b64encode as b64us

from seguid import slseguid
from seguid import scseguid
from seguid import dlseguid
from seguid import dcseguid

from seguid.chksum import seguid

from seguid.manip import reverse
from seguid.manip import rc

from seguid.reprutils import repr_from_tuple

from seguid.tables import COMPLEMENT_TABLE_DNA
from seguid.tables import COMPLEMENT_TABLE_RNA
from seguid.tables import COMPLEMENT_TABLE_IUPAC
from seguid.tables import TABLE_IUPAC_PROTEIN


def test_seguid():
    assert seguid("AT") == "seguid:Ax/RG6hzSrMEEWoCO1IWMGska+4"
    NP_313053_1 = (
        "MKALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSG"
        "ASRGIRLLQEEEEGLPLVGRVAAGEPLLAQQHIEGHYQVDPSLFKPNADFLLRVSGMSMKD"
        "IGIMDGDLLAVHKTQDVRNGQVVVARIDDEVTVKRLKKQGNKVELLPENSEFKPIVVDLRQ"
        "QSFTIEGLAVGVIRNGDWL"
    )

    assert seguid(NP_313053_1, table=TABLE_IUPAC_PROTEIN) == "seguid:2c4yjE+JqjvzYF1d0OmUh8pCpz8"




def cs(arg):
    return (
        b64us(sha1(arg.encode("ASCII")).digest()).decode("ASCII").rstrip("=")
    )


def test_slseguid():
    assert slseguid("AT") == "slseguid:Ax_RG6hzSrMEEWoCO1IWMGska-4"
    assert cs("AT") in slseguid("AT")


def test_scseguid():
    m13dna = Path("test_data/M13.txt").read_text().strip()
    sc = "scseguid:aAjgnsF9cPI6cu8IQ81sYnstVzU"
    assert scseguid(m13dna) == sc
    assert cs(Path("test_data/M13_minimal_rotation.txt").read_text().strip()) in sc

    scseguid("ATTT") == 'scseguid:ot6JPLeAeMmfztW1736Kc6DAqlo'
    slseguid("ATTT") == 'slseguid:ot6JPLeAeMmfztW1736Kc6DAqlo'
    scseguid("TTTA") == 'scseguid:ot6JPLeAeMmfztW1736Kc6DAqlo'
    slseguid("TTTA") == 'slseguid:8zCvKwyQAEsbPtC4yTV-pY0H93Q'




def test_dlseguid():
    ct = COMPLEMENT_TABLE_DNA
    table = ct | {"\n":"\n", "-":"-"}
    # AT
    # TA

    dlDNA = "AT"
    dlDNA_dlseguid = "AWD-dt5-TEua8RbOWfnctJIu9nA"
    assert dlseguid(dlDNA, rc(dlDNA), 0) == f"dlseguid:{dlDNA_dlseguid}"
    assert dlDNA_dlseguid in slseguid("AT\nTA", table = table)
    assert cs("AT\nTA") == dlDNA_dlseguid

    #  -AT
    #  AT-

    dlDNA2 = ("AT", "TA", 1)
    dlDNA2_dlseguid = "JwB2eUmZkCNjyWAv471JeUbiSDM"
    assert dlseguid(*dlDNA2) == f"dlseguid:{dlDNA2_dlseguid}"
    assert dlDNA2_dlseguid in slseguid("-AT\nAT-", table = table)
    assert cs("-AT\nAT-") == dlDNA2_dlseguid

    # TA-
    # -TA

    dlDNA3 = ("TA", "AT", -1)
    dlDNA3_dlseguid = "bv0UOR12eWrBeaAx79PNZvveviU"
    assert dlseguid(*dlDNA3) == f"dlseguid:{dlDNA3_dlseguid}"
    assert dlDNA3_dlseguid in slseguid("AT-\n-AT", table = table)
    assert cs("AT-\n-AT") == dlDNA3_dlseguid

    # CTATAG
    #   TA

    dlDNA4 = ("CTATAG", "AT", -2)
    dlDNA4_dlseguid = "np3hncfQvOh8rZ8Co1Ts_02NXg4"
    assert dlseguid(*dlDNA4) == f"dlseguid:{dlDNA4_dlseguid}"
    assert dlDNA4_dlseguid in slseguid("--AT--\nGATATC", table = table)
    assert cs("--AT--\nGATATC") == dlDNA4_dlseguid

    #   AT
    # GATATC

    dlDNA5 = ("AT", "CTATAG", 2)
    dlDNA5_dlseguid = "np3hncfQvOh8rZ8Co1Ts_02NXg4"
    assert dlseguid(*dlDNA5) == f"dlseguid:{dlDNA4_dlseguid}"
    assert dlDNA5_dlseguid in slseguid("--AT--\nGATATC", table = table)
    assert cs("--AT--\nGATATC") == dlDNA5_dlseguid

    repr_from_tuple("AT", "CTATAG", 2)

    assert dlseguid("TATGCC", "GCATAC", 1) == 'dlseguid:E7YtPGWjj3qCaPzWurlYBaJy_X4'
    assert dlseguid("GCATAC", "TATGCC", 1) == 'dlseguid:E7YtPGWjj3qCaPzWurlYBaJy_X4'


def test_dcseguid():
    pUC19dna = Path("test_data/pUC19.txt").read_text().strip()
    dcsg = "dcseguid:zhw8Yrxfo3FO5DDccx4PamBVPCQ"
    assert dcseguid(pUC19dna, rc(pUC19dna)) == dcsg
    w, c = Path("test_data/pUC19_minimal_rotation_watson_linebreak_crick.txt").read_text().splitlines()
    assert dlseguid(w, c[::-1], 0) == "dlseguid:zhw8Yrxfo3FO5DDccx4PamBVPCQ"

    truth = "dcseguid:tYeHZYwxQGDHTqGDcrebERag0AU"
    assert dcseguid("ACGTT", "AACGT") == truth
    assert dcseguid("AACGT", "ACGTT") == truth


def test_with_tables():

    result = 'seguid:Ax/RG6hzSrMEEWoCO1IWMGska+4'
    result_rna = 'seguid:rN9Bc195AlLq45vug03K0N5Yfj0'
    assert seguid("AT", table=COMPLEMENT_TABLE_DNA) == result
    assert seguid("AU", table=COMPLEMENT_TABLE_RNA) == result_rna
    assert seguid("AT", table=COMPLEMENT_TABLE_IUPAC) == result
    assert seguid("AT", table=TABLE_IUPAC_PROTEIN) == result

    result = 'slseguid:Ax_RG6hzSrMEEWoCO1IWMGska-4'
    result_rna = 'slseguid:rN9Bc195AlLq45vug03K0N5Yfj0'
    assert slseguid("AT", table=COMPLEMENT_TABLE_DNA) == result
    assert slseguid("AU", table=COMPLEMENT_TABLE_RNA) == result_rna
    assert slseguid("AT", table=COMPLEMENT_TABLE_IUPAC) == result
    assert slseguid("AT", table=TABLE_IUPAC_PROTEIN) == result

    result = 'scseguid:Ax_RG6hzSrMEEWoCO1IWMGska-4'
    result_rna = 'scseguid:rN9Bc195AlLq45vug03K0N5Yfj0'
    assert scseguid("AT", table=COMPLEMENT_TABLE_DNA) == result
    assert scseguid("AU", table=COMPLEMENT_TABLE_RNA) == result_rna
    assert scseguid("AT", table=COMPLEMENT_TABLE_IUPAC) == result
    assert scseguid("AT", table=TABLE_IUPAC_PROTEIN) == result

    result = 'dlseguid:AWD-dt5-TEua8RbOWfnctJIu9nA'
    result_rna = 'dlseguid:1jgY1uMadj9rCRXKjeFDBK2jI44'
    assert dlseguid("AT", "AT", 0, table=COMPLEMENT_TABLE_DNA) == result
    assert dlseguid("AU", "AU", 0, table=COMPLEMENT_TABLE_RNA) == result_rna
    assert dlseguid("AT", "AT", 0, table=COMPLEMENT_TABLE_IUPAC) == result
    with pytest.raises(AssertionError):
        dlseguid("AT", "AT", 0, table=TABLE_IUPAC_PROTEIN)

    result = 'dcseguid:AWD-dt5-TEua8RbOWfnctJIu9nA'
    result_rna = 'dcseguid:1jgY1uMadj9rCRXKjeFDBK2jI44'
    assert dcseguid("AT", "AT", table=COMPLEMENT_TABLE_DNA) == result
    assert dcseguid("AU", "AU", table=COMPLEMENT_TABLE_RNA) == result_rna
    assert dcseguid("AT", "AT", table=COMPLEMENT_TABLE_IUPAC) == result
    with pytest.raises(AssertionError):
        assert dcseguid("AT", "AT", table=TABLE_IUPAC_PROTEIN) == result

def test_empty():

    with pytest.raises(AssertionError):
        seguid("")

    with pytest.raises(AssertionError):
        slseguid("")

    with pytest.raises(AssertionError):
        scseguid("")

    with pytest.raises(AssertionError):
        dlseguid("", "", overhang=0)

    with pytest.raises(AssertionError):
        dcseguid("", "")

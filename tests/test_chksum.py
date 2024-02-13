#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

import tempfile
import os

from pathlib import Path
from hashlib import sha1
from base64 import urlsafe_b64encode as b64us

from seguid import lsseguid
from seguid import csseguid
from seguid import ldseguid
from seguid import cdseguid

from seguid.chksum import seguid

from seguid.manip import reverse


def test_seguid():
    assert seguid("AT") == "seguid=Ax/RG6hzSrMEEWoCO1IWMGska+4"
    NP_313053_1 = (
        "MKALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSG"
        "ASRGIRLLQEEEEGLPLVGRVAAGEPLLAQQHIEGHYQVDPSLFKPNADFLLRVSGMSMKD"
        "IGIMDGDLLAVHKTQDVRNGQVVVARIDDEVTVKRLKKQGNKVELLPENSEFKPIVVDLRQ"
        "QSFTIEGLAVGVIRNGDWL"
    )

    assert seguid(NP_313053_1, alphabet="{protein}") == "seguid=2c4yjE+JqjvzYF1d0OmUh8pCpz8"




def cs(arg):
    return (
        b64us(sha1(arg.encode("ASCII")).digest()).decode("ASCII").rstrip("=")
    )


def test_lsseguid():
    assert lsseguid("AT") == "lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4"
    assert cs("AT") in lsseguid("AT")


def test_csseguid():
    m13dna = Path("test_data/M13.txt").read_text().strip()
    sc = "csseguid=aAjgnsF9cPI6cu8IQ81sYnstVzU"
    assert csseguid(m13dna) == sc
    assert cs(Path("test_data/M13_minimal_rotation.txt").read_text().strip()) in sc

    csseguid("ATTT") == 'csseguid=ot6JPLeAeMmfztW1736Kc6DAqlo'
    lsseguid("ATTT") == 'lsseguid=ot6JPLeAeMmfztW1736Kc6DAqlo'
    csseguid("TTTA") == 'csseguid=ot6JPLeAeMmfztW1736Kc6DAqlo'
    lsseguid("TTTA") == 'lsseguid=8zCvKwyQAEsbPtC4yTV-pY0H93Q'




def test_ldseguid():
    ct = "{DNA}"
    alphabet = ct + ",--,\n\n"
    # AT
    # TA

    dlDNA_ldseguid = "AWD-dt5-TEua8RbOWfnctJIu9nA"
    truth = f"ldseguid={dlDNA_ldseguid}"
    assert dlDNA_ldseguid in lsseguid("AT\nTA", alphabet = alphabet)
    assert cs("AT\nTA") == dlDNA_ldseguid
    assert ldseguid("AT", "AT") == truth

    #  -AT
    #  AT-

    dlDNA2_ldseguid = "JwB2eUmZkCNjyWAv471JeUbiSDM"
    truth = f"ldseguid={dlDNA2_ldseguid}"
    assert dlDNA2_ldseguid in lsseguid("-AT\nAT-", alphabet = alphabet)
    assert cs("-AT\nAT-") == dlDNA2_ldseguid
    assert ldseguid("-AT", "-TA") == truth
    
    # TA-
    # -TA

    dlDNA3_ldseguid = "XBcVadfQevTW_lklW4rdqw5udQ8"
    truth = f"ldseguid={dlDNA3_ldseguid}"
    assert dlDNA3_ldseguid in lsseguid("-TA\nTA-", alphabet = alphabet)
    assert cs("-TA\nTA-") == dlDNA3_ldseguid
    assert ldseguid("-TA", "-AT") == truth
    
    # CTATAG
    # --TA--

    dlDNA4_ldseguid = "_E05Xeo7KnLxrjsqDdpXNw_AIDE"
    truth = f"ldseguid={dlDNA4_ldseguid}"
    assert dlDNA4_ldseguid in lsseguid("--TA--\nCTATAG", alphabet = alphabet)
    assert cs("--TA--\nCTATAG") == dlDNA4_ldseguid
    assert ldseguid("CTATAG", "--AT--") == truth
    
    # --AT--
    # GATATC

    dlDNA5_ldseguid = "np3hncfQvOh8rZ8Co1Ts_02NXg4"
    truth = f"ldseguid={dlDNA5_ldseguid}"
    assert dlDNA5_ldseguid in lsseguid("--AT--\nGATATC", alphabet = alphabet)
    assert cs("--AT--\nGATATC") == dlDNA5_ldseguid
    ldseguid("--AT--", "CTATAG") == truth
    
    assert ldseguid("-TATGCC", "-GCATAC") == 'ldseguid=I6X4lBK0sBSc7WeeaaZvEoKmTYo'
    assert ldseguid("-GCATAC", "-TATGCC") == 'ldseguid=E7YtPGWjj3qCaPzWurlYBaJy_X4'


def test_cdseguid():
    pUC19dna = Path("test_data/pUC19.txt").read_text().strip()
    dcsg = "cdseguid=zhw8Yrxfo3FO5DDccx4PamBVPCQ"
    pUC19dna_rc = reverse(pUC19dna.translate(str.maketrans("ACGT", "TGCA")))
    assert cdseguid(pUC19dna, pUC19dna_rc) == dcsg
    w, c = Path("test_data/pUC19_minimal_rotation_watson_linebreak_crick.txt").read_text().splitlines()
    assert ldseguid(w, c[::-1]) == "ldseguid=zhw8Yrxfo3FO5DDccx4PamBVPCQ"

    truth = "cdseguid=tYeHZYwxQGDHTqGDcrebERag0AU"
    assert cdseguid("ACGTT", "AACGT") == truth
    assert cdseguid("AACGT", "ACGTT") == truth


def test_with_alphabets():

    result = 'seguid=Ax/RG6hzSrMEEWoCO1IWMGska+4'
    result_rna = 'seguid=rN9Bc195AlLq45vug03K0N5Yfj0'
    assert seguid("AT", alphabet="{DNA}") == result
    assert seguid("AU", alphabet="{RNA}") == result_rna
    assert seguid("AT", alphabet="{IUPAC}") == result
    assert seguid("AT", alphabet="{protein}") == result

    result = 'lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
    result_rna = 'lsseguid=rN9Bc195AlLq45vug03K0N5Yfj0'
    assert lsseguid("AT", alphabet="{DNA}") == result
    assert lsseguid("AU", alphabet="{RNA}") == result_rna
    assert lsseguid("AT", alphabet="{IUPAC}") == result
    assert lsseguid("AT", alphabet="{protein}") == result

    result = 'csseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
    result_rna = 'csseguid=rN9Bc195AlLq45vug03K0N5Yfj0'
    assert csseguid("AT", alphabet="{DNA}") == result
    assert csseguid("AU", alphabet="{RNA}") == result_rna
    assert csseguid("AT", alphabet="{IUPAC}") == result
    assert csseguid("AT", alphabet="{protein}") == result

    result = 'ldseguid=AWD-dt5-TEua8RbOWfnctJIu9nA'
    result_rna = 'ldseguid=1jgY1uMadj9rCRXKjeFDBK2jI44'
    assert ldseguid("AT", "AT", alphabet="{DNA}") == result
    assert ldseguid("AU", "AU", alphabet="{RNA}") == result_rna
    assert ldseguid("AT", "AT", alphabet="{IUPAC}") == result
    with pytest.raises(AssertionError):
        ldseguid("AT", "AT", alphabet="{protein}")

    result = 'cdseguid=AWD-dt5-TEua8RbOWfnctJIu9nA'
    result_rna = 'cdseguid=1jgY1uMadj9rCRXKjeFDBK2jI44'
    assert cdseguid("AT", "AT", alphabet="{DNA}") == result
    assert cdseguid("AU", "AU", alphabet="{RNA}") == result_rna
    assert cdseguid("AT", "AT", alphabet="{IUPAC}") == result
    with pytest.raises(AssertionError):
        assert cdseguid("AT", "AT", alphabet="{protein}") == result

def test_empty():

    with pytest.raises(AssertionError):
        seguid("")

    with pytest.raises(AssertionError):
        lsseguid("")

    with pytest.raises(AssertionError):
        csseguid("")

    with pytest.raises(AssertionError):
        ldseguid("", "")

    with pytest.raises(AssertionError):
        cdseguid("", "")


def test_checksum_as_filename():

    seq="GATTACA"
    ## Comment:
    ## The   SEGUID check is seguid=tp2jzeCM2e3W4yxtrrx09CMKa/8
    ## The slSEGUID check is seguid=tp2jzeCM2e3W4yxtrrx09CMKa_8
    with tempfile.TemporaryDirectory() as temp_dir:
        filename=os.path.join(temp_dir, lsseguid(seq))
        with open(filename, "w") as file:
            file.write(seq)
        assert os.path.isfile(filename)
        with open(filename, "r") as file:
             content = file.read()
        os.remove(filename)
        assert content == seq

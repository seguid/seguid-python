# from seguid.tables import COMPLEMENT_ALPHABET_DNA
# from textwrap import dedent
from inspect import cleandoc
from seguid.asserts import assert_in_alphabet
from seguid.asserts import assert_anneal
from seguid.manip import reverse
from seguid.tables import tablefactory
import re

def tuple_from_repr(
    rpr: str,
    alphabet: str = "{DNA}",
    space: str = "-"
) -> tuple:
    """Generate a (watson, crick, overhang) tuple from dsDNA text representation.

    This function can generate a tuple (watson, crick, overhang)
    from a dsDNA figure such as the ones depicted below. The resulting
    tuple can be used as an argument for the lSEGUID_sticky or nseguid
    functions. See these functions for the definition of watson, crick and
    overhang. Example inputs can be:
    ::

              -TATGCC
              CATACG-


              GTATGCC
              CATACGG


              GTATGC-
              -ATACGG


    The first and last figure above represent DNA with single
    stranded ends, 3' and 5' respectively. The dash represent
    an empty space in the DNA sequence. This is only allowed
    on one of the adjacent positions. The following is *not*
    allowed:
    ::

              -TATGCC
              -ATACGG


    Examples
    --------
    >>> rpr1 = \"""-TATGCC
    ...           CATACG-\"""
    >>> tuple_from_repr(rpr1)
    ('TATGCC', 'GCATAC', 1)
    >>> rpr2 = \"""GTATGCC
    ...            CATACGG\"""
    >>> tuple_from_repr(rpr2)
    ('GTATGCC', 'GGCATAC', 0)
    >>> rpr3 = \"""GTATGC-
    ...            -ATACGG\"""
    >>> tuple_from_repr(rpr3)
    ('GTATGC', 'GGCATA', -1)
    """
    assert isinstance(space, str)
    assert len(space) == 1
    assert space != " ", "Space can not be 'space' (ASCII 32)"
    linebreak = "\n"

    tabledict = tablefactory(alphabet)

    try:
        assert_in_alphabet(space, alphabet=set(tabledict.keys()) | set(linebreak))
    except ValueError:
        pass
    else:
        ValueError(f"space was set to {space} which is already in the alphabet")

    cleaned_rpr = cleandoc(rpr)

    assert_in_alphabet(cleaned_rpr,
                       alphabet=set(tabledict.keys()) | set(space) | set(linebreak))

    watson, crickrv = cleaned_rpr.splitlines()

    assert len(watson) == len(crickrv)
    assert not (watson.startswith(space) and crickrv.startswith(space))
    assert not (watson.endswith(space) and crickrv.endswith(space))

    overhang = (
        len(watson) - len(watson.lstrip(space)) - (len(crickrv) - len(crickrv.lstrip(space)))
    )

    result = watson.strip(space), crickrv.strip(space)[::-1], overhang
    assert_anneal(*result, alphabet={**tabledict, **{space: space}})

    return result


def repr_from_tuple(
    watson: str,
    crick: str,
    overhang: int,
    alphabet: str = "{DNA}",
    space: str = "-"
) -> str:
    """docstring."""
    assert_anneal(watson, crick, overhang=overhang, alphabet = tablefactory(alphabet))
    assert isinstance(space, str)
    assert len(space) == 1

    msg = (
        f"{overhang*space}{watson}{space*(-overhang+len(crick)-len(watson))}"
        "\n"
        f"{-overhang*space}{reverse(crick)}{space*(overhang+len(watson)-len(crick))}"
    ).rstrip()

    return msg


def watson_crick_from_tuple(
    watson: str,
    crick: str,
    overhang: int,
    space: str = "-"
) -> tuple:
    """docstring."""
    
    ## Nothing to do?
    if overhang == 0:
        return watson, crick

    
    if overhang > 0:
        watson_pad_left  = f"{+overhang*space}"
        watson_pad_right = f"{space*(-overhang+len(crick)-len(watson))}"
        crick_pad_left   = f"{space*(+overhang+len(watson)-len(crick))}"
        crick_pad_right  = f"{-overhang*space}"
    elif overhang < 0:
        crick_pad_left   = f"{-overhang*space}"
        crick_pad_right  = f"{space*(+overhang+len(watson)-len(crick))}"
        watson_pad_left  = f"{space*(-overhang+len(crick)-len(watson))}"
        watson_pad_right = f"{+overhang*space}"

    watson = f"{watson_pad_left}{watson}{watson_pad_right}"
    crick  = f"{crick_pad_left}{crick}{crick_pad_right}"

    return watson, crick



def dsseq_to_tuple(
    watson: str,
    crick: str,
    overhang: int,
) -> str:
    """docstring."""
    
    ## Staggeredness specified via dash symbols ('-')?
    if not "-" in watson and not "-" in crick:
        return watson, crick, overhang

    assert len(watson) == len(crick)
    pattern = r"^([-]*)([^-]*)([-]*)$"
    assert re.search(pattern, watson)
    assert re.search(pattern, crick)
    
    match = re.match(pattern, watson)
    watson_trim = match.group(2)
    watson_pad_left = match.group(1)
    watson_pad_right = match.group(3)
    
    match = re.match(pattern, crick)
    crick_trim = match.group(2)
    crick_pad_left = match.group(1)
    crick_pad_right = match.group(3)
    
    if len(watson_pad_left) > 0:
        assert len(crick_pad_right) == 0
        overhang = len(watson_pad_left)
    elif len(crick_pad_left) > 0:
        assert len(watson_pad_right) == 0
        overhang = -len(crick_pad_left)
  
    watson = watson_trim
    crick = crick_trim

    return watson, crick, overhang


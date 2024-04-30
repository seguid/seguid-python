from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from seguid import __version__

from seguid._chksum import seguid
from seguid._chksum import lsseguid
from seguid._chksum import csseguid
from seguid._chksum import ldseguid
from seguid._chksum import cdseguid
from seguid._manip import reverse
from seguid._reprutils import parse_sequence_string

parser = ArgumentParser(
    prog="python -m seguid",
    description="seguid: Sequence Globally Unique Identifier Checksums for Linear, Circular, Single- and Double-Stranded Biological Sequences",
    epilog=
"""
Predefined alphabets:
 '{DNA}'              Complementary DNA symbols (= 'AT,CG')
 '{DNA-extended}'     Extended DNA (= '{DNA},BV,DH,KM,SS,RY,WW,NN')
 '{RNA}'              Complementary RNA symbols (= 'AU,CG')
 '{RNA-extended}'     Extended DNA (= '{RNA},BV,DH,KM,SS,RY,WW,NN')
 '{protein}'          Amino-acid symbols (= 'A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y')
 '{protein-extended}' Amino-acid symbols (= '{protein},O,U,B,J,Z,X')

Examples:
python -m seguid --version
python -m seguid --help

echo 'ACGT' | python -m seguid --type=lsseguid
python -m seguid --type=lsseguid <<< 'ACGT'
python -m seguid --type=cdseguid <<< $'ACGT\\nTGCA' # two-line syntax
python -m seguid --type=ldseguid <<< 'ACGT;ACGT'   # watson-crick syntax
python -m seguid --type=ldseguid <<< $'-CGT\\nTGCA' # two-line syntax
python -m seguid --type=ldseguid <<< '-CGT;ACGT'   # watson-crick syntax
python -m seguid --type=lsseguid --alphabet='{RNA}' <<< 'ACGU'

Version: """ + __version__ + """
Copyright: Bjorn Johansson, Henrik Bengtsson (2023-2024)
License: MIT
""",
    formatter_class=RawDescriptionHelpFormatter  # Keeps the formatting of the epilog
)

parser.add_argument("--version",  action="store_true", help="Display version")
parser.add_argument("--type",     type=str, nargs="?", help="Type of checksum to calculate (lsseguid, csseguid, ldseguid, cdseguid, or seguid [default])")
parser.add_argument("--alphabet", type=str, nargs="?", help="Set of symbols for the input sequence, e.g. '{DNA}', 'AC,GT', and '{DNA},AU'")
parser.add_argument("--form",     type=str, nargs="?", help="Form of checksum to display ('long' [default], 'short', or 'both')")


args = vars(parser.parse_args())

if args.pop("version"):
    print(__version__)
else:
    form = args.pop("form")
    if form == None:
        form = "long"

    type = args.pop("type")
    if type == None:
        type = "seguid"

    alphabet = args.pop("alphabet")
    if alphabet == None:
        alphabet = "{DNA}"

    ## Read sequence data from the standard input
    lines = []
    try:
        while True:
            line = input()
            if not line:  # Optionally, break if an empty line is encountered
                break
            lines.append(line)
    except EOFError:
        pass
    seq = "\n".join(lines)

    if type == "seguid":
        res = seguid(seq, alphabet=alphabet, form=form)
    elif type == "lsseguid":
        res = lsseguid(seq, alphabet=alphabet, form=form)
    elif type == "csseguid":
        res = csseguid(seq, alphabet=alphabet, form=form)
    elif type == "ldseguid":
        void, void, watson, crick = parse_sequence_string(seq)
        res = ldseguid(watson=watson, crick=crick, alphabet=alphabet, form=form)
    elif type == "cdseguid":
        void, void, watson, crick = parse_sequence_string(seq)
        res = cdseguid(watson=watson, crick=crick, alphabet=alphabet, form=form)
    else:
        raise ValueError("Unknown --type='" + type + "'")

    if isinstance(res, tuple):
        res = " ".join(res)
        
    print(res)


from argparse import ArgumentParser
from seguid import __version__

from seguid.chksum import seguid
from seguid.chksum import lsseguid
from seguid.chksum import csseguid
from seguid.chksum import ldseguid
from seguid.chksum import cdseguid
from seguid._manip import reverse
from seguid.reprutils import parse_sequence_string

parser = ArgumentParser(
    prog="python -m seguid",
    description="seguid: Sequence Globally Unique Identifier (SEGUID) Checksums for Linear, Circular, Single-Stranded and Double-Stranded Biological Sequences",
)
parser.add_argument("--version", action="store_true", help="Show version")
parser.add_argument("--alphabet", type=str, nargs="?", help="Type of input sequence")
parser.add_argument("--type", type=str, nargs="?", help="Type of checksum to calculate")
parser.add_argument("--form", type=str, nargs="?", help="Form of checksum to return")


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

    print(res)

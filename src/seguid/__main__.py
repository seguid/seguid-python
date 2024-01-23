from argparse import ArgumentParser
from seguid import __version__

from seguid.chksum import seguid
from seguid.chksum import lsseguid
from seguid.chksum import csseguid
from seguid.chksum import ldseguid
from seguid.chksum import cdseguid
from seguid.manip import reverse
from seguid.reprutils import tuple_from_repr

parser = ArgumentParser(prog="python -m seguid", description="seguid: Sequence Globally Unique Identifier (SEGUID) for Nucleotide and Amino-Acid Sequences")
parser.add_argument("--version", action="store_true", help="Show version")
parser.add_argument("--type", type=str, nargs="?", help="Type of checksum to calculate")

args = vars(parser.parse_args())

if args.pop("version"):
    print(__version__)
else:
    type=args.pop("type")
    if type == None:
        type="seguid"
        
    ## Read sequence data from the standard input
    lines=[]
    try:
        while True:
            line = input()
            if not line:  # Optionally, break if an empty line is encountered
                break
            lines.append(line)
    except EOFError:
        pass
    seq="\n".join(lines)

    if type == "seguid":
        res=seguid(seq)
    elif type == "lsseguid":
        res=lsseguid(seq)
    elif type == "csseguid":
        res=csseguid(seq)
    elif type == "ldseguid":
        tuple=tuple_from_repr(seq)
        res=ldseguid(watson = tuple[0], crick = tuple[1], overhang = tuple[2])
    elif type == "cdseguid":
        tuple=tuple_from_repr(seq)
        res=cdseguid(watson = tuple[0], crick = tuple[1])
    else:
        raise ValueError("Unknown --type='" + type + "'")
    
    print(res)

from seguid._manip import reverse
import re


def is_staggered(watson, crick):
    return "-" in watson or "-" in crick


def escape_sequence_spec(spec):
    spec = spec.replace("\n", "\\n")
    return spec


def parse_sequence_string(spec: str) -> str:
    """docstring."""
    assert isinstance(spec, str)

    ## Single- or double-stranded sequence?
    pattern = r"^([0-9A-Za-z-]+)$"
    if re.match(pattern, spec):
        return "ss", spec

    ## "<watson>;<crick>"?
    pattern = r"^([0-9A-Za-z-]+);([0-9A-Za-z-]+)$"
    match = re.match(pattern, spec)
    if match:
        watson = match.group(1)
        crick = match.group(2)
        rcrick = reverse(crick)
        if len(watson) != len(crick):
            raise ValueError(
                "Double-strand sequence string specifies two strands of different lengths (%d != %d): '%s'"
                % (len(watson), len(crick), spec)
            )

        if is_staggered(watson, crick):
            ## Watson and reverse Crick must not be staggered on the same side
            if watson.startswith("-") and rcrick.startswith("-"):
                raise ValueError(
                    "Please trim the staggering. Watson and Crick are both staggered at the beginning of the double-stranded sequence: '%s'"
                    % spec
                )
            if watson.endswith("-") and rcrick.endswith("-"):
                raise ValueError(
                    "Please trim the staggering. Watson and Crick are both staggered at the end of the double-stranded sequence: '%s'"
                    % spec
                )

        return "ds", spec, watson, crick

    ## "<watson>\n<rev crick>"?
    pattern = r"^([0-9A-Za-z-]+)\n([0-9A-Za-z-]+)$"
    match = re.match(pattern, spec)
    if match:
        watson = match.group(1)
        rcrick = match.group(2)
        crick = reverse(rcrick)
        if len(watson) != len(crick):
            raise ValueError(
                "Double-strand sequence string specifies two strands of different lengths (%d != %d): '%s'"
                % (len(watson), len(crick), escape_sequence_spec(spec))
            )

        if is_staggered(watson, crick):
            ## Watson and reverse Crick must not be staggered on the same side
            if watson.startswith("-") and rcrick.startswith("-"):
                raise ValueError(
                    "Please trim the staggering. Watson and Crick are both staggered at the beginning of the double-stranded sequence: '%s'"
                    % escape_sequence_spec(spec)
                )
            if watson.endswith("-") and rcrick.endswith("-"):
                raise ValueError(
                    "Please trim the staggering. Watson and Crick are both staggered at the end of the double-stranded sequence: '%s'"
                    % escape_sequence_spec(spec)
                )

        return "ds", spec, watson, crick

    raise ValueError(
        "Syntax error in sequence string: '%s'" % escape_sequence_spec(spec)
    )

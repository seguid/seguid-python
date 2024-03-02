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

from seguid.chksum import lsseguid
from seguid.chksum import csseguid
from seguid.chksum import ldseguid
from seguid.chksum import cdseguid

__all__ = ["lsseguid", "csseguid", "ldseguid", "cdseguid"]

[![Python checks](https://github.com/MetabolicEngineeringGroupCBMA/seguid/actions/workflows/check-python.yml/badge.svg)](https://github.com/MetabolicEngineeringGroupCBMA/seguid/actions/workflows/check-python.yml)
[![Python Code Coverage](https://codecov.io/gh/MetabolicEngineeringGroupCBMA/seguid/graph/badge.svg)](https://codecov.io/gh/MetabolicEngineeringGroupCBMA/seguid)
[![R checks](https://github.com/MetabolicEngineeringGroupCBMA/seguid/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/MetabolicEngineeringGroupCBMA/seguid/actions/workflows/R-CMD-check.yaml)


# SEGUID v2 checksums for single or double stranded linear or circular DNA

This package implements SEGUID v2 and the original SEGUID for legacy reasons.

SEGUID v2 consists of four separate functions (see table below). SEGUID v2 is useful for protein sequences as well as single stranded (ssDNA) and double stranded (dsDNA), either linear or circular.

|          | ssDNA     | dsDNA     |
|----------|-----------|-----------|
| linear   | lsSEGUID  | ldSEGUID  |
| circular | csSEGUID  | cdSEGUID  |


## R


## C++



## Rust



## Python

[![Documentation Status](https://readthedocs.org/projects/seguid/badge/?version=latest)](https://seguid.readthedocs.io/en/latest/?badge=latest)

Install with:

```sh
$ python -m pip install --user seguid
```

use:

```python
Python 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> from seguid import lsseguid
>>> lsseguid("AT")
'lsseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> from seguid import csseguid
>>> lsseguid("AT")
'lsseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> csseguid("AT")
'csseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> csseguid("TA")
'csseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> from seguid.reprutils import tuple_from_repr
>>> bluntdsDNAtuple = tuple_from_repr("""TA
...                                      AT""")
>>> bluntdsDNAtuple
('TA', 'TA', 0)

>>> from seguid import ldseguid
>>> ldseguid(*bluntdsDNAtuple)
'ldseguid-p_7aVtdTvX0G5N6NSDSPw0NgU6Y'
>>> stickydsDNAtuple = tuple_from_repr("""-TA
...                                       TA-""")
>>> stickydsDNAtuple
('TA', 'AT', 1)
>>> ldseguid(*stickydsDNAtuple)
'ldseguid-JwB2eUmZkCNjyWAv471JeUbiSDM'

>>> from seguid import cdseguid
>>> cdseguid("AT", "AT")
'cdseguid-AWD-dt5-TEua8RbOWfnctJIu9nA'
>>> cdseguid("TA", "TA")
'cdseguid-AWD-dt5-TEua8RbOWfnctJIu9nA'
```

Run tests with pytest without arguments in the python/ directory;

```sh
$ cd python/
$ pytest
```

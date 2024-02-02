[![Python checks](https://github.com/MetabolicEngineeringGroupCBMA/seguid/actions/workflows/check-python.yml/badge.svg)](https://github.com/MetabolicEngineeringGroupCBMA/seguid/actions/workflows/check-python.yml)
[![Python Code Coverage](https://codecov.io/gh/MetabolicEngineeringGroupCBMA/seguid/graph/badge.svg)](https://codecov.io/gh/MetabolicEngineeringGroupCBMA/seguid)
[![Documentation Status](https://readthedocs.org/projects/seguid/badge/?version=latest)](https://seguid.readthedocs.io/en/latest/?badge=latest)



# SEGUID v2: Checksums Circular, Linear, Single- and Double-Stranded Sequences

This Python package, **seguid**, implements SEGUID v2 together with
the original SEGUID algorithm.


## Example

```python
>>> from seguid import *

>>> lsseguid("AT")
'lsseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> lsseguid("AT")
'lsseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> csseguid("AT")
'csseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> csseguid("TA")
'csseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> cdseguid("AT", "AT")
'cdseguid-AWD-dt5-TEua8RbOWfnctJIu9nA'

>>> cdseguid("TA", "TA")
'cdseguid-AWD-dt5-TEua8RbOWfnctJIu9nA'
```


## Documentation

The package documentation is available on [Read the
Docs](https://seguid.readthedocs.io/en/latest/).


## Installation

The **seguid** package requires Python 3.6 or newer. To install it, use:

```sh
$ python -m pip install --user seguid
```

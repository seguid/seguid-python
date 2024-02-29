[![Python checks](https://github.com/seguid/seguid-python/actions/workflows/check-python.yml/badge.svg)](https://github.com/seguid/seguid-python/actions/workflows/check-python.yml)
[![CLI checks](https://github.com/seguid/seguid-python/actions/workflows/check-cli.yml/badge.svg)](https://github.com/seguid/seguid-python/actions/workflows/check-cli.yml)
[![Python Code Coverage](https://codecov.io/gh/seguid/seguid-python/graph/badge.svg)](https://codecov.io/gh/seguid/seguid-python)
[![Documentation Status](https://github.com/seguid/seguid-python/actions/workflows/publish-docs.yml/badge.svg)](https://github.com/seguid/seguid-python/actions/workflows/publish-docs.yml)


# SEGUID v2: Checksums for Linear, Circular, Single- and Double-Stranded Biological Sequences

This Python package, **seguid**, implements SEGUID v2 together with
the original SEGUID algorithm.


## Example

```python
>>> from seguid import *

>>> lsseguid("AT")
'lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> lsseguid("AT")
'lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> csseguid("AT")
'csseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> csseguid("TA")
'csseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'

>>> cdseguid("AT", "AT")
'cdseguid=AWD-dt5-TEua8RbOWfnctJIu9nA'

>>> cdseguid("TA", "TA")
'cdseguid=AWD-dt5-TEua8RbOWfnctJIu9nA'
```


## Documentation

The package documentation is available on <https://seguid-python.seguid.org>.


## Installation

The **seguid** package requires Python 3.6 or newer. To install it, use:

```sh
$ python -m pip install --user seguid
```


[Read the Docs]: https://seguid.readthedocs.io/en/latest/

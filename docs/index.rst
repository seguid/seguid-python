SEGUID v2: Checksums for Linear, Circular, Single- and Double-Stranded Biological Sequences
===========================================================================================

This python package, seguid, implements SEGUID v2 together with the original SEGUID algorithm.

.. image:: _static/seguid-figure.png


Single-stranded DNA examples
----------------------------
::

    import seguid

    ## Linear single-stranded DNA

    seguid.lsseguid("TATGCCAA")
    Out[2]: 'lsseguid=EevrucUNYjqlsxrTEK8JJxPYllk'

    ## Linear single-stranded DNA

    seguid.lsseguid("AATATGCC")
    Out[3]: 'lsseguid=XsJzXMxgv7sbpqIzFH9dgrHUpWw'

    ## Circular single-stranded DNA

    seguid.csseguid("TATGCCAA")
    Out[4]: 'csseguid=XsJzXMxgv7sbpqIzFH9dgrHUpWw'

    ## Same rotating two basepairs

    seguid.csseguid("GCCAATAT")
    Out[5]: 'csseguid=XsJzXMxgv7sbpqIzFH9dgrHUpWw'

Double-stranded DNA examples:
-----------------------------
::

    import seguid

    ## Linear double-stranded DNA

    seguid.ldseguid("AATATGCC", "GGCATATT")
    Out[2]: 'ldseguid=dUxN7YQyVInv3oDcvz8ByupL44A'

    ## Same swapping Watson and Crick

    seguid.ldseguid("GGCATATT", "AATATGCC")
    Out[3]: 'ldseguid=dUxN7YQyVInv3oDcvz8ByupL44A'

    ## Circular double-stranded DNA

    seguid.cdseguid("TATGCCAA", "TTGGCATA")
    Out[3]: 'cdseguid=dUxN7YQyVInv3oDcvz8ByupL44A'

    ## Same swapping Watson and Crick

    seguid.cdseguid("TTGGCATA", "TATGCCAA")
    Out[4]: 'cdseguid=dUxN7YQyVInv3oDcvz8ByupL44A'

    ## Same rotating two basepairs (= minimal rotation by Watson)

    seguid.cdseguid("AATATGCC", "GGCATATT")
    Out[5]: 'cdseguid=dUxN7YQyVInv3oDcvz8ByupL44A'

Installation
------------

The seguid package is available on PyPI and can be installed as:
::

    pip install seguid


Module contents
---------------

.. automodule:: seguid
   :members:
   :undoc-members:
   :show-inheritance:

SEGUID v2: Checksums for Linear, Circular, Single- and Double-Stranded Biological Sequences
===========================================================================================

Functions for calculating sequence checksums for linear, circular, single- and double-stranded
sequences based on either the original SEGUID (SEGUID v1) algorithm (Babnigg & Giometti, 2006)
or the SEGUID v2 algorithm (Pereira et al., 2024).


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

Double-stranded DNA examples
----------------------------
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


References
----------

Pereira, Humberto, Paulo César Silva, Wayne M Davis, Louis Abraham, Gyorgy Babnigg, Henrik Bengtsson,
and Bjorn Johansson. SEGUID v2: Extending SEGUID Checksums for Circular, Linear, Single- and Double-Stranded
Biological Sequences. bioRxiv (2024). https://doi.org/10.1101/2024.02.28.582384

Babnigg, György, and Carol S Giometti. A database of unique protein sequence identifiers for proteome
studies. Proteomics (2006) 6 (16): 4514–22. https://doi.org/10.1002/pmic.200600032


Module contents
---------------

.. automodule:: seguid
   :members:
   :undoc-members:
   :show-inheritance:

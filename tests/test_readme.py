"""
Python 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from seguid import slseguid
>>> slseguid("AT")
'slseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> from seguid import scseguid
>>> slseguid("AT")
'slseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> scseguid("AT")
'scseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> scseguid("TA")
'scseguid-Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> from seguid.reprutils import tuple_from_repr
>>> bluntdsDNAtuple = tuple_from_repr(\"""TA
...                                       AT\""")
>>> bluntdsDNAtuple
('TA', 'TA', 0)
>>> from seguid import dlseguid
>>> dlseguid(*bluntdsDNAtuple)
'dlseguid-p_7aVtdTvX0G5N6NSDSPw0NgU6Y'
>>> stickydsDNAtuple = tuple_from_repr(\"""-TA
...                                        TA-\""")
>>> stickydsDNAtuple
('TA', 'AT', 1)
>>> dlseguid(*stickydsDNAtuple)
'dlseguid-JwB2eUmZkCNjyWAv471JeUbiSDM'
>>> from seguid import dcseguid
>>> dcseguid("AT", "AT")
'dcseguid-AWD-dt5-TEua8RbOWfnctJIu9nA'
>>> dcseguid("TA", "TA")
'dcseguid-AWD-dt5-TEua8RbOWfnctJIu9nA'
"""

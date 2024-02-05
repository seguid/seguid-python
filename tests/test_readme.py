"""
Python 3.11.3 | packaged by conda-forge | (main, Apr  6 2023, 08:57:19) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from seguid import lsseguid
>>> lsseguid("AT")
'lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> from seguid import csseguid
>>> lsseguid("AT")
'lsseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> csseguid("AT")
'csseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> csseguid("TA")
'csseguid=Ax_RG6hzSrMEEWoCO1IWMGska-4'
>>> from seguid.reprutils import tuple_from_repr
>>> bluntdsDNAtuple = tuple_from_repr(\"""TA
...                                       AT\""")
>>> bluntdsDNAtuple
('TA', 'TA', 0)
>>> from seguid import ldseguid
>>> ldseguid(*bluntdsDNAtuple)
'ldseguid=p_7aVtdTvX0G5N6NSDSPw0NgU6Y'
>>> stickydsDNAtuple = tuple_from_repr(\"""-TA
...                                        TA-\""")
>>> stickydsDNAtuple
('TA', 'AT', 1)
>>> ldseguid(*stickydsDNAtuple)
'ldseguid=JwB2eUmZkCNjyWAv471JeUbiSDM'
>>> from seguid import cdseguid
>>> cdseguid("AT", "AT")
'cdseguid=AWD-dt5-TEua8RbOWfnctJIu9nA'
>>> cdseguid("TA", "TA")
'cdseguid=AWD-dt5-TEua8RbOWfnctJIu9nA'
"""

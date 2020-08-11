# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:41:51 2020

@author: wxy
"""

import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session

import os
import sys
sys.path.append(os.path.abspath("/Users/ananyakondiparthy/lam/flaskr"))
import sys
from Dataframe import dfTotal
from Dataframe import dfSilfex


import pandas as pd
import numpy as np
from datetime import datetime

# Formatting the Install Base Data.

dfTotal.columns=['ShipDate','ShipTo','SuperiorSerial','Serial','ProductGroup','Product','Technology','System','WarrantyEnd','WarrantyStatus','Qty']
dfTotal['ShipDate']=pd.to_datetime(dfTotal.ShipDate)

# Formatting SilfexTBbyShipTo csv file

dfSilfex.columns=['ShipDate','ShipTo','Region','Serial','SuperiorSerial','System','Material','Qty']
dfSilfex['ShipDate']=pd.to_datetime(dfSilfex.ShipDate)
dfTransport = dfSilfex[dfSilfex.System.apply(lambda x: 'TRANSPORT' in str(x))]
dfMerge=dfTransport.merge(dfTotal,left_on=['ShipDate','ShipTo','Serial'],right_on=['ShipDate','ShipTo','SuperiorSerial'])
dfMerge.drop(['SuperiorSerial_x','System_x','Serial_x','Qty_x'],axis=1,inplace=True)
dfMerge.rename(columns={'SuperiorSerial_y':'SuperiorSerial','Serial_y':'Serial','System_y':'System','Qty_y':'Qty'},inplace=True)
dfSilfexNorm=dfSilfex[dfSilfex.System.apply(lambda x: 'TRANSPORT' not in str(x))]
#dfSilfexNorm=dfSilfexNorm[dfSil]
df=dfMerge[['ShipDate','ShipTo','Region','Serial','SuperiorSerial','System','Material','Qty']]
df1=[dfSilfexNorm,df]
df2=pd.concat(df1)
df2.dropna(axis=0,subset=['System'])
dfInstallBase = df2
print(dfInstallBase)


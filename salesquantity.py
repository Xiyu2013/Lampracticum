# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:11:40 2020

@author: wxy
"""
import sys
import pandas as pd
import functools
import numpy as np
from datetime import datetime, timedelta
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from flask import Blueprint
from pandas.core.frame import DataFrame
import Dataframe
import os
sys.path.append(os.path.abspath("/Users/ananyakondiparthy/lam/flaskr"))

from Dataframe import dfOrder
from modeling.scikit_learn.installbase  import dfInstallBase
from modeling.scikit_learn.installbase  import dfDate

#dfInstallBase.drop([': 0'],axis=1,inplace=True)

# Chambers need time to become active installbase


#
# class InstallBase:
#
#     def ExtractQuarter(self,month,df):
#         self.df['Quarter'] = self.df['Month'].apply(lambda x: 'Q1' if (x==1 or x==2 or x==3) \
#                                                         else 'Q2' if (x==4 or x==5 or x==6) \
#                                                         else 'Q3' if (x==7 or x==8 or x==9) \
#                                                         else 'Q4')
#         return df['Quarter']
#
#
#     def ExtractMonth(self,df):
#




dfInstallBase['ShipDate']=pd.to_datetime(dfInstallBase['ShipDate'])
dfInstallBase['Year']=dfInstallBase['ShipDate'].dt.year
dfInstallBase['Month']=dfInstallBase['ShipDate'].dt.month
dfInstallBase['Quarter']=dfInstallBase['Month'].apply(lambda x: 'Q1' if (x==1 or x==2 or x==3) \
                                                        else 'Q2' if (x==4 or x==5 or x==6) \
                                                        else 'Q3' if (x==7 or x==8 or x==9) \
                                                        else 'Q4')
ShipTo= [4206,1341,2658]
Material= ['716-443086-401']
df=dfInstallBase.loc[dfInstallBase['ShipTo'].isin(ShipTo) & dfInstallBase['Material'].isin(Material)]
dfInstallBaseQty=df.groupby(['Year','Quarter'])['Qty'].sum().reset_index()
dfInstallBaseQty['Quarter']=dfInstallBaseQty.Year.map(str)+dfInstallBaseQty.Quarter
dfInstallBaseQty=dfInstallBaseQty.sort_values(by='Quarter')
dfInstallBaseQty['sumQty']=dfInstallBaseQty.Qty.cumsum()
dfOrder.columns=['SalesOrderDate','ShipTo','OrderType','Material','Qty']
dfOrder.SalesOrderDate=pd.to_datetime(dfOrder.SalesOrderDate)
ShipTo= ['4206','1341','2658']
dfSales=dfOrder.loc[dfOrder['ShipTo'].isin(ShipTo) & dfOrder['Material'].isin(Material)].copy()
dfSales['Year']=dfSales['SalesOrderDate'].dt.year
dfSales['Month']=dfSales['SalesOrderDate'].dt.month
dfSales['Quarter']=dfSales['Month'].apply(lambda x: 'Q1' if (x==1 or x==2 or x==3) \
                                               else 'Q2' if (x==4 or x==5 or x==6) \
                                               else 'Q3' if (x==7 or x==8 or x==9) \
                                               else 'Q4')
dfSalesQty=dfSales.groupby(['Year','Quarter'])['Qty'].sum().reset_index()
dfSalesQty['Quarter']=dfSalesQty.Year.map(str)+dfSalesQty.Quarter
dfGeneral=dfSalesQty.merge(dfInstallBaseQty,how='left',on='Quarter')
dfGeneral.drop(['Year_y'],axis=1,inplace=True)
dfGeneral.columns=['Year','Quarter','SalesQty','InstallBaseQty','sumQty']
dfDate=dfDate[(dfDate.Quarter>=dfGeneral.iloc[0,1]) & (dfDate.Quarter<=dfGeneral.iloc[-1,1])]
dfGeneral=dfDate.merge(dfGeneral,how='left',on='Quarter')
dfGeneral['sumQty']=dfGeneral.sumQty.fillna(method='ffill')
dfGeneral['SalesQty']=dfGeneral.SalesQty.fillna(value=0)
dfGeneral['InstallBaseQty']=dfGeneral.InstallBaseQty.fillna(value=0)
dfGeneral

# import glob
#
# import quandl
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import sklearn as sk
# import sklearn.tree as tree
# # import pydotplus
# import re
# from numpy import exp, cos, linspace
# import matplotlib.pyplot as plt
# import os, time, glob
# from datetime import datetime
# from datetime import timedelta
# import os
# import sys
#
# sys.path.append(os.path.abspath("/Users/ananyakondiparthy/lam/flaskr"))
# from Dataframe import dfshipto, dfChina
#
# # import warnings
# dfshipto.columns = ['Shipdate', 'Company', 'Shipto', 'Group', 'System', 'Product', 'Plant', 'Warranty_Status',
#                     'Warranty_End', 'Chambers']
# dfshipto.Shipdate = pd.to_datetime(dfshipto.Shipdate)
# dfshipto.Warranty_End = pd.to_datetime(dfshipto.Warranty_End, errors='coerce')
# dfshipto['Quarter'] = pd.to_datetime(dfshipto['Shipdate']).dt.to_period('Q')
# # china
# dfChina.columns = ['Calendar_Q', 'Customer', 'Shipto', 'BillingDate', 'DeliveryNo', 'PGI_Date', 'SalesNo', 'PO_Date',
#                    'DocCreationDate', 'Req_Date', 'Material', 'Description', 'Revenue', 'Qty']
# # Handling all the dates
# dfChina.BillingDate = dfChina.BillingDate.apply(lambda x: x[6:10] + '-' + x[3:5] + '-' + x[0:2])
# dfChina.BillingDate = dfChina.BillingDate.apply(lambda x: 'NaT' if x.startswith('-') else pd.to_datetime(x))
# dfChina.PGI_Date = pd.to_datetime(dfChina.PGI_Date, errors='coerce')
# dfChina.PO_Date = pd.to_datetime(dfChina.PGI_Date, errors='coerce')
# dfChina.DocCreationDate = pd.to_datetime(dfChina.DocCreationDate, errors='coerce')
# dfChina.Req_Date = pd.to_datetime(dfChina.Req_Date, errors='coerce')
# dfChina.Revenue = dfChina.Revenue.str.replace(',', '').str.replace('$', '').astype(int)
# dfChina.Qty = dfChina.Qty.str.replace(',', '').astype(int)
# dfChina['Quarter'] = dfChina.Calendar_Q.apply(lambda x: '20' + x[5:7] + x[1:4])
# dfChina['Quarter'] = dfChina.Quarter.apply(lambda x: x.replace('Mar', 'Q1'))
# dfChina['Quarter'] = dfChina.Quarter.apply(lambda x: x.replace('Jun', 'Q2'))
# dfChina['Quarter'] = dfChina.Quarter.apply(lambda x: x.replace('Sep', 'Q3'))
# dfChina['Quarter'] = dfChina.Quarter.apply(lambda x: x.replace('Dec', 'Q4'))
# df_14 = dfChina[dfChina.Customer == 'COMPANY 14']
# df_28 = dfChina[dfChina.Customer == 'COMPANY 28']
# df_shipto_14 = dfshipto[dfshipto.Company == 'COMPANY 14']
# df_shipto_28 = dfshipto[dfshipto.Company == 'COMPANY 28']
#
#
# def compute(Material):
#     # "Return Materials"
#     plot1 = df_14[df_14.Material == str(Material)].groupby('Quarter').Qty.sum()
#     plt.figure()
#     plt.plot(plot1)
#     plt.title("Materials Analysis")
#
#     if not os.path.isdir('static'):
#         os.mkdir('static')
#     else:
#         for filename in glob.glob(os.path.join('static', '*.png')):
#             os.remove(filename)
#     # Use time since Jan 1, 1970 in filename in order make
#     # a unique filename that the browser has not chached
#     plotfile = os.path.join('static', str(time.time()) + '.png')
#     plt.savefig(plotfile)
#     return plotfile
#
#
# if __name__ == '__main__':
#     print (compute("1"))

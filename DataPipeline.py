import csv
import os
import pandas as pd
import numpy as np
import sys
inFile = sys.argv[1]

class DataPipeline(object):


    def __init__(self):
        self.merged = False
        self.num_flag = False


    def extractdata(self):
        self.df1 = pd.read_csv(inFile, sep=',')
        #csv_reader = csv.reader(inFile, delimiter=',')
        with open(inFile,'r') as i:
             lines = i.readlines()
        processedLines = self.ManipulateData(lines)
        return self.processedLines

    def Merge2data(self):
        a = pd.read_csv("SCU-TotalIBbyShipTo.csv")
        b = pd.read_csv("SCU-SilfexIBbyShipTov2.csv")
        b = b.dropna(axis=1)
        merged = a.merge(b, on='Ship To')
        return self.merged


    def Manipulatedata(self):



        self.new_df = self.df1['Ship Date','Ship To','Superior Serial','Serial','QuantityShip']]



    def filter(self, df):
        df1 = df.filter(['System'])

    def has_column(self) : --> bool
















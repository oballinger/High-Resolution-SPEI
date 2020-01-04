import os
import glob
import csv
import numpy as np
import pandas as pd
from pathlib import Path
import re


## Define a function to convert epoch time output into year and month
def monthly(f):
      baseyear=1985
      basemonth=0
      newmonth=basemonth+f
      newyear=baseyear+int(newmonth/12)
      if newmonth>12:
           month=newmonth%12
      else:
           month=newmonth
      if newmonth%12==0:
           newyear=newyear-1
           month=12
      else:
           pass
      return(str(newyear)+"-"+str(month))


## Input path to R output 
folder="/Users/ollie/Google Drive/"
path=str(Path(folder+"*_month_*"))
files=glob.glob(path)


## Add a date column and convert to panel format
for f in files:
      df=pd.read_csv(f, header=None,dtype=object)
      filename= os.path.basename(f)
      df=df.reset_index()
      for a in range(len(df)-1):
            df.loc[[a],0]=df.loc[[a],0].fillna("cell")
            inp=int(df.loc[[a+1],0])
            df.loc[[a+1],0]=monthly(inp)
      df=df.T
      df=df.reset_index()
      df.columns=df.iloc[1]
      df=df.iloc[3:]
      df.to_csv(filename+".csv")
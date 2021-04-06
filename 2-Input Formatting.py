
## Format data 
import csv
import pandas as pd
from pathlib import Path

## Input the total number of months in your timeframe and the path to the files from step 1.
months=398
path="/Users/ollie/Google Drive/"
df=pd.read_csv(path+"Grid_10km_Mean_WaterBalance.csv"), header=None)

## Clean column names 
df.iloc[0]=df.iloc[0].str.split('_').str[0]
df.iloc[0]=(df.iloc[0].str[:4])+"_"+(df.iloc[0].str[4:])
df.columns=df.iloc[0]
df=df.iloc[1:]

## Transpose data 
df=df.T.reset_index()
df.columns=df.loc[months]
df=df.iloc[1:]
df=df.iloc[:months-1]

## Export to CSV
df.to_csv("SPEI_Input10k.csv")


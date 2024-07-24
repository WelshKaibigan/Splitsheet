import pandas as pd
import sys
import os
import pathlib
import contextlib

filename = sys.argv[1]
filetype = pathlib.Path(filename).suffix
print(filetype)
if filetype == ".xlsx":
    mydata = pd.read_excel(filename)
elif filetype == ".csv":
    mydata = pd.read_csv(filename)

df1 = pd.DataFrame()
numcols = len(mydata.columns)   

colnum=0
with contextlib.redirect_stderr(None):
    for y in range(numcols):
        for column in mydata.columns[colnum:colnum+3]:
            df1 = mydata.iloc[:,colnum:colnum+3].copy()
            df1.drop(labels=[0], inplace=True, axis=0)
            df1.to_csv(column +".csv",",",index=False, header=False)
            df1.drop(df1.index, inplace=True)
        colnum=colnum+4

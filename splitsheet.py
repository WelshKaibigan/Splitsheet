import pandas as pd
import sys
import os
import pathlib
import contextlib

if len(sys.argv) < 2:
    print("Usage: python splitsheet.py <filename>")
    sys.exit(1)
else:
    filename = sys.argv[1]

filetype = pathlib.Path(filename).suffix
print(filetype)
if filetype == ".xlsx":
    mydata = pd.read_excel(filename)
elif filetype == ".csv":
    mydata = pd.read_csv(filename)

df1 = pd.DataFrame()

numcols = len(mydata.columns)   

# Find the columns where each value is null
empty_cols = [col for col in mydata.columns if mydata[col].isnull().all()]

# Drop these columns from the dataframe
mydata.drop(empty_cols,
        axis=1,
        inplace=True)


colnum=0
with contextlib.redirect_stderr(None):
    for y in range(numcols):
        for column in mydata.columns[colnum:colnum+3]:
            df1 = mydata.iloc[:,colnum:colnum+3].copy()
            df1.drop(labels=[0], inplace=True, axis=0)
            df1.to_csv(column +".csv",",",index=False, header=False)
            df1.drop(df1.index, inplace=True)
        colnum=colnum+3

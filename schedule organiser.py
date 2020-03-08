# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:55:13 2019

@author: MUDIT
"""

import pandas as pd
import numpy as np
from tkinter import Tk
from tkinter import filedialog

root=Tk()
root.file = filedialog.askopenfilename(filetypes = ( ("spreadsheet", ".xls"),("all files","*.*")))
#file = 'Downloads/Registration Data- Sem I 19-20(9.8.19).xls'
df = pd.read_excel(root.file, index = False)
print(df)
 
arr = df.as_matrix()

n=arr.shape[0]
# =============================================================================
# for i in range(1,n):
# 	arr[i,7]=str(arr[i,7])[2:]
# =============================================================================
for i in range(1,n):
    if ((i<n-1) and arr[i,2]==arr[i+1,2]):
        if ((arr[i,7]==arr[i+1,7]) and arr[i,7]!=0):
            arr[i+1,7]=0
    if ((i<n-2) and arr[i,2]==arr[i+2,2]):
        if ((arr[i,7]==arr[i+2,7]) and arr[i,7]!=0):
            arr[i+2,7]=0
         
x=arr

df2=pd.DataFrame.from_records(arr)
df3 = df2.drop(df2.columns[[0,1,3,5,6,8,9,10,11,12,13,14]], axis = 1)

x=df3.as_matrix()

temp = np.arange(0,x.shape[0]).reshape([x.shape[0],1])

x=np.hstack((temp,x))
x[0,0] = "id"
df3=pd.DataFrame(x)
df3 = df3.replace({pd.np.nan: None})
root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))

#writer = pd.ExcelWriter(root.filename, engine='xlsxwriter')
df3.to_csv(root.filename, index=False, header=False)
#writer.save() 
root.destroy()

# =============================================================================
# output_file=root.file
# output_file = PureWindowsPath(output_file)
# 
# =============================================================================


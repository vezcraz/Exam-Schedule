import pandas as pd 
import numpy as np
import math as mt
from tkinter import Tk
from tkinter import filedialog
from pathlib import Path, PureWindowsPath
root=Tk()
root.file = filedialog.askopenfilename(filetypes = ( ("spreadsheet", ".xls*"),("all files","*.*")))
#file = 'Downloads/Registration Data- Sem I 19-20(9.8.19).xls'
df = pd.read_excel(root.file, index=False)
df = df.replace({pd.np.nan: None})
df.astype(str)
arr = df.as_matrix()
arr[951,0][:4]

n = df.shape[0]
c1=0
c2=0

for i in range(n):
    if(isinstance(arr[i,0],str)):
        if(arr[i,0][:4]=="EXAM"):
            print(arr[i,0][:4])
            c1=i+1
           
        
        if(arr[i,0][:4]=="TEXT"):
            c2=i
        
print(c1,c2)
list=[]
for i in range(c1,c2):
    if(not isinstance(arr[i,0],str)):
        list.append(arr[i])
        
ar=np.asarray(list)
 
df2=pd.DataFrame(ar)
    
list=[4,9,25,32,39]

x= np.ones([ar.shape[0],1])
x= ar[:,0].reshape([ar.shape[0],1]).astype(str)

for i in range(5):
    x=np.hstack((x,ar[:,list[i]].reshape([ar.shape[0],1])))



df3=pd.DataFrame(x)

x= df3.as_matrix()


x[:,0] = '0' + x[:,0]
b = x=="TBA"
c = x=="0nan"
d = x=="TO BE ANNOUNCED BY IC"

x[b]=None
x[c]=None
x[d]=None
df3=pd.DataFrame(x)

temp = np.arange(1,x.shape[0]+1).reshape([x.shape[0],1])

x=np.hstack((temp,x))


#np.insert(x,4,np.ones([x.shape[0],1]),axis=1)
#df4=pd.DataFrame(x)
x=np.hstack((x,temp))
for i in range(x.shape[0]):
    if(isinstance(x[i,4],str) and x[i,4]!=None):
        
        x[i,7] = x[i,4][-4:]
        x[i,4] = x[i,4][:8]
    
    if(isinstance(x[i,7], int)):
        x[i,7]=None;
    
    if(x[i,7]=="(FN)"):
        x[i,7] = "09:00 AM - 12:00 PM"
    
    if(x[i,7]=="(AN)"):
        x[i,7] = "02:00 PM - 05:00 PM"
    
    

for i in range(x.shape[0]):
    if(isinstance(x[i,4],str)):
        x[i,4] = x[i,4][:8]
    if(isinstance(x[i,5],str)):
        x[i,5] = x[i,5][:8]

df3=pd.DataFrame(x)
df = df3


df.columns = ["id", "cid", "courseno", "title", "cd", "md", "mt", "ct"]
df = df[["id", "cid", "courseno", "title",  "md", "mt", "cd", "ct"]]
df['md'] =  pd.to_datetime(df['md'],
                              format='%d/%m/%y')
df['cd'] =  pd.to_datetime(df['cd'],
                              format='%d/%m/%y')
root.filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))

#writer = pd.ExcelWriter(root.filename, engine='xlsxwriter')
df.to_csv(root.filename, index=False, header=True)
#writer.save() 
root.destroy()
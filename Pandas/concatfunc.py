import pandas as pd 
data1={'Name':['nadeem','ashraf','hussain','manzor','ali','rozi'],
       'Age ':[60,80,70,90,50,100],
       'Address':['kharmang','khapolo','shigar','skardu','gilgit','hunza'],
       'qualification':['bscs','ms','m.phil','bsmath','phd','mca'].upper()}
data2={'Name':['nadee','ashra','hussai','manzo','alii','rozii'],
       'Age ':[62,83,74,95,56,99],
       'Address':['kharmang','khapolo','shigar','skardu','gilgit','hunza'],
       'qualification':['bscs','ms','m.phil','bsmath','phd','mca'].upper()}
df=pd.DataFrame(data1,index=[0,1,2,3])
df1=pd.DataFrame(data2,index=[0,1,2,3])
print(df,"\n",df1)
frame=[df,df1]
res=pd.concat([df,df1],axis=1,join='inner')
print(res)
res1=pd.concat([df,df1],axis=1,sort=False)
print(res1)
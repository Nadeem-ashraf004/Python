import pandas as pd
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
dict={'name':nme,'degree':deg,'score':scr}
df=DataFram(dict)
df.to_csv('file1.csv')
df.to_csv('file1.csv',header=False,index=False)
df.to_csv("your_name.csv", na_rep = 'nothing')
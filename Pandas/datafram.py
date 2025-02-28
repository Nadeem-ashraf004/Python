import pandas as pd
lst=['nadeem','gulzar','hameed']
pt=pd.DataFrame(lst)
print(pt)
################
lst1={'name':['nadeem','gulzar','hameed'],'age':[22,20,21]}
p=pd.DataFrame(lst1)
print(p)
##################
dict={'name':["aparna", "pankaj", "sudhir", "Geeku"],'degree': ["MBA", "BCA", "M.Tech", "MBA"],'score':[90, 40, 80, 98]}
data=pd.DataFrame(dict)
print(data)
#################
lst2=[]
pf=pd.DataFrame(lst2)
print(pf)
######################
data = [{'a': 1, 'b': 2, 'c': 3},{'a': 10, 'b': 20, 'c': 30}]
df=pd.DataFrame(data)
print(df)
###############
data={'Name':['nadeem','ashraf','hussain','haider'],'Marks':[99, 98, 95, 90]}
df=pd.DataFrame(data,index=['ranaked1','ranked2','ranked3','ranked4'])
print(df)

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
###########################
dic={'first':[12,np.nan,23,24,25,26,27],'second':[13,12,14,15,16,17,np.nan],'third':[np.nan,34,35,36,37,38,39]}
df=pd.DataFrame(dic)
pd.isnull()
#########################
Data=['New York', 'Chicago', 'Toronto', 'Lisbon']
index_name=[1,2,3,4]
sr=pd.Series(data=Data,
            index=index_name)
print(sr)
print(sr.index)
#########################
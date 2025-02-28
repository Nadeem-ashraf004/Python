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
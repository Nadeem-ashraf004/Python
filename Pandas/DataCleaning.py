import numpy as np
import pandas as pd
data = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df=pd.DataFrame(data)
missing_values=df.isnull()
print("missing values from the dataset !\n",missing_values)
missing_values=df.notnull()
print(missing_values)
########################################
data = pd.read_csv("C:\\Users\\nadeem\\Downloads\\employees.csv")
print(data)
# print(data)
missing_values=pd.isnull(data["Gender"])
print(missing_values)
non_missing_values=data[missing_values]
print(non_missing_values)
data["Gender"].fillna('No Gender',inplace=True)
data[10:25]
data.replace(to_replace=np.nan,value=-99)
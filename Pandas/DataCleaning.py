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
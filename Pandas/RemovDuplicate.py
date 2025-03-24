import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}
df=pd.DataFrame(data)
unique_df=df.drop_duplicates(subset=['Name'])
print(unique_df)
############## converting datatype 
data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}
df=pd.DataFrame(data)
df=df.astype({'Age':'float64','Salary':'str'})
print(df.dtypes)
#####
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40],
    "City": ["NY", "LA", "NY", "Chicago"]
}
df=pd.DataFrame(data)
unique_df=df.drop_duplicates(subset=['Name'])
print(unique_df)
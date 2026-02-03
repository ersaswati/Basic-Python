import pandas as pd
import numpy as np

data = {
    "name": ["Alice", "Bob", None],
    "age": [25, np.nan, 35],
    "salary": [50000, 60000, None]
}

df = pd.DataFrame(data)

print(df.isnull().sum())
df.fillna(0, inplace=True)

df = pd.DataFrame({"A": [1, 1, 2, 3]})
df = df.drop_duplicates()
print(df)

df = pd.DataFrame({"price": ["10", "20", "30"]})
df["price"] = df["price"].astype(int)
print(df.dtypes)
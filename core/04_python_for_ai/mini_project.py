import pandas as pd
import numpy as np

data = {
    "age": [25, 30, 35, np.nan],
    "salary": [50000, 60000, np.nan, 80000]
}

df = pd.DataFrame(data)

df.fillna(df.mean(), inplace=True)

df["salary_scaled"] = (df["salary"] - df["salary"].mean()) / df["salary"].std()

print(df)
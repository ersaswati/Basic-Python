import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [25, 30, 35, 40],
    "salary": [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

print(df)
print(df[df["age"] > 30])
print(df[["name", "salary"]])

df["bonus"] = df["salary"] * 0.1
df["department"] = ["HR", "IT", "IT", "HR"]

print(df.groupby("department")["salary"].mean())
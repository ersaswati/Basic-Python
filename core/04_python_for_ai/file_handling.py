import pandas as pd
import json

df = pd.DataFrame({"A": [1, 2, 3]})
df.to_csv("test.csv", index=False)

new_df = pd.read_csv("test.csv")
print(new_df)

data = {"name": "Alice", "age": 25}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    loaded = json.load(f)

print(loaded)
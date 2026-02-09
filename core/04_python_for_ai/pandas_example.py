import pandas as pd
import numpy as np

# ============================================================
'''
TOPIC 1: DATAFRAME CREATION
SUBTOPICS: dictionary, list, numpy array
INPUT: Raw data
OUTPUT: Structured DataFrame

EXPECTED OUTPUT:
   Name  Age  Score
0  A     25   85
1  B     30   90
2  C     22   78
'''
print("TOPIC 1: DATAFRAME CREATION")

data = {
    "Name": ["A", "B", "C"],
    "Age": [25, 30, 22],
    "Score": [85, 90, 78]
}
df = pd.DataFrame(data)
print(df)
print("="*60)


# ============================================================
'''
TOPIC 2: DATA INSPECTION
SUBTOPICS: head, info, describe, shape
INPUT: DataFrame
OUTPUT: Summary of dataset

EXPECTED OUTPUT:
Shape: (3,3)
Head: first rows
Info: column types
Describe: stats of numeric columns
'''
print("TOPIC 2: DATA INSPECTION")

print("Shape:", df.shape)
print("Head:\n", df.head())
print("Info:")
print(df.info())
print("Describe:\n", df.describe())
print("="*60)


# ============================================================
'''
TOPIC 3: COLUMN SELECTION & FILTERING
SUBTOPICS: single column, multiple columns, condition
INPUT: DataFrame
OUTPUT: Filtered data

EXPECTED OUTPUT:
Scores column
Rows where Score > 80
'''
print("TOPIC 3: SELECTION & FILTERING")

print("Scores Column:\n", df["Score"])
print("Score > 80:\n", df[df["Score"] > 80])
print("="*60)


# ============================================================
'''
TOPIC 4: ADDING & MODIFYING COLUMNS
SUBTOPICS: new column, transformation
INPUT: DataFrame
OUTPUT: Updated DataFrame

EXPECTED OUTPUT:
New column 'Passed'
'''
print("TOPIC 4: MODIFYING COLUMNS")

df["Passed"] = df["Score"] > 80
print(df)
print("="*60)


# ============================================================
'''
TOPIC 5: GROUPBY (CORE ANALYTICS)
SUBTOPICS: aggregation
INPUT: DataFrame
OUTPUT: Grouped summary

EXPECTED OUTPUT:
Average score per Passed category
'''
print("TOPIC 5: GROUPBY")

print(df.groupby("Passed")["Score"].mean())
print("="*60)


# ============================================================
'''
TOPIC 6: HANDLING MISSING VALUES
SUBTOPICS: isnull, fillna, dropna
INPUT: DataFrame with NaN
OUTPUT: Cleaned data

EXPECTED OUTPUT:
Filled missing Age with mean
'''
print("TOPIC 6: MISSING VALUES")

df2 = df.copy()
df2.loc[1, "Age"] = np.nan
print("Before Fill:\n", df2)

df2["Age"].fillna(df2["Age"].mean(), inplace=True)
print("After Fill:\n", df2)
print("="*60)


# ============================================================
'''
TOPIC 7: SORTING & APPLY
SUBTOPICS: sort_values, apply function
INPUT: DataFrame
OUTPUT: Sorted and transformed data

EXPECTED OUTPUT:
Sorted by Score
New Grade column
'''
print("TOPIC 7: SORTING & APPLY")

df_sorted = df.sort_values("Score", ascending=False)
print("Sorted:\n", df_sorted)

df["Grade"] = df["Score"].apply(lambda x: "A" if x > 85 else "B")
print("With Grade:\n", df)
print("="*60)

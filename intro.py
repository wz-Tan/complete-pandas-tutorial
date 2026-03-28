import pandas as pd

# Shift control enter to run jupyter notebook
df = pd.DataFrame([[1, 2], [1, 2]], columns=["A", "B"], index=["X", "Y"])

# Print first row or last 2 rows
print(df.head(1))
print(df.tail(2))

# Some Additional Info
print(df)
print(df.info())
print(df.describe())

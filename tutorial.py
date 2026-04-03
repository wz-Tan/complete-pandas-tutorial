import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")
olympic = pd.read_parquet("./data/results.parquet")

# Generate Some Data
# coffee.sample(10)

# Acquiring Rows (Can Do coffee.loc[[0,1,2]] for The first 3 rows) and Second Parameter for Column (Use Key in Loc and Index for Iloc)
coffee.loc[0, "Day"]
coffee.iloc[0, [0, 1]]

# Faster than loc, but usually for single values
coffee.at[0, "Day"]

# Reassign Index / Primary Key with a Specific Column
coffee.index = coffee["Day"]
coffee.loc["Monday"]

coffee.sort_values(["Units Sold"])
print(coffee)

# Iterate through rows
for row, value in coffee.iterrows():
    print(value)

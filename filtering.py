import pandas as pd

bios = pd.read_excel("./data/olympics-data.xlsx")
bios.head()

# Get Height of Athletes >= 200cm, Show Name
bios[bios["height_cm"] >= 200]["name"]

# Multiple Conditions, Born in USA and City is New Jersey
bios[(bios["born_country"] == "USA") & (bios["born_region"] == "New Jersey")]

# Alternative Way To Query
bios.query("born_country == 'USA' and born_region == 'New Jersey' ")

# Find Shaq or Kobe (We can also use RegEx within the strings)
bios[bios["name"].str.contains("Shaq|Kobe Bryant")]

# Use .isin for Multiple Conditions Under the Same Category (Instead of Multiple AND statements)
bios[bios["born_country"].isin(["MAS", "SGP"])]

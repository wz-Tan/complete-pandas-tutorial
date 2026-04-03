import numpy as np
import pandas as pd

# Extracting Data Out Of CSV Files

# Olympics Database
bios = pd.read_csv("./data/bios.csv")

# Short Form to Full Form of the Country
nocs = pd.read_csv("./data/noc_regions.csv")

# Select Datasets, Inner Join on Born Country for Bios and NOC on NOCS
merged_data = pd.merge(bios, nocs, left_on="born_country", right_on="NOC", how="inner")
merged_data.head()

# Renaming Columns
merged_data.rename(columns={"NOC_x": "born_country_full"}, inplace=True)
merged_data[["born_country_full", "born_country"]]

# Getting Players from USA and Britain
usa = bios[bios["born_country"] == "USA"]
gbr = bios[bios["born_country"] == "GBR"]

# Combine Them
usa_gbr = pd.concat([usa, gbr])
usa_gbr

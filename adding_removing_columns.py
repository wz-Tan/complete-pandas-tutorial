import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")

# Add In Column
coffee["brewer"] = "John Kaisen"

import numpy as np

# Set The Brewer Based Off Coffee Type (John Kaisen for Espresso and James Kaisen For Others)
coffee["brewer"] = np.where(
    coffee["Coffee Type"] == "Espresso", "John Kaisen", "James Kaisen"
)

# Deleting A Column (The Original Remains Untouched) - Add inPlace = True tag after columns for it to be permanent
coffee_without_price = coffee.drop(columns=["Units Sold"])

coffee["revenue"] = "One bazillion dollars"

# Renaming a Column via Dictionary
coffee.rename(columns={"brewer": "sigma"}, inplace=True)

# Applying Lambdas to A New Category (Alternative for Numpy Where)
coffee["sales_category"] = coffee["Units Sold"].apply(
    lambda x: "Good" if x >= 20 else "Bad"
)

import numpy as np
import pandas as pd

coffee = pd.read_csv("./warmup-data/coffee.csv")

# Set Items Sold on Mondays and Sundays to Be NaN
coffee.loc[(coffee["Day"] == "Sunday") | (coffee["Day"] == "Monday"), "Units Sold"] = (
    np.nan
)

# Drop All Na
# coffee.dropna()

# Replace NaNs with Funny Number 67
coffee.fillna(67, inplace=True)
coffee

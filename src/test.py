import matplotlib as plt
import pandas as pd

data = pd.read_csv("../data/properties_2016_raw.csv")

print(data.columns)

cols = ["longitue", "latitude"]
geo_data = data[cols]

print(geo_data)

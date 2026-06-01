import matplotlib as plt
import pandas as pd
import pathlib as path

parent_dir = path.Path(__file__).resolve().parents[1]
data = pd.read_csv(parent_dir / "data/properties_2016_raw.csv")

print(data.columns)

cols = ["longitue", "latitude"]
geo_data = data[cols]

print(geo_data)

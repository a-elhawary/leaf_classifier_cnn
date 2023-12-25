import os
import pandas as pd

data = pd.read_csv("train.csv")

os.mkdir("data")

folders = []
for record, species in zip(data["id"], data["species"]):
    path = f"images/{record}.jpg" 
    if species not in folders:
        os.mkdir(f"data/{species}")
        folders.append(species)
    to = f"data/{species}/{record}.jpg"
    os.rename(path, to)
    
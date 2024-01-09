# Writing to csv file

import csv
import pandas as pd

data = {"Name": ["Aman", "Diksha", "Akanksha", "Sai", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}

data = pd.DataFrame(data)
print(data)
data.to_csv("age_data.csv", index=False)

# reading the csv file

data = pd.read_csv("age_data.csv")

print(data)
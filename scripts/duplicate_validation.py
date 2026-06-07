import pandas as pd

df = pd.read_csv("../source_data/customers_source.csv")

duplicates = df[df.duplicated()]

if len(duplicates) > 0:
    print("Duplicate records found")
    print(duplicates)
else:
    print("No duplicate records found")

import pandas as pd

df = pd.read_csv("../source_data/customers_source.csv")

duplicates = df[df.duplicated()]

print(duplicates)

import pandas as pd

df = pd.read_csv("../source_data/customers_source.csv")

print(df.isnull().sum())

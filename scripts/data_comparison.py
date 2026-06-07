import pandas as pd

source = pd.read_csv("../source_data/customers_source.csv")
target = pd.read_csv("../target_data/customers_target.csv")

if source.equals(target):
    print("PASS: Source and Target data match")
else:
    print("FAIL: Data mismatch found")

import parquet
import json
import pandas as pd
df = pd.read_parquet('testset.parquet')
print(df)

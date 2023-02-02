#!/bin/env python3

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("nyc_squirrels.csv")

print(df)
print(df.iloc[0])

obj_columns = df.select_dtypes(include=['object']).columns

for col in obj_columns:
	print(df[col].value_counts(dropna=False))

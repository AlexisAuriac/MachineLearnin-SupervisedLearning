#!/bin/env python3

import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = np.load('inputs.npy')

df = pd.DataFrame()
df["feature"] = list(range(X.shape[1]))

df["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]

print(df['VIF'].mean())
print(df['VIF'].std())

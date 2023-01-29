#!/bin/env python3

import numpy as np
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

X = np.load('inputs.npy')

df = pd.DataFrame()
df["feature"] = list(range(X.shape[1]))

df["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]

print(f"Mean VIF: {df['VIF'].mean():.3f}")
# 7.826
print(f"Standard deviation of VIF: {df['VIF'].std():.3f}")
# 0.846

#!/bin/python3

"""
Selects the most informative features in the dataset using RFE.
"""

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE

df = pd.read_csv('nyc_squirrels.csv')

y = df['approaches'].to_numpy()

to_drop = ['unique_squirrel_id', 'hectare', 'lat_long', 'approaches']
for col in to_drop:
	df.drop(col, axis=1, inplace=True)

for col in df.select_dtypes(include=['bool']).columns:
	df[col] = df[col].astype(int)

df['shift'] = df['shift'].apply(lambda x: 0 if x == 'AM' else 1)
df['zip_codes'].fillna(0, inplace=True)

for col in df.select_dtypes(include=['object']).columns:
	df[col] = df[col].apply(lambda x: 0 if pd.isnull(x) else 1)

X = df.to_numpy()

logreg = LogisticRegression()

rfe = RFE(logreg, n_features_to_select=10)
rfe = rfe.fit(X, y)

print(rfe.support_)
print(rfe.ranking_)

for i in range(len(df.columns)):
	if rfe.support_[i]:
		print(f'yes: {df.columns[i]}')
	else:
		print(f'no:  {df.columns[i]}')

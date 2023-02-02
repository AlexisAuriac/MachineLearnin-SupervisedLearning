#!/bin/env python3

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import make_scorer, accuracy_score

def get_data():
	df = pd.read_csv('nyc_squirrels.csv')

	to_drop = ['unique_squirrel_id', 'hectare', 'lat_long']
	for col in to_drop:
		df.drop(col, axis=1, inplace=True)

	for col in df.select_dtypes(include=['bool']).columns:
		df[col] = df[col].astype(int)

	df['shift'] = df['shift'].apply(lambda x: 0 if x == 'AM' else 1)
	df['zip_codes'].fillna(0, inplace=True)

	for col in df.select_dtypes(include=['object']).columns:
		df[col] = df[col].apply(lambda x: 0 if pd.isnull(x) else 1)

	X = df.drop('approaches', axis=1).to_numpy()
	y = df['approaches'].to_numpy()

	return X, y

if __name__ == '__main__':
	X, y = get_data()

	param_grid = {
		'C': np.logspace(-3, 3, 7),
		'solver' : ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
		'max_iter': [1000, 2500, 5000],
	}

	lg = LogisticRegression()

	scorer = make_scorer(accuracy_score)
	search = RandomizedSearchCV(lg, param_grid, scoring=scorer)

	search.fit(X, y.ravel())

	print(f'Best parameters: {search.best_params_}')
	# {'solver': 'lbfgs', 'max_iter': 1000, 'C': 0.001}
	print(f'Best score: {search.best_score_:.3f}')
	# 0.941

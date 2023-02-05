#!/bin/env python3

"""
Simplifies dataset using one hot encoding and uses a Logistic Regression model to try and predict if the squirrel approaches.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import make_scorer, accuracy_score

def get_data():
	"""
	Loads and simplifies dataset using one hot encoding.
	"""
	df = pd.read_csv("nyc_squirrels.csv")

	y = df['approaches'].to_numpy()

	to_drop = ['unique_squirrel_id', 'hectare', 'lat_long', 'approaches']
	for col in to_drop:
		df.drop(col, axis=1, inplace=True)

	for col in df.select_dtypes(include=['bool']).columns:
		df[col] = df[col].astype(int)

	categorical_columns = df.select_dtypes(include=['object']).columns
	categorical_data = df[categorical_columns].values

	onehot_encoder = OneHotEncoder(sparse=False)

	X = onehot_encoder.fit_transform(categorical_data)

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
	# {'solver': 'lbfgs', 'max_iter': 5000, 'C': 1.0}
	print(f'Best score: {search.best_score_:.3f}')
	# 0.941	

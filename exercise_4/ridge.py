#!/bin/env python3

"""
Ridge regression model with hyperparameter tuning
"""

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, r2_score

X = np.load('inputs.npy')
y = np.load('labels.npy')

param_grid = {
	'alpha': np.logspace(-3, 3, 7),
	'fit_intercept': [True, False],
}

model = Ridge()

scorer = make_scorer(r2_score)

search = GridSearchCV(estimator=model, param_grid=param_grid, scoring=scorer)
search.fit(X, y.ravel())

print(f'Best parameters: {search.best_params_}')
# {'alpha': 1.0, 'fit_intercept': False}
print(f'Best score: {search.best_score_:.3f}')
# 0.765

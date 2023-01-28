#!/bin/env python3

"""
RandomForest model with hyperparameter tuning
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import make_scorer, accuracy_score

X = np.load('inputs.npy')
y = np.load('labels.npy')

param_grid = {
    # Number of trees in random forest
    'n_estimators': [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)],
    # Number of features to consider at every split
    'max_features': ['sqrt', 'log2'],
    # Maximum number of levels in tree
    'max_depth': [int(x) for x in np.linspace(10, 110, num = 11)] + [None],
    # Minimum number of samples required to split a node
    'min_samples_split': [2, 5, 10],
    # Minimum number of samples required at each leaf node
    'min_samples_leaf': [1, 2, 4],
    # Method of selecting samples for training each tree
    'bootstrap': [True, False],
}

rf = RandomForestClassifier()

scorer = make_scorer(accuracy_score)

rand_search = RandomizedSearchCV(rf, param_grid, scoring=scorer)

rand_search.fit(X, y.ravel())

print("Best parameters:", rand_search.best_params_)
# {'n_estimators': 400, 'min_samples_split': 10, 'min_samples_leaf': 4, 'max_features': 'sqrt', 'max_depth': None, 'bootstrap': False}
print("Best score:", rand_search.best_score_)
# 0.816

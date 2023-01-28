#!/bin/env python3

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
# from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import make_scorer, accuracy_score

X = np.load('inputs.npy')
y = np.load('labels.npy')

param_grid = {
    # not sure if this parameter is deprecated + compatibility with solvers is complicated, search gives a bunch of errors
    # 'penalty': ['l1', 'l2', 'elasticnet', None],
    # controls regularization strength (prevents overfitting)
    'C': np.logspace(-3, 3, 7),
    # some solvers are better depending on: number of features, size of dataset, number of classes, etc...
    'solver' : ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    # https://stats.stackexchange.com/a/184026/378578
    'max_iter': [1000, 2500, 5000],
}

lg = LogisticRegression()

scorer = make_scorer(accuracy_score)

# Grid search is a bit slow (~70s) but still usable
search = GridSearchCV(estimator=lg, param_grid=param_grid, scoring=scorer)
# search = RandomizedSearchCV(lg, param_grid, scoring=scorer)

search.fit(X, y.ravel())

print("Best parameters:", search.best_params_)
# {'C': 0.01, 'max_iter': 1000, 'solver': 'newton-cg'}
print("Best score:", search.best_score_)
# 0.904

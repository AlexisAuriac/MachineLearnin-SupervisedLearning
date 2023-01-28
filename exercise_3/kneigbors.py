#!/bin/env python3

"""
KNeigbors model with hyperparameter tuning
"""

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score

X = np.load('inputs.npy')
y = np.load('labels.npy')

param_grid = {
    # can decrease time consumption at the cost of accuracy
    # difficult to tune: https://stackoverflow.com/a/49969671/12864941
    # 'leaf_size': list(range(1, 50, 2)),
    # small n_neighbors -> risk of overfitting
    # large n_neighbors -> risk of underfitting
    'n_neighbors': list(range(3, 30, 2)),
    # uniform -> all points have same importance
    # distance -> closer neighbors of a query point will have a greater influence than neighbors which are further away.
    'weights': ['uniform', 'distance'],
    # p = 1 -> Manhattan distance
    # p = 2 -> Euclidean distance
    'p': [1, 2]
}

kn = KNeighborsClassifier()

scorer = make_scorer(accuracy_score)

search = GridSearchCV(estimator=kn, param_grid=param_grid, scoring=scorer)
search.fit(X, y.ravel())

print("Best parameters:", search.best_params_)
# {'n_neighbors': 11, 'p': 2, 'weights': 'uniform'}
print("Best score:", search.best_score_)
# 0.804

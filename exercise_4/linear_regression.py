#!/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score

X = np.load('inputs.npy')
y = np.load('labels.npy')

model = LinearRegression()

scores = cross_val_score(model, X, y, cv=5, scoring='r2')

print(f'Mean R2 score: {np.mean(scores):.3f}')
# 0.688
print(f'Standard deviation of R2 scores: {np.std(scores):.3f}')
# 0.113

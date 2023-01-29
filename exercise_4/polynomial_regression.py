#!/bin/env python3

"""
Polynomial regression model with cross validation
The model is tested with degree 2 and 3
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import PolynomialFeatures

X = np.load('inputs.npy')
y = np.load('labels.npy')

poly_2 = PolynomialFeatures(degree=2)
poly_3 = PolynomialFeatures(degree=3)

X_poly_2 = poly_2.fit_transform(X)
X_poly_3 = poly_3.fit_transform(X)

model = LinearRegression()

scores_2  = cross_val_score(model, X_poly_2, y, cv=5, scoring='r2')
scores_3  = cross_val_score(model, X_poly_3, y, cv=5, scoring='r2')

print(f'Mean R2 score (degree=2): {np.mean(scores_2):.3f}')
# 0.750
print(f'Mean R2 score (degree=3): {np.mean(scores_3):.3f}')
# 0.722

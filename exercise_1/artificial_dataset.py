#!/bin/env python3

import numpy as np

# generate data from different distributions: https://stackabuse.com/generating-synthetic-data-with-numpy-and-scikit-learn/
LINES = 300

x_list = [
    np.random.randint(0, 6, size=LINES),
    np.random.exponential(1, size=LINES),
    np.random.lognormal(0, 1, size=LINES),
]

# generate correlated data: https://stackoverflow.com/a/16026231/12864941
mu = np.array([5.0, 0.0, 10.0])
r = np.array([
  [  3.40, -2.75, 2.00],
  [ -2.75,  5.50,  0],
  [ 2.00,  0,  1.25]
])

y = np.random.multivariate_normal(mu, r, size=LINES, check_valid='ignore')

x_list = list(zip(*x_list))
x_list = np.concatenate((x_list, y), axis=1)

np.save('data.npy', x_list)

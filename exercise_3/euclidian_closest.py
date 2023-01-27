#!/bin/python3

import math

import numpy as np
from scipy.spatial import distance

inputs = np.load('inputs.npy')
labels = np.load('labels.npy')

right = 0
wrong = 0

for i in range(inputs.shape[0]):
	closest_idx = None
	closest = math.inf

	for j in range(inputs.shape[0]):
		if i == j:
			continue

		diss = distance.euclidean(inputs[i], inputs[j])

		if diss < closest:
			closest = diss
			closest_idx = j

	predicted = labels[closest_idx]

	if predicted == labels[i]:
		right += 1
	else:
		wrong += 1


print(f'right: {right}')
print(f'wrong: {wrong}')
print(f'{right / inputs.shape[0] * 100}%')
# 68.2%

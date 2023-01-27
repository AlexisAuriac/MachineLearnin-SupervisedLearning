#!/bin/python3

import numpy as np

import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

inputs = np.load('inputs.npy')
labels = np.load('labels.npy')

train_X, test_X, train_y, test_y = train_test_split(inputs, labels)

logreg_clf = LogisticRegression()
logreg_clf.fit(train_X, train_y)

pred = logreg_clf.predict(test_X)

right = 0

for i in range(len(test_y)):
	if test_y[i] == pred[i]:
		right += 1

print(f'accuracy: {right / len(test_y)}')

from typing import List, Callable, TypeVar

import numpy as np

A = TypeVar('A')
B = TypeVar('B')
def mapArrayToMatrix(l: List[A], f: Callable[[A, A], B]) -> np.ndarray:
	size = len(l)
	m = np.zeros((size, size))

	for i in range(size):
		for j in range(size):
			m[i, j] = f(l[i], l[j])

	return m

A = TypeVar('A')
B = TypeVar('B')
def matrixToDict(m: np.ndarray, x: List[A], y: List[A]) -> dict[A, B]:
	d = {}

	for i in range(len(x)):
		d2 = {}
		for j in range(len(y)):
			d2[y[j]] = m[i, j]
		d[x[i]] = d2

	return d

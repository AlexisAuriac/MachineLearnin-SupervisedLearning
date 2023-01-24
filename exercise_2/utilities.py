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

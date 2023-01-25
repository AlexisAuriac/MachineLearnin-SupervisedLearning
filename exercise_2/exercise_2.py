#!/bin/env python3

import math
from typing import Tuple

import numpy as np
import pandas as pd

from utilities import mapArrayToMatrix
from job import dissimilarity_jobs, job_char_df, job_diss_df, job_diss_dict
from city import dissimilarity_cities, city_char_df, city_diss_df, city_diss_dict
from music import dissimilarity_music, music_diss_df, music_diss_dict

print('---\nJob characteristics')
print(job_char_df)
print('---\nJob dissimilarity')
print(job_diss_df)

print('---\nCity characteristics')
print(city_char_df)
print('---\nCity dissimilarity')
print(city_diss_df)

print('---\nMusic dissimilarity')
print(music_diss_df)

data_df = pd.read_csv('dataset.csv', index_col=0)

# Unused
def dissimilarity_person(person1: Tuple[float, float, str, str, str], person2: Tuple[float, float, str, str, str]) -> float:
	age1 = person1[0]
	age2 = person2[0]

	height1 = person1[1]
	height2 = person2[1]

	job1 = person1[2]
	job2 = person2[2]

	city1 = person1[3]
	city2 = person2[3]

	music1 = person1[4]
	music2 = person2[4]

	diss_age = (age1 - age2) ** 2
	diss_height = (height1 - height2) ** 2
	diss_job = job_diss_dict[job1][job2]
	diss_city = city_diss_dict[city1][city2]
	diss_music = music_diss_dict[music1][music2]

	return diss_age

data = np.array(data_df.values)

print('==== Dissimilarity of columns within the dataset ====')

diss_col_df = {
	'mean': [],
	'std': [],
	'adjusted std': [],
}

diss_age = mapArrayToMatrix(data[:, 0], lambda x, y: abs(x-y))

diss_col_df['mean'].append(diss_age.mean())
diss_col_df['std'].append(diss_age.std())
diss_age *= 10 / diss_age.mean()
diss_col_df['adjusted std'].append(diss_age.std())

diss_height = mapArrayToMatrix(data[:, 1], lambda x, y: abs(x-y))

diss_col_df['mean'].append(diss_height.mean())
diss_col_df['std'].append(diss_height.std())
diss_height *= 10 / diss_height.mean()
diss_col_df['adjusted std'].append(diss_height.std())

diss_job = mapArrayToMatrix(data[:, 2], lambda x, y: job_diss_dict[x][y])

diss_col_df['mean'].append(diss_job.mean())
diss_col_df['std'].append(diss_job.std())
diss_job *= 10 / diss_job.mean()
diss_col_df['adjusted std'].append(diss_job.std())

diss_city = mapArrayToMatrix(data[:, 3], lambda x, y: city_diss_dict[x][y])

diss_col_df['mean'].append(diss_city.mean())
diss_col_df['std'].append(diss_city.std())
diss_city *= 10 / diss_city.mean()
diss_col_df['adjusted std'].append(diss_city.std())

diss_music = mapArrayToMatrix(data[:, 4], lambda x, y: music_diss_dict[x][y])

diss_col_df['mean'].append(diss_music.mean())
diss_col_df['std'].append(diss_music.std())
diss_music *= 10 / diss_music.mean()
diss_col_df['adjusted std'].append(diss_music.std())
diss_col_df = pd.DataFrame(diss_col_df, ['age', 'height', 'job', 'city', 'favorite music style'])
print(diss_col_df)


# See README for justifications
AGE_IMP_FACTOR = 3
HEIGHT_IMP_FACTOR = 1
JOB_IMP_FACTOR = 3
CITY_IMP_FACTOR = 2.5
MUSIC_IMP_FACTOR = 0.5

diss_matrix = np.sqrt(
	(diss_age * AGE_IMP_FACTOR) ** 2
	+ (diss_height * HEIGHT_IMP_FACTOR) ** 2
	+ (diss_job * JOB_IMP_FACTOR) ** 2
	+ (diss_city * CITY_IMP_FACTOR) ** 2
	+ (diss_music * MUSIC_IMP_FACTOR) ** 2
)

np.save('data.npy', diss_matrix)

print('====== total ======')
print(f'mean: {diss_matrix.mean()}')
print(f'standard deviation: {diss_matrix.std()}')


# from examples: https://numpy.org/doc/stable/reference/generated/numpy.argmin.html
diss_matrix[diss_matrix == 0] = math.inf
(min_diss_1, min_diss_2) = np.unravel_index(np.argmin(diss_matrix, axis=None), diss_matrix.shape)

diss_matrix[diss_matrix == math.inf] = -math.inf
(max_diss_1, max_diss_2) = np.unravel_index(np.argmax(diss_matrix, axis=None), diss_matrix.shape)

print('==== 2 most similar items ====')
print(data_df.iloc[[min_diss_1, min_diss_2]])

print('==== 2 most dissimilar items ====')
print(data_df.iloc[[max_diss_1, max_diss_2]])

#!/bin/env python3

import numpy as np
import pandas as pd

from utilities import mapArrayToMatrix
from job import dissimilarity_jobs, job_char_df, job_diss_df
from city import dissimilarity_cities, city_char_df, city_diss_df
from music import dissimilarity_music, music_diss_df

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

# data = pd.read_csv('dataset.csv')
# print(data['favorite music style'].unique())

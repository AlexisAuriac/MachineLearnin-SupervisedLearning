import numpy as np
import pandas as pd

from utilities import mapArrayToMatrix, matrixToDict

jobs = [
	'designer',
	'fireman',
	'teacher',
	'doctor',
	'painter',
	'developper',
	'engineer',
]

job_metrics = ['art', 'science', 'altruism']

jobs_char = np.array([
	[8, 3, 4],
	[0, 7, 10],
	[4, 5, 6],
	[2, 9, 8],
	[10, 2, 3],
	[3, 6, 1],
	[4, 8, 2],
])

# https://stackoverflow.com/a/29482058/12864941
job_char_df = pd.DataFrame(jobs_char, jobs, job_metrics)

# A function that does this probably already exists
# https://stackoverflow.com/a/1401828/12864941
dissimilarity_jobs = mapArrayToMatrix(jobs_char, lambda x, y: np.linalg.norm(y - x))

job_diss_df = pd.DataFrame(dissimilarity_jobs, jobs, jobs)

job_diss_dict = matrixToDict(dissimilarity_jobs, jobs, jobs)

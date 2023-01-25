import numpy as np
import pandas as pd

from utilities import matrixToDict

music_styles = [
	'trap',
	'hiphop',
	'metal',
	'rock',
	'rap',
	'classical',
	'other',
	'jazz',
	'technical death metal'
]

dissimilarity_music = np.array([
	[0,  3,  20, 20, 5,  20, 10, 15, 20],
	[3,  0,  18, 17, 5,  15, 10, 12, 20],
	[20, 18, 0,  5,  10, 14, 10, 20, 5],
	[20, 17, 5,  0,  10, 12, 10, 17, 13],
	[5,  5,  10, 10, 0,  15, 10, 15, 20],
	[20, 15, 14, 12, 15, 0,  10, 8,  20],
	[10, 10, 10, 10, 10, 10, 0,  10, 10],
	[15, 12, 20, 17, 15, 8,  10, 0,  20],
	[20, 20, 5,  13, 20, 20, 10, 20, 0],
])

# Check that the matrix is symmetric
assert (dissimilarity_music == dissimilarity_music.T).all()

music_diss_df = pd.DataFrame(dissimilarity_music, music_styles, music_styles)

music_diss_dict = matrixToDict(dissimilarity_music, music_styles, music_styles)

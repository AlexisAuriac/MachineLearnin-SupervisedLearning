import math

import numpy as np
import pandas as pd
import geopy.distance

from utilities import mapArrayToMatrix

cities = [
	'paris',
	'marseille',
	'toulouse',
	'madrid',
	'lille'
]

cities_metrics = ['coordinates', 'population', 'country', 'capital']

# All these were found with a simple google search, they may bot be completely accurate or up to date
cities_char = [
	[(48.8566, 2.3522), 2.161e6, 'France', True],
	[(43.2965, 5.3698), 861.635, 'France', False],
	[(43.6047, 1.4442), 471.941, 'France', False],
	[(40.4168, 3.7038), 3.223e6, 'Spain', True],
	[(50.6292, 3.0573), 232.741, 'France', False],
]

city_char_df = pd.DataFrame(cities_char, cities, cities_metrics)

def computeDissimilarityCity(city1, city2):
	global i
	city1_coords = city1[0]
	city2_coords = city2[0]

	city1_population = city1[1]
	city2_population = city2[1]

	city1_country = city1[2]
	city2_country = city2[2]

	city1_capital = city1[3]
	city2_capital = city2[3]

	# https://stackoverflow.com/a/43211266/12864941232,741
	distance = geopy.distance.geodesic(city1_coords, city2_coords).km

	dissimilarity_capital = 0 if city1_capital == city2_capital else 5
	dissimilarity_country = 0 if city1_country == city2_country else 10

	pop_diff = abs(city1_population - city2_population)

	return math.sqrt(
		0 if distance == 0 else math.log(distance) ** 2
		+ 0 if pop_diff == 0 else math.log(pop_diff) ** 2
		+ dissimilarity_country ** 2
		+ dissimilarity_capital ** 2
	)

dissimilarity_cities = mapArrayToMatrix(cities_char, computeDissimilarityCity)

# https://stackoverflow.com/a/29482058/12864941
city_diss_df = pd.DataFrame(dissimilarity_cities, cities, cities)

# Exercise 2: definition of a metric

## Subject

```
A dataset representing a population is stored in dataset.csv inside the project/ex_2_metric/
folder.

Define a metric in this dataset, which means define a dissimilarity between the samples, by taking into account all their features (columns of the dataset).

Some features are numerical and others are categorical, hence you can not use a standard euclidean metric, and you need to define a custom metric, like we did in the code/metrics/hybrid_data/ exercise during the course. Compute the mean dissimilarity and the standard deviation of the dissimilarity distribution that you obtain, and save the dissimilarity matrix to a file (e.g. a npy file).

Importantly, you must define and explain which features are more important with this metric, since you have to balance the contribution of all the features. Your metric should be meaningful in the sense that not all feature values should induce the same contribution to the dissimilarity : the music style "technical death metal" is closer to "metal" than it is to "classical".
```

## Sources

Simple explaination of similarity/dissimilarity/distance in datascience (with examples): https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681

## Dataset

columns: age,height,job,city,favorite music style

### Job

(see job.py)

Non numerical data.

Jobs in the dataset: designer, fireman, teacher, doctor, painter, developper, engineer

The metrics and values chosen are subjective and will not be justified.

Evaluating jobs using 3 metrics: art, science, and altruism

Values:
```
            art  science  altruism
designer      8        3         4
fireman       0        7        10
teacher       4        5         6
doctor        2        9         8
painter      10        2         3
developper    3        6         1
engineer      4        8         2
```

Using the euclidian distance we get this dissimilarity matrix:
```
             designer    fireman   teacher     doctor    painter  developper  engineer
designer     0.000000  10.770330  4.898979   9.380832   2.449490    6.557439  6.708204
fireman     10.770330   0.000000  6.000000   3.464102  13.190906    9.539392  9.000000
teacher      4.898979   6.000000  0.000000   4.898979   7.348469    5.196152  5.000000
doctor       9.380832   3.464102  4.898979   0.000000  11.747340    7.681146  6.403124
painter      2.449490  13.190906  7.348469  11.747340   0.000000    8.306624  8.544004
developper   6.557439   9.539392  5.196152   7.681146   8.306624    0.000000  2.449490
engineer     6.708204   9.000000  5.000000   6.403124   8.544004    2.449490  0.000000
```

### City

(see city.py)

Non numerical data.

Cities in the dataset: paris, marseille, toulouse, madrid, lille

The metrics and values chosen are subjective and will not be justified.

Evaluating cities using 4 metrics: coordinates, population, country, and if it is a capital.

Values:
```
                 coordinates   population country  capital
paris      (48.8566, 2.3522)  2161000.000  France     True
marseille  (43.2965, 5.3698)      861.635  France    False
toulouse   (43.6047, 1.4442)      471.941  France    False
madrid     (40.4168, 3.7038)  3223000.000   Spain     True
lille      (50.6292, 3.0573)      232.741  France    False
```

To measure distance we use the library ```geopy``` (Euclidian won't work since the earth isn't flat). We then use log10 so that it doesn't impact the dissimilarity too much.

We compare the population using euclidian distance. We then use log10 so that it doesn't impact the dissimilarity too much.

Not being from the same country adds a dissimilarity of ```10```.

One being a capital and not the other adds a dissimilarity of ```5```.

All of these are squared and the result is square rooted ("square root" isn't a verb but I don't care 😎).

We get this dissimilarity matrix:
```
               paris  marseille   toulouse     madrid      lille
paris       0.000000  15.418889  15.419060  17.103627  15.419165
marseille  15.418889   0.000000   5.965362  18.696708   6.443963
toulouse   15.419060   5.965362   0.000000  18.696805   5.477300
madrid     17.103627  18.696708  18.696805   0.000000  18.696864
lille      15.419165   6.443963   5.477300  18.696864   0.000000
```

### Music style

(see music.py)

Non numerical data.

Music styles in the dataset: trap, hiphop, metal, rock, rap, classical, other, jazz, technical death metal

Hard to find metrics, there aren't clear delimitations between music styles.

Could maybe use Google trends to measure popularity.

Gave each pair a dissimilarity from 0 to 20 by hand, based on my personal knowledge.

Some important assumptions that influenced my choices:
- trap, hiphop, and rap are related
- metal, rock, and technical death metal are related
- other is very vague and large, gave it a dissimilarity of 10 for all music styles

We get this dissimilarity matrix:
```
                       trap  hiphop  metal  rock  rap  classical  other  jazz  technical death metal
trap                      0       3     20    20    5         20     10    15                     20
hiphop                    3       0     18    17    5         15     10    12                     20
metal                    20      18      0     5   10         14     10    20                      5
rock                     20      17      5     0   10         12     10    17                     13
rap                       5       5     10    10    0         15     10    15                     20
classical                20      15     14    12   15          0     10     8                     20
other                    10      10     10    10   10         10      0    10                     10
jazz                     15      12     20    17   15          8     10     0                     20
technical death metal    20      20      5    13   20         20     10    20                      0
```

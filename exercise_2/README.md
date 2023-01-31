# Exercise 2: definition of a metric

## Subject

```
A dataset representing a population is stored in dataset.csv inside the project/ex_2_metric/
folder.

Define a metric in this dataset, which means define a dissimilarity between the samples, by taking into account all their features (columns of the dataset).

Some features are numerical and others are categorical, hence you can not use a standard euclidean metric, and you need to define a custom metric, like we did in the code/metrics/hybrid_data/ exercise during the course. Compute the mean dissimilarity and the standard deviation of the dissimilarity distribution that you obtain, and save the dissimilarity matrix to a file (e.g. a npy file).

Importantly, you must define and explain which features are more important with this metric, since you have to balance the contribution of all the features. Your metric should be meaningful in the sense that not all feature values should induce the same contribution to the dissimilarity : the music style "technical death metal" is closer to "metal" than it is to "classical".
```

## Main sources

Simple explanation of similarity/dissimilarity/distance in datascience (with great examples): https://towardsdatascience.com/17-types-of-similarity-and-dissimilarity-measures-used-in-data-science-3eb914d2681

## Dissimilarity by individual feature

columns: age,height,job,city,favorite music style

### age

euclidean distance

### height

euclidean distance

### Job

(see job.py)

Non numerical data.

Jobs in the dataset: designer, fireman, teacher, doctor, painter, developper, engineer

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

Using the euclidean distance we get this dissimilarity matrix:
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

Evaluating cities using 4 metrics: coordinates, population, country, and if it is a capital.

Values:
```
                 coordinates  population country  capital
paris      (48.8566, 2.3522)     2161000  France     True
marseille  (43.2965, 5.3698)      861635  France    False
toulouse   (43.6047, 1.4442)      471941  France    False
madrid     (40.4168, 3.7038)     3223000   Spain     True
lille      (50.6292, 3.0573)      232741  France    False
```

To measure distance we use the library ```geopy``` (Euclidean won't work since the earth isn't flat). We then use log10 so that it doesn't impact the dissimilarity too much.

We compare the population using euclidean distance. We then use log10 so that it doesn't impact the dissimilarity too much.

Not being from the same country adds a dissimilarity of ```10```.

One being a capital and not the other adds a dissimilarity of ```5```.

All of these are squared and the result is square rooted ("square root" isn't a verb but I don't care 😎).

We get this dissimilarity matrix:
```
               paris  marseille   toulouse     madrid      lille
paris       0.000000   7.897956   7.986461  11.675366   8.031395
marseille   7.897956   0.000000   5.590724  12.869235   5.798577
toulouse    7.986461   5.590724   0.000000  12.902215   5.378761
madrid     11.675366  12.869235  12.902215   0.000000  12.920325
lille       8.031395   5.798577   5.378761  12.920325   0.000000
```

### Music style

(see music.py)

Non numerical data.

Music styles in the dataset: trap, hiphop, metal, rock, rap, classical, other, jazz, technical death metal

Hard to find metrics, there aren't clear delimitation between music styles.

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

## Overall dissimilarity

(see exercise_2.py)

### Adjusting means

If we look at the mean and standard deviation for each column we get:
```
                            mean       std
age                     6.456159  4.892174
height                  6.000623  4.679549
job                     6.259779  3.747122
city                    6.950629  5.205568
favorite music style   11.796500  6.390359
```

The mean isn't the same, which means that because of the way we compute dissimilarity some columns have inherently more value, that's bad ! It also makes standard deviations impossible to compare.

We will try to have all means equal 10 (10 is arbitrary, it makes things relatively readable).

After adjustment we get this:
```
                            mean       std  adjusted std
age                     6.456159  4.892174      7.577531
height                  6.000623  4.679549      7.798439
job                     6.259779  3.747122      5.986029
city                    6.950629  5.205568      7.489348
favorite music style   11.796500  6.390359      5.417165
```

### Deciding feature importance

Age: The age of a person changes a lot of a person, beliefs, physical ability, experience, etc...
-> **3**

Height: Beside appearance and physical ability (in some contexts) this doesn't change much
-> **1**

Job: job is closely related to knowledge, ability, wealth, status, and more
-> **3**

City: Geographical location is related to culture, opportunities, language, and more
-> **2.5**

Favorite music style: As explained before, this dissimilarity is very hard to measure and music styles have a lot of intersections
-> **0.5**

### Result matrix

See ```dissimilarity_matrix.npy``` for the final dissimilarity matrix.

mean: ```57.719```

standard deviation: ```19.274```

### Side note: most (dis)similar items

Most similar items:
```
           age      height      job    city favorite music style
102  27.086348  180.242244  teacher  madrid                 jazz
163  26.968458  179.665081  teacher  madrid                 jazz
```

Most dissimilar items:
```
          age      height      job      city favorite music style
40  10.851506  169.432515  fireman     lille                 jazz
85  46.610179  181.358551  fireman  toulouse                 trap
```

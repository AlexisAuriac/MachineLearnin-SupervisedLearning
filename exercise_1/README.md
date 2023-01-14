# Exercise 1: artificial dataset generation

## Subject

```
The goal of this exercise is to work with statistical notions such as mean, standard
deviation, and correlation.

Write a file named artificial_dataset.py that generates a numerical dataset with
300 datapoints (i.e. lines) and at least 6 columns and saves it to a csv file or to a
numpy array in a binary python file.

The columns must satisfy the following requirements :
- they must all have a different mean
- they must all have a different standard deviation (English for "écart type")
- at least one column should contain integers.
- at least one column should contain floats.
- one column must have a mean close to 2.5.
- some columns must be positively correlated.
- some columns must be negatively correlated.
- some columns must have a correlation close to 0.
```

## Sources

generate data from different distributions: https://stackabuse.com/generating-synthetic-data-with-numpy-and-scikit-learn/
generate correlated data: https://stackoverflow.com/a/16026231/12864941

## Todo

- add documentation
- improve code
- redact correctly for report
- ask teacher if results/methods are good ? (not sure that's allowed)

## Usage

Run ```artificial_dataset.py``` to create a ```data.npy``` file.

```plot_dataset.py``` contains some tests to check the requirements are fullfilled.

## requirements

### different mean

(with random data, will not be the same everytime)

uniform: 2.58
normal: 0.8975425935444271
exponential: 1.6862197333034463
normal 1: 4.707184590116353
normal 2: 0.34861619419389656
normal 3: 10.115023077708935

### different standard deviation

uniform: 1.7522176424938392
normal: 0.8269509872971826
exponential: 1.9979611032118032
normal 1: 1.8894875149456702
normal 2: 2.4304248257090313
normal 3: 1.3524791279302508

### column with integers

uniform

### column with floats

all but uniform

### column with mean close to 2.5

uniform

### column correlations

(using [numpy.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy-corrcoef))

Example correlation:
```python
[[ 1.         -0.5595593   0.66913029]
 [-0.5595593   1.          0.03168539]
 [ 0.66913029  0.03168539  1.        ]]
```

*normal 1* is **negatively correlated** with *normal 2*
*normal 1* is **positively correlated** with *normal 3*
*normal 2* is **has a correlation close to 0** with *normal 3*

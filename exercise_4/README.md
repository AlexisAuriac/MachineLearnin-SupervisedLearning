# Exercise 4: prediction of the amount of electricity produced (regression)

## Subject

We would like to predict the amount of electricity produced by a windfarm, as a function of the information gathered in a number of physical sensors (e.g. speed of the wind, temperature, ...).

The dataset is stored in ```project/ex_4_regression_windfarm/```:
- The inputs x are stored in inputs.npy.
- The labels y are stored in labels.npy

The instructions are the same as in 3.

Your objective should be to obtain a R2 score superior to 0.85 on a test set or as a cross validation score.

https://fr.wikipedia.org/wiki/Coefficient_de_d%C3%A9termination

https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html

Several methods might work, including some methods that we have not explicitely studied in the class. Do not hesitate to try such methods.

## Main sources

simple explanation of regression and regression techniques: https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/

great tutorial for polynomial regression: https://data36.com/polynomial-regression-python-scikit-learn/

## Linear regression

(see linear_regression.py)

"Vanilla linear regression doesn't have any hyperparameters. But variants of linear regression do." - https://www.oreilly.com/library/view/evaluating-machine-learning/9781492048756/ch04.html

Mean R2: ```0.688```

## Logistic regression

Can't use it because dependent variable is not binary.

## Polynomial regression

(see polynomial_regression.py)

Mean R2 (degree=2): ```0.750```
Mean R2 (degree=3): ```0.722```

Better than linear regression but still not enough.

## VIF / multicollinearity

how to compute and interpret VIF: https://www.displayr.com/variance-inflation-factors-vifs/

code example: https://www.geeksforgeeks.org/detecting-multicollinearity-with-vif-python/

The VIF of the data is moderately high.

## Ridge regression

Mean R2: ```0.765```

## Lasso regression

Mean R2: ```0.887```

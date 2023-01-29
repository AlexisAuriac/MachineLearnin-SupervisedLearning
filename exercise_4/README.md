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

Several methods might work, including some methods that we have not explicitly studied in the class. Do not hesitate to try such methods.

## Main sources

simple explanation of regression and regression techniques: https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/

great tutorial for polynomial regression: https://data36.com/polynomial-regression-python-scikit-learn/

how to compute and interpret VIF: https://www.displayr.com/variance-inflation-factors-vifs/

code example for computing VIF: https://www.geeksforgeeks.org/detecting-multicollinearity-with-vif-python/

## Linear regression

(see linear_regression.py)

Mean R2: ```0.688```

This accuracy is too low.

## Logistic regression

Can't use it because dependent variable is not binary.

## Polynomial regression

(see polynomial_regression.py)

Mean R2 (degree=2): ```0.750```

Mean R2 (degree=3): ```0.722```

The reduced accuracy with degree=3 can be explained by overfitting.

degree=4 is too complex to be tested (I don't have enough RAM test it anyways).

This method yields better results than linear regression but is still not enough.

## VIF / multicollinearity

(see data_vif.py)

mean VIF: ```7.826```

Standard deviation of VIF: ```0.846```

The VIF of the data is moderately high, which is a sign of multicollinearity.

Ridge and Lasso regression are better for dataset who suffer from multicollinearity.

## Ridge regression

(see ridge.py)

Mean R2: ```0.765```

## Lasso regression

(see lasso.py)

Mean R2: ```0.887```

Satisfactory solution.

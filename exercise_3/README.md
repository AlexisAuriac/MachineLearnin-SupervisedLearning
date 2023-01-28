# Exercise 3: prediction of the winner of a nba game (classification)

## Subject

We would like to predict the winner of a Basketball game, as a function of the
data gathered at half-time.

The dataset is stored in ```project/ex_3_classification_NBA/```:
- The inputs x representing the features are stored in inputs.npy.
- The labels y are stored in labels.npy. If the home team wins, the label is 1, −1
otherwise.

You are free to choose the classification method. However, it is required that you
explain and discuss your approach in your report. For instance, you could discuss :
- the performance of several methods and models that you tried.
- the choice of the hyperparameters and the method to tune them.
- the optimization procedure.

Your objective should be to obtain a mean accuracy superior than 0.85 on a test
set or as a cross validation score.

https://scikit-learn.org/stable/modules/model_evaluation.html#accuracy-score
https://scikit-learn.org/stable/modules/cross_validation.html

Several methods might work, including some methods that we have not explici-
tely studied in the class. Do not hesitate to try such methods.

## Main sources

overview of classification and how to do it with sklearn: https://stackabuse.com/overview-of-classification-methods-in-python-with-scikit-learn/

## Solution

I tried 3 models for this exercise: KNeighbors, RandomForest and Logistic Regression.

For each model I chose some hyperparameters to tune and then used ```GridSearchCV``` or ```RandomizedSearchCV``` to tune them and measure the mean accuracy of the model.

```GridSearchCV``` and ```RandomizedSearchCV``` both use cross validation.

### KNeighbors Classifier

(see kneighbors.py)

sources:
- [official doc](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [hyperparameter tuning](https://medium.datadriveninvestor.com/k-nearest-neighbors-in-python-hyperparameters-tuning-716734bc557f)
- [issues with ```leaf_size``` tuning](https://stackoverflow.com/a/49969671/12864941)

hyperparameters:
- ```n_neighbors```: can cause overfitting or underfitting if it is too small or too big respectively
- ```weights```: give all points the same or a different importance
- ```p```: distance measure, 1 -> manhattan / 2 -> euclidean

The best parameters found using ```GridSearchCV``` were:
```
{
	'n_neighbors': 11,
	'p': 2,
	'weights': 'uniform'
}
```

They give a mean score of ```0.804```.

### RandomForest Classifier

(see random_forest.py)

sources:
- [official doc](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [hyperparameter tuning](https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74)

hyperparameters:
- ```n_estimators```: number of trees
- ```max_features```: number of features to consider at every split
- ```max_depth```: maximum number of levels in tree
- ```min_samples_split```: minimum number of samples required to split a node
- ```min_samples_leaf```: minimum number of samples required at each leaf node
- ```bootstrap```: method of selecting samples for training each tree

```GridSearchCV``` took too long so I decided to use ```RandomizedSearchCV``` for this model.

The best parameters found using ```RandomizedSearchCV``` were:
```
{
	'n_estimators': 400,
	'min_samples_split': 10,
	'min_samples_leaf': 4,
	'max_features': 'sqrt',
	'max_depth': None,
	'bootstrap': False
}
```

They give a mean score of ```0.816```.

### LogisticRegression

(see logistic_regression.py)

sources:
- [official doc](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [fix warning about failed covergence](https://stats.stackexchange.com/a/184026/378578)

hyperparameters:
- ```C```: controls regularization strength (prevents overfitting)
- ```solver```: some solvers are better depending on: number of features, size of dataset, number of classes, etc...
- ```max_iter```: maximum number of iterations taken for the solvers to converge

I am confused about the ```penalty``` hyperparameter, it seems to be deprecated in favor of solver but I am not sure. Furthermore only some values of ```solver``` are compatible with some values of ```penalty```, I am not sure how to take that into account when using ```GridSearchCV```/```RandomizedSearchCV```. I eventually decided to exclude it from the tuning.

The best parameters found using ```GridSearchCV``` were:
```
{
	'C': 0.01,
	'solver': 'newton-cg',
	'max_iter': 1000
}
```

They give a mean score of ```0.904```.

This classification method achieves a mean score superior to ```0.85```.

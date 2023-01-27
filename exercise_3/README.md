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

Managed to get a precision of ```0.904``` basically copying code from a tutorial (see main sources).

This seems waaaay too easy.

This method uses logistic regression, but the exercise 4 is supposed to be about regression

The subject also requires explaining the choice of hyperparameters and the optimization procedure, which I did not do.

Clearly I missed something.

- did I solve it in the wrong way ?
- used tools I wasn't allowed to use ?
- misunderstand the objective ?

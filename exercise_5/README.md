# Exercise 5: application of supervised learning

## Subject

Pick a dataset and perform a supervised learning on it. Ideally, your algorithm should answer an interesting question about the dataset. The supervised learning can then be either a classification or a regression.

You are free to choose the dataset within the following constraints:
- several hundreds of lines
- at least 6 attributes (columns), the first being a unique id
- some features may be categorical (non quantitative).

If necessary, you can tweak an existing dataset in order to artificially make it possible to apply analysis ans visualization techniques. Example resources to find datasets:
- [Link 1](https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research)
- [Link 2](https://perso.telecom-paristech.fr/eagan/class/igr204/datasets)
- [Link 3](https://github.com/awesomedata/awesome-public-datasets)
- [Link 4](https://www.kaggle.com/datasets)

You could start with a general analysis of the dataset, with for instance a file analysis.py that studies:
- histograms of quantitative variables with a comment on important statistical aspects, such as means, standard deviations, etc.
- A study of potential outliers
- Correlation matrices (maybe not for all variables)
- Any interesting analysis : if you have categorical data, with categories are represented most ? To what extent ?

If the dataset is very large you may also extract a random sample of the dataset to build histogram or compute correlations. You can discuss whether the randomness of the sample has an important influence on the analysis result (this will depend on
the dataset).

Whether it is a classification or a regression, you must provide an evaluation of your processing. For supervised learning, this could be an average squared error, coefficient of determination (R2 score), etc (https://scikit-learn.org/stable/modules/model_evaluation.html).

Short docstrings in the python files will be appreciated, at least at the beginning of each file.

In your report, you could include for instance:
- general informations on the dataset found in the analysis file.
- a potential comparison between several algorithm / models that you explored, if relevant
- a presentation of the method used to tune the algorithms (choice of hyperparameters, cross validation, etc).
- a short discussion of the results

Feel free to add useful visualizations for each step of your processing.

## Solution

For this exercise I chose a the [nyc_squirrels dataset](https://github.com/rfordatascience/tidytuesday/tree/master/data/2019/2019-10-29
), it comes from a census where over 300 volunteers counted and observed the squirels living in New York.

This dataset contains 3023 rows and 36 columns.

Our objective will be to predict when a squirrel approaches, this measure is interesting because sqirrels are cute and I want them to eat out of my hand 🥰.

<img src="https://i.dailymail.co.uk/i/pix/2012/10/21/article-0-159C2D56000005DC-840_634x793.jpg" />

## Simplifying the dataset

Some of the columns are numerical (longitude, latitude, date, etc...).

Some of the columns are binary (climbing, approaches, tail_twiches, etc...).

Some of the columns are strings (fur color, notes by the volunteer, a unique id, etc...).

There are some values that can be dropped immidiately:
- unique_squirrel_id: a unique id that looks like ```37F-PM-1014-03```
- lat_long: latitude and longitude of the sigthing, there are already a lat and a long feature in the dataset
- hectare: ID tag, which is derived from the hectare grid used to divide and count the park area, it is redundant with lat and long

A lot of the features are strings, but a lot of the time these features are not set.

I tried 2 methods:
- if the feature is set 1 else 0 (see simplify_dataset.py)
- using one hot encoding (see one_hot_encoding.py)

## Prediction

I then used a Logistic regression model using the approaches feature as the label.

With both ways of simplyfing the dataset we get the same accuracy: ```0.941```

Actually adding and removing features doesn't seem to affect the accuracy at all, this probably means there is a problem.

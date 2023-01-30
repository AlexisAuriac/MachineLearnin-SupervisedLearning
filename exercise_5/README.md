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

# Simple-NLP-Classifier
A simple NLP classifier by implementing the Naive Bayes Classification in python. Trained on nearly a 1500 questions long dataset, this classifier can classify whether a question asked is one of the following types - who,what,when,affirmation,unknown.
Naive Bayes classifier is a great classifier for text based classification and for making small projects. More on Naive bayes classifier can be found here https://en.wikipedia.org/wiki/Naive_Bayes_classifier.

# Explanation
We can predict the type of question into one of the 5 categories - who,what,when,affirmation,unknown.I made a class which has the following methods. In general this classifier can be used to classify any text based entities into some given labels, provided some datasets.

# Methods

### train method
This method accepts the filename as a parameter and trains the model so that it can classify any given query into one of the five labels.

### accuracy_test method
This method tests the accuracy of the trained model by performing the classification on some examples which have already been separated from the training dataset randomly.The accuracy comes out be around 80% for the given dataset.This method accepts filename as the parameter.

### predict method
This method classifies/predicts a given question/sentence/query into one of the following type of question - who,when,what,affirmation,unknown. This method accepts string as a parameter and returns the predicted label.

# Files used
predict_data.txt - this file contains the questions whose predictions/classifications are required.

training_data.txt - this file contains the training data to feed the model.

accuracy_test.txt - this file consists of some separated data from the training_data file and is tested to know the accuracy.

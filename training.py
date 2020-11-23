import numpy as np
import time
import json
import datetime
import nltk
nltk.download('punkt')
from nltk.stem.lancaster import LancasterStemmer

import data as data
import neural_network as nn
stemmer = LancasterStemmer()

words = []
classes = []
documents = []
ignore_words = ['?']

# create our training data
training = []
output = []

data.init_data(words, classes, documents, ignore_words)
data.init_training_data(training, output, words, classes, documents)

X = np.array(training)
y = np.array(output)

start_time = time.time()
hidden_neurons = 20
alpha = 0.1
epochs = 100000
dropout = False
dropout_percent = 0.2

nn.train(words, classes, X, y, hidden_neurons, alpha, epochs, dropout, dropout_percent)

elapsed_time = time.time() - start_time
print ("processing time:", elapsed_time, "seconds")
#!/usr/bin/env python
"""train a deep net on board value pairings"""
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.utils.np_utils import to_categorical
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


# import training and testing data, then segregate into values and labels
train = np.loadtxt('value_train.csv', delimiter=',', dtype=np.float32)
train_data = np.array([t[:9].reshape(3, 3) for t in train])
train_labels = np.array([t[9:] for t in train])

test = np.loadtxt('value_validate.csv', delimiter=',', dtype=np.float32)
test_data = np.array([t[:9].reshape(3, 3) for t in test])
test_labels = np.array([t[9:] for t in test])

# create model
np.random.seed(1729)
model = Sequential()
#model.add(Dense(units=12, input_dim=9, activation='relu'))
model.add(Dense(units=8, input_shape=(3, 3), activation='relu'))
#model.add(Dense(units=126, activation='relu'))
#model.add(Dense(units=7560, activation='relu'))
#model.add(Dense(units=24, activation='relu'))
#model.add(Dense(units=64, activation='relu'))
model.add(Flatten())
model.add(Dense(units=2))
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# train model
model.fit(train_data, train_labels, epochs=20, batch_size=10)

# print metrics
score = model.evaluate(test_data, test_labels, batch_size=len(test_labels), verbose=1)
print 'accuracy =', score[1]

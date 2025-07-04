# -*- coding: utf-8 -*-
"""SK_APPROACH.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ndk0dBoMU-kSMHlBAss59ppmgOQhW98Y
"""

from sklearn.datasets import load_digits
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

"""
# Load the digits dataset
digits = load_digits()

# Print the shape of the data
print(digits.data.shape)
num = 10

for i in range(num) :
  print(i)
  plt.subplot(3,4,i+1)
  imshow(digits.data[i].reshape((8,8)), cmap = 'gray')

  """

from sklearn.model_selection import train_test_split
import numpy as np

# Prepare the data and target values
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
y = [0, 1, 2, 3, 4]

# Split the data into a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

# Print the shapes of the training and test sets
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
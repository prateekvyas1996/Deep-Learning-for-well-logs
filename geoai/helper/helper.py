from mxnet import autograd
import random
import numpy as np

def synthetic_data(w, b, num_examples):  #@save
    """
    Generate y = Xw + b + noise.
	Input : array of weights w, bias scalar b and number of examples
	output : tuple of (inputs, labels)
    """
    if type(w) is list:
    	w = np.array(w)
    X = np.random.normal(0, 1, (num_examples, len(w)))
    y = np.dot(X, w) + b
    y += np.random.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))

def squared_loss(y_hat, y):  #@save
    """Squared loss."""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


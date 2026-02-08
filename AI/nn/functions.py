from numpy import exp

def sigmoid(x):
    return 1/(1 + exp(-x))

def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

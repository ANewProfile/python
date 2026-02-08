import numpy as np
from functions import sigmoid

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

if __name__ == "__main__":
    weights = np.array([0, 1])
    bias = 4
    n = Neuron(weights, bias)

    inputs = np.array([2, 3])
    output = n.feedforward(inputs)

    print(f"Output for inputs {inputs}: {output}")

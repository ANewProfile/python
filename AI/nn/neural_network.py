import numpy as np
from neuron import Neuron

class OurNeuralNetwork:
    def __init__(self, weights, bias):
        self.h1 = Neuron(weights, bias)
        self.h2 = Neuron(weights, bias)
        self.o1 = Neuron(weights, bias)

    def feedforward(self, inputs):
        h1_out = self.h1.feedforward(inputs)
        h2_out = self.h2.feedforward(inputs)
        h1h2_outs = np.array([h1_out, h2_out])

        o1_out = self.o1.feedforward(h1h2_outs)
        return o1_out

class GenericNeuralNetwork:
    def __init__(self, w1, w2, w3, w4, w5, w6, b1, b2, b3):
        h1_weights = np.array([w1, w2])
        h2_weights = np.array([w3, w4])
        o1_weights = np.array([w5, w6])

        self.h1 = Neuron(h1_weights, b1)
        self.h2 = Neuron(h2_weights, b2)
        self.o1 = Neuron(o1_weights, b3)

    def feedforward(self, inputs):
        h1_out = self.h1.feedforward(inputs)
        h2_out = self.h2.feedforward(inputs)
        h1h2_outs = np.array([h1_out, h2_out])

        o1_out = self.o1.feedforward(h1h2_outs)
        return o1_out

if __name__ == "__main__":
    """
    weights = np.array([0, 1])
    bias = 0
    net = OurNeuralNetwork(weights, bias)

    inputs = np.array([2, 3])
    output = net.feedforward(inputs)

    print(f"Output for inputs {inputs}: {output}")
    """

    data = {
        "alice": {"weight": -2, "height": -1, "gender": 1, "data": np.array([-2, -1])},
        "bob": {"weight": 25, "height": 6, "gender": 0, "data": np.array([25, 6])},
        "charlie": {"weight": 17, "height": 4, "gender": 0, "data": np.array([17, 4])},
        "diana": {"weight": -15, "height": -6, "gender": 1, "data": np.array([-15, -6])}
    }

    net = GenericNeuralNetwork(1, 1, 1, 1, 1, 1, 0, 0, 0)

    out = net.feedforward(data["alice"]["data"])

    print(out)

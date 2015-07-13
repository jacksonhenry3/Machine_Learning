import numpy as np
from scipy.special import expit
import matplotlib.pyplot as plt
class neuron(object):
    def __init__(self, numInputs,weights = None):
        super(neuron, self).__init__()
        self.numInputs = numInputs
        self.weights = weights
        if weights == None:
            self.weights   = (np.random.random(numInputs+1)-.5)*2

class layer(object):
    def __init__(self, neurons):
        super(layer, self).__init__()
        self.numNeurons = len(neurons)
        self.neurons    = neurons

class neuralNet(object):
    """docstring for neuralNet"""
    def __init__(self, layers):
        super(neuralNet, self).__init__()
        self.layers = layers
        self.numHiddenLayers = len(self.layers)
    def update(self,inputs):
        for i in range(self.numHiddenLayers):
            if  i > 0:
                inputs = outputs
            outputs = []
            weight = 0
            for j in range(self.layers[i].numNeurons):
                neuron         = self.layers[i].neurons[j]
                rawNeuronValue = sum([inputs[p]*w for p,w in enumerate(neuron.weights[:-1])])
                neuronValue    = expit(rawNeuronValue)
                outputs.append(neuronValue)
        return outputs

ipt = np.ones(8*8)
l1_neurons = []
for value in range(8*8):
    l1_neurons.append(neuron(8*8))
hidden = layer(l1_neurons)
output = layer([neuron(8*8)])

net = neuralNet([hidden,output])


print net.update(ipt)


# class networkOrganism(object):
#     """docstring for networkOrganism"""
#     def __init__(self, net):
#         super(networkOrganism, self).__init__()
#         self.genome = []
#         self.get_genome()
#         self.fitness = 0
#         self.get_fitness()
#         def get_genome(self):
#             for layer in net.layers:
#                 for neuron in layer.neurons:
#                     for weight in neuron.weights:
#                         self.genome.append(weight)
#         def get_fitness(self):
#             pass
#
# class genAlg(object):
#     """docstring for genAlg"""
#     def __init__(self, populationSize):
#         super(genAlg, self).__init__()
#         self.arg          = arg
#         self.mutationRate = .05
#         self.generation   = 0
#     def crossover(mom,dad):
#         pass

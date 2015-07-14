import numpy as np
from scipy.special import expit
from scipy.misc import derivative
np.random.seed(1)
class neural_network(object):
    """docstring for neural_network"""
    def __init__(self, layers):
        """
            Layers is an array of numpy arrays
            Each ellement of the numpy arrays represents a neuron
        """
        super(neural_network, self).__init__()
        self.layers    = layers
        self.raw       = layers
        self.numLayers = len(layers)
        self.weights   = {}

        self.initialize_weights()

    def initialize_weights(self):
        for x in range(self.numLayers-1):
            layer1 = self.layers[x]
            layer2 = self.layers[x+1]
            for y1 in range(len(layer1)):
                for y2 in range(len(layer2)):
                    neuron1 = layer1[y1]
                    neuron2 = layer2[y2]
                    self.weights[edge_name(x,x+1,y1,y2)] = np.random.random()-.5

                    # self.weights[edge_name(x,x+1,y1,y2)] = 1

    def update(self,input = None):
        if input != None:
            if len(input) == len(self.layers[0]):
                self.layers[0] = input
            else:
                print("hey! you! yeah you. Your input was the wrong length.")
        for x in range(1,self.numLayers):
            layer1 = self.layers[x-1]
            layer2 = self.layers[x]
            layer2 = np.zeros(layer2.shape)
            for y2 in range(len(layer2)):
                for y1 in range(len(layer1)):
                    layer2[y2] += layer1[y1]*self.weights[edge_name(x-1,x,y1,y2)]
                self.raw[x][y2] = layer2[y2]
                self.layers[x][y2] = expit(layer2[y2])
        print self.layers[-1]

    def train(self,input,desiredOutput):
        """desiredOutput and input should be numpy arrays"""
        self.update(input = input)
        # print self.layers[-1]
        output = self.layers[-1]
        delta = []
        for layer in self.layers:
            delta.append(np.zeros(layer.shape))

        delta[-1]  = desiredOutput-output


        for x in range(self.numLayers-2,0,-1):
            layerPrev    = self.layers[x]
            layerPrev    = np.zeros(layerPrev.shape)
            layerCurrent = self.layers[x+1]

            for y1 in range(len(layerPrev)-1,-1,-1):
                for y2 in range(len(layerCurrent)):
                    layerPrev[y1]+=layerCurrent[y2]*self.weights[edge_name(x,x+1,y1,y2)]
            delta[x] = layerPrev

        for x in range(1,self.numLayers):
            for y1 in range(len(self.layers[x-1])-1,-1,-1):
                for y2 in range(len(self.layers[x])):
                    edge = edge_name(x-1,x,y1,y2)
                    self.weights[edge]+=eta*delta[x][y2]*dSigmoid(self.raw[x][y2])*self.layers[x-1][y1]



eta = 3
#creates a name for an edge that goes from neuron x1,y1 to x2,y2
def edge_name(x1,x2,y1,y2):
    return(str(x1)+str(y1)+','+str(x2)+str(y2))

def dSigmoid(x):
    return np.exp(x)/((np.exp(x)+1)**2)

inputLayer      = np.ones(2)
processingLayer = np.ones(50)
outputLayer     = np.zeros(1)

a = neural_network([inputLayer,processingLayer,outputLayer])



# a.update()

#
# err1 = []
# err2 = []
# err3 = []
# err4 = []
#
for i in range(500):
    # a.update(input = np.array([1,0]))
    # err1.append(1-a.layers[-1])
    # a.update(input = np.array([0,1]))
    # err2.append(1-a.layers[-1])
    # a.update(input = np.array([0,0]))
    # err3.append(a.layers[-1])
    # a.update(input = np.array([1,1]))
    # err4.append(a.layers[-1])

#     print ''
#
#
    a.train(np.array([0,1]),[1])
    a.train(np.array([1,0]),[1])
    a.train(np.zeros(2),[0])
    a.train(np.ones(2),[0])
    print ''
# import matplotlib.pyplot as plt
#
# a.update(input = np.array([1,0]))
# print(a.layers[-1])
# a.update(input = np.array([0,1]))
# print(a.layers[-1])
# a.update(input = np.array([0,0]))
# print(a.layers[-1])
# a.update(input = np.array([1,1]))
# print(a.layers[-1])
#
# plt.plot(err1)
# plt.plot(err2)
# plt.plot(err3)
# plt.plot(err4)
# plt.show()

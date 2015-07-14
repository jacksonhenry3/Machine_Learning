import numpy as np
from scipy.special import expit
from scipy.misc import derivative
class neural_network(object):
    """docstring for neural_network"""
    def __init__(self, layers):
        """
            Layers is an array of numpy arrays
            Each ellement of the numpy arrays represents a neuron
        """
        super(neural_network, self).__init__()
        self.layers    = layers
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
                self.layers[x][y2] = expit(layer2[y2])

    def train(self,input,desiredOutput):
        """desiredOutput and input should be numpy arrays"""
        self.update(input = input)
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
            for y1 in range(len(layerPrev)-1,-1,-1):
                for y2 in range(len(layerCurrent)):
                    edge = edge_name(x-1,x,y1,y2)
                    #This is the part you are still working on!
                    #it should wind up being eta*self.layers[x][y2]*derivative(sigmoid)(x)*y1
                    self.weights[edge]+=eta*self.layers[x][y2]*derivative(expit,)



eta = .1
#creates a name for an edge that goes from neuron x1,y1 to x2,y2
def edge_name(x1,x2,y1,y2):
    return(str(x1)+str(y1)+','+str(x2)+str(y2))


inputLayer      = np.ones(2)
processingLayer = np.ones(2)
outputLayer     = np.zeros(1)

a = neural_network([inputLayer,processingLayer,outputLayer])
a.update()
print a.layers
a.train(np.ones(2),np.zeros(1))
print a.layers
a.update()
print ''
print a.layers[-1]

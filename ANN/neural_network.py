from edge import *
from node import *

class neural_network(object):
    """takes layers as an argument
    Layers is a list of list of nodes
    each sublist is a layer
    the first is an input layer the last is an output layer"""
    def __init__(self, layers):
        super(neural_network, self).__init__()
        self.layers    = layers
        self.numLayers = len(layers)
        self.nodes     = [node for layer in layers for node in layer]
        self.edges     = {}
        self.initialize_edges()

    def get_node_errors(self):
        deltas = [node.delta for layer in self.layers for node in layer]
        return(deltas)
    def get_edge_weights(self):
        deltas = [edge.weight for edge in self.edges.values()]
        return(deltas)

    def feed_forward(self,input = None):
        if input != None:
            self.set_input(input)
        for originX in range(self.numLayers-1):
            terminalX     = originX+1
            originLayer   = self.layers[originX]
            terminalLayer = self.layers[terminalX]
            for terminalY,terminalNode in enumerate(terminalLayer):
                terminalNode.raw = 0
                for originY,originNode in enumerate(originLayer):
                    edgeName = edge_name(originX,originY,terminalX,terminalY)
                    self.edges[edgeName].forward_propogate_val()

                terminalNode.update_val()

    def initialize_edges(self):
        for originX in range(self.numLayers-1):
            terminalX     = originX+1
            originLayer   = self.layers[originX]
            terminalLayer = self.layers[terminalX]
            for originY,originNode in enumerate(originLayer):
                for terminalY,terminalNode in enumerate(terminalLayer):
                    newEdge  = edge(originNode,terminalNode)
                    edgeName = edge_name(originX,originY,terminalX,terminalY)
                    self.edges[edgeName] = newEdge

    def set_input(self,input):
        if len(input) != len(self.layers[0]):
            print "Fool of a Took! your input lengths dont match!"
            return
        for i,node in enumerate(self.layers[0]):
            node.val = input[i]

    def get_output(self):
        output = []
        for node in self.layers[-1]:
            output.append(node.val)
        return output

    def train(self,trainingData,acceptableError = 10):
        """
            training data is a list of the form
            [[[input points],[ output points]],...]
        """
        # while np.mean(np.array(self.get_node_errors())**2) > acceptableError:
        for i in range(50):
            # print self.get_node_errors()
            for example in trainingData:
                self.feed_forward(input = example[0])
                desiredOutput = example[1]
                if len(desiredOutput) != len(self.layers[-1]):
                    print "Output length doesnt match the number of out nodes"
                    return
                for i,node in enumerate(self.layers[-1]):
                    node.delta = desiredOutput[i]-node.val
                for terminalX in range(1,self.numLayers):
                    originX       = terminalX-1
                    originLayer   = self.layers[originX]
                    terminalLayer = self.layers[terminalX]
                    for originY,originNode in enumerate(originLayer):
                        originNode.delta = 0
                        for terminalY,terminalNode in enumerate(terminalLayer):
                            edgeName = edge_name(originX,originY,terminalX,terminalY)
                            self.edges[edgeName].back_propogate_error()
                for edge in self.edges.values():
                    edge.update_weight(eta = 1000-i)


#creates a name for an edge that goes from neuron x1,y1 to x2,y2
def edge_name(x1,y1,x2,y2):
    return(str(x1)+str(y1)+','+str(x2)+str(y2))

def generate_neural_network(numInputs,NumProcessingNodes,numOutputs):
    """ This generates a feed forward neural network with 3 layers """
    inputLayer      = [node() for i in range(numInputs)]
    ProccesingLayer = [node() for i in range(NumProcessingNodes)]
    outputLayer     = [node() for i in range(numOutputs)]
    layers          = [inputLayer,ProccesingLayer,outputLayer]
    return(neural_network(layers))

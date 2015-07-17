from edge import *
from node import *

class neural_network(object):
    """takes layers as an argument
    Layers is a list of list of nodes
    each sublist is a layer
    the first is an input layer the last is an output layer"""
    def __init__(self, layers):
        super(neural_network, self).__init__()

        #this is a list of list of nodes
        self.layers    = layers

        self.numLayers = len(layers)

        #a list of nodes in the network
        self.nodes     = [node for layer in layers for node in layer]

        #initialize the edges with random weights
        self.edges     = {}
        self.initialize_edges()

    def initialize_edges(self):
        #loops through all the edges and assigns random weights
        for originX in range(self.numLayers-1):
            terminalX     = originX+1
            originLayer   = self.layers[originX]
            terminalLayer = self.layers[terminalX]
            for originY,originNode in enumerate(originLayer):
                for terminalY,terminalNode in enumerate(terminalLayer):
                    newEdge  = edge(originNode,terminalNode)
                    edgeName = edge_name(originX,originY,terminalX,terminalY)
                    self.edges[edgeName] = newEdge

    def feed_forward(self,input = None):
        """This function takes the values of the input nodes and feeds them
        forward with the current weights all the way to the output nodes"""
        if input != None:
            self.set_input(input)

        #loop through all the nodes in each layer except the output layer
        for originX in range(self.numLayers-1):
            terminalX     = originX+1
            originLayer   = self.layers[originX]
            terminalLayer = self.layers[terminalX]
            for terminalY,terminalNode in enumerate(terminalLayer):
                terminalNode.raw = 0
                for originY,originNode in enumerate(originLayer):
                    edgeName = edge_name(originX,originY,terminalX,terminalY)

                    #send the value from the origin node to the terminal node
                    self.edges[edgeName].forward_propogate_val()

                #recalcalculate the terminal node value via the sigmoid func
                terminalNode.update_val()

    def set_input(self,input):
        #allows the user to input a list of input value
        #the assigns those as the input node values
        if len(input) != len(self.layers[0]):
            print "Fool of a Took! your input lengths dont match!"
            return
        for i,node in enumerate(self.layers[0]):
            node.val = input[i]

    def get_output(self):
        #returns the output node values as a list
        output = []
        for node in self.layers[-1]:
            output.append(node.val)
        return output

    def train(self,trainingData,acceptableError = .1):
        """
            Teaches the network via backpropgation and gradient decent

            training data is a list of the form
            [[[input points],[ output points]],...]
        """

        #peta is the learning rate, right now it is  linearly related to
        #the error, try out some other functions

        n       = len(trainingData)
        error   = 1
        peta    = 1 #the learning rate
        counter = 0

        #continue untill the error is small enough
        while error > acceptableError:

            #reset the error
            error = 0

            #loop through the training examples
            for example in trainingData:

                #start by feeding the input forward to test the current state
                self.feed_forward(input = example[0])
                desiredOutput = example[1]

                if len(desiredOutput) != len(self.layers[-1]):
                    print "Output length doesnt match the number of out nodes"
                    return

                #calculate how far off the network is for all output nodes
                for i,node in enumerate(self.layers[-1]):
                    node.delta = desiredOutput[i]-node.val

                #Propogate that error backwords through the network
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
                    edge.update_weight(eta = peta)

                #add this training examples error to the total error for this iteration
                error+=np.linalg.norm(self.get_output()-np.array(desiredOutput))\

            #average the error
            error*=1/(2.*n)

            print "iteration "+str(counter)+" completed with a "+str(np.round(error*100,2))+"% error"
            counter+=1
            peta = 5*error

    def show(self):
        pass
        #this method should eventually allow you to display the network via networkx

#creates a name for an edge that goes from neuron x1,y1 to x2,y2
def edge_name(x1,y1,x2,y2):
    return(str(x1)+str(y1)+','+str(x2)+str(y2))

#allows you to more easily generate a network
def generate_neural_network(layerSizes):
    """ This generates a feed forward neural network with 3 layers """
    layers = []
    for layerSize in layerSizes:
        layers.append([node() for i in range(layerSize)])
    return(neural_network(layers))

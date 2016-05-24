import numpy as np
from sys import exit
from scipy.special import expit

class network(object):
    """
    A neural network which can be trained with stochastic gradient decent
        structure : a list with number of neurons in each layer. eg [5,10,7]
        layers    : a list of numpy arrays with the weights between layers
    """

    def __init__(self, structure,layers = None):
        super(network, self).__init__()
        if layers is None:
            #initialize a random network
            self.numLayers = len(structure)
            self.layers = [np.random.randn(structure[i]+1,structure[i+1]) for i in range(len(structure)-1)]
        else:
            #initialize a specified network (to make compatible with genetic algorithms)
            self.numLayers = len(layers)
            self.layers = layers

    def feedForward(self,inputVector):
        """
        Feeds the recieved inputVector through the network to see what the result is. Returns the value of every node in a list of numpy arrays of the same shape as the net.
            inputVector : A numpy array of the same length as the first layer of the network
        """
        values = [inputVector]
        for layer in self.layers:
            # add a one to the input vector to represent the bias
            inputVector = np.append(inputVector,1)

            # print inputVector.shape
            # print layer.shape

            try:
                #propogate forward via a dot product and then take the sigmoid of the value
                inputVector = expit(np.dot(inputVector,layer))
            except ValueError:
                print "Your input vector is the wrong shape! This makes it incompatible with your network."
                print 'The shape of your input vector is '+str(inputVector.shape)+' while the relevant network layer has shape '+str(layer.shape)
                # exit()




            values.append(inputVector)
        return(values)

    def backPropogate(self,deltaVector):
        """
        Feeds the delta vector backwords through the network. Returns the error at every node in a list of numpy arrays in the same shape as the network.
            deltaVector : a numpy array of errors in the shape of the final layer of the network.
        """
        deltaList = [deltaVector]

        #transpose each layer and reverse there order.
        transposedLayersReversed = reversed([np.transpose(layer) for layer in self.layers])

        for transposedLayer in transposedLayersReversed:

            #remove the last value becouse it is the bias.
            deltaVector = np.dot(deltaVector,transposedLayer)[:-1]
            deltaList.append(deltaVector)
        return(deltaList[::-1])

    def reWeightEdges(self,inpt,desiredOutput,eta = 1):
        """
        Changes the weight of all the edges based on the difference between the current output and what the output is supposed to be.
            inpt          : A numpy array of the same shape as the first layer of the network.
            desiredOutput : A numpy array of the same shape as the final layer of the network.
        """
        output = self.feedForward(inpt)
        deltaList = self.backPropogate(desiredOutput-output[-1])
        for i,layer in enumerate(self.layers):
            #add another dimension in the nescesary place for array broadcasting to work
            inpts = np.reshape(np.append(output[i],1),(layer.shape[0],1))
            deriv =  np.reshape(output[i+1]*(1-output[i+1]),(1,layer.shape[1]))
            deltas = np.reshape(deltaList[i+1],(1,layer.shape[1]))

            #this is the actual workhorse. It updates the weights. See
            self.layers[i] = layer+eta*deltas*deriv*inpts
        return(desiredOutput-output[-1])

    def train(self, trainingData, minibatchSize = 10, eta = 1, errorThreshold = .05, maxEpoch = 2000, verbose = False):
        """
            Trains the network using stochatcic gradient desent from training data untill error is less than errorThreshold
                trainingData   : a list of tuples. The first entry in each tuple is the input and the second is the output.
                minibatchSize  : the size of the small training batches. Must divide len(trainingData).
                eta            : learning speed.
                errorThreshold : How low the error must get before termination.
                maxEpoch       : sets a maximum number of iterations in case errorThreshold isn't reached.
                verbose        : If True prints out current error and epoch.
        """
        epoch = 0 #the current epoch
        error = errorThreshold+1 #initialize the error above errorThreshold
        while error > errorThreshold and epoch < maxEpoch:
            epoch+=1
            errorArray = []
            np.random.shuffle(trainingData) #randomizes the order of trainingData
            #Create a list of all the data in each minibatch
            miniBatches = [trainingData[idx:idx+minibatchSize] for idx in range(0, len(trainingData),minibatchSize)]
            for miniBatch in miniBatches:
                for data in miniBatch:
                    #difference between output and epxected oputput
                    currentError = self.reWeightEdges(data[0],data[1],eta = eta)
                    errorArray.append(np.linalg.norm(currentError))
            error = np.mean(errorArray)
            if verbose:
                print "Epoch "+str(epoch)+" completed, mean error "+str(error)

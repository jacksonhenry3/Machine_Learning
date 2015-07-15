from neural_network import *
import matplotlib.pyplot as plt

width = 5
squareDetector = generate_neural_network(width**2,width,1)

trainingData = []
for i in range(5):
    inData = np.floor(np.random.random((width,width))*2)
    # inData = np.zeros((width,width))
    v = 0
    if np.random.randint(2) == 0:
        v = 1
        w = np.random.randint(2,width)
        t = np.random.randint(width-w)
        l = np.random.randint(width-w)
        for x in range(width):
            for y in range(width):
                if l+w>x>l and t+w>y>t:
                    inData[x,y]=1
                if ((x == l+w or x==l)  and (y < t+w and y>t)) or ((y == t+w or y == t) and (x < l+w and x>l)):
                    inData[x,y]=0
    trainingData.append([inData.flatten(),[v]])

squareDetector.train(trainingData)

# print v
# inData[x,y]=1
# for i in range(1):
# inData = np.zeros((width,width))
# w = np.random.randint(width)
# t = np.random.randint(width-w)
# l = np.random.randint(width-w)
# for x in range(width):
#     for y in range(width):
#         if l+w>x>l and t+w>y>t:
#             inData[x,y]=1
# trainingData.append([inData.flatten(),[1]])

succes = 0
for i in range(500):
    inData = np.floor(np.random.random((width,width))*2)
    # inData = np.zeros((width,width))
    v = 0
    if np.random.randint(2) == 0:
        v = 1
        w = np.random.randint(2,width)
        t = np.random.randint(width-w)
        l = np.random.randint(width-w)
        for x in range(width):
            for y in range(width):
                if l+w>x>l and t+w>y>t:
                    inData[x,y]=1
                if x == l+w or x==l or y == t+w or y == t:
                    inData[x,y]=0
    squareDetector.feed_forward(input = inData.flatten())



    out =  squareDetector.get_output()
    out = np.rint(np.array(out))[0]
    if out == v:
        succes+=1
    # if out == 1:
    #     print "this image contains a square"
    # else:
    #     print "this image doesn't contain a square"
    #
    #
    # plt.imshow(inData,interpolation = "none",cmap = "gray")
    # plt.show()
print succes/500.

for i in range(1):
    inData = np.floor(np.random.random((width,wi    def feed_forward(self,input = None):
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
        if len(input) != len(self.ldth))*2)
    # inData = np.zeros((width,width))
    v = 0    def feed_forward(self,input = None):
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
        if len(input) != len(self.l
    if np.random.randint(2) == 0:
        v = 1
        w = np.random.randint(2,width)
        t = np.random.randint(width-w)
        l = np.random.randint(width-w)
        for x in range(width):
            for y in range(width):
                if l+w>x>l and t+w>y>t:
                    inData[x,y]=1
                if x == l+w or x==l or y == t+w or y == t:
                    inData[x,y]=0
    squareDetector.feed_forward(input = inData.flatten())



    out =  squareDetector.get_output()
    out = np.rint(np.array(out))[0]

    if out == 1:
        print "this image contains a square"
    else:
        print "this image doesn't contain a square"


    plt.imshow(inData,interpolation = "none",cmap = "gray")
    plt.show()

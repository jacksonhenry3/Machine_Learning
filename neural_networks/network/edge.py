import numpy as np
# np.random.seed(1)
class edge(object):
    """docstring for edge"""
    def __init__(self,originNode,terminalNode,weight = None):
        super(edge, self).__init__()
        self.weight       = weight
        if weight == None:
            self.weight = np.random.random()-.5
        self.terminalNode = terminalNode
        self.originNode   = originNode

    def update_weight(self,eta = 100):
        #this is the gradient decent implimentation
        self.weight += eta*self.terminalNode.delta*self.terminalNode.deriv*self.originNode.val
        # self.weight -= eta*self.terminalNode.delta*self.terminalNode.deriv*self.originNode.val

    #send the value from edges start node to its end nodes raw sum
    def forward_propogate_val(self):
        self.terminalNode.raw += self.originNode.val*self.weight

    #send the error from edges end node to its start nodes error
    def back_propogate_error(self):
        self.originNode.delta += self.terminalNode.delta*self.weight

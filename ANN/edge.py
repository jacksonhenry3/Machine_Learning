import numpy as np
np.random.seed(1)
class edge(object):
    """docstring for edge"""
    def __init__(self,originNode,terminalNode,weight = None):
        super(edge, self).__init__()
        self.weight       = weight
        if weight == None:
            self.weight = np.random.random()-.5
        self.terminalNode = terminalNode
        self.originNode   = originNode

    def update_weight(self,eta = 10):
        self.weight += eta*self.terminalNode.delta*self.terminalNode.deriv*self.originNode.val

    def forward_propogate_val(self):
        self.terminalNode.raw += self.originNode.val*self.weight

    def back_propogate_error(self):
        self.originNode.delta += self.terminalNode.delta*self.weight

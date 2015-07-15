from scipy.special import expit
class node(object):
    """docstring for node"""
    def __init__(self):
        super(node, self).__init__()
        self.raw   = 0
        self.val   = expit(self.raw)
        self.deriv = self.val*(1-self.val)
        self.delta = 10

    def update_val(self):
        self.val = expit(self.raw)
        self.deriv = self.val*(1-self.val)

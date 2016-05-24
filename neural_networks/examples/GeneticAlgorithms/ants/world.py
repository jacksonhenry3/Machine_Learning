import numpy as np
class world(object):
    """docstring for world"""
    def __init__(self, timestep):
        super(world, self).__init__()
        self.timestep = timestep
        self.foodPositions = (np.random.random((100,2))-.5)*20

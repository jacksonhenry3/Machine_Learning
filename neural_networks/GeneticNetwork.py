import sys
sys.path.insert(0, './network')

from neural_network import *
import matplotlib.pyplot as plt

for i in range(10):
    wts = np.random.random(10)
    generate_neural_network([5,100,length],weights = np.ones(length*100*length))

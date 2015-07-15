from neural_network import *
import matplotlib.pyplot as plt

logicalOperator = generate_neural_network(2,2,1)
trainingData = [[[1,1],[1]],[[1,0],[1]],[[0,1],[1]],[[0,0],[0]]]
Poop = logicalOperator.train(trainingData)
tot = 0
for inpt in trainingData:
    logicalOperator.feed_forward(input = inpt[0])
    # print np.rint(logicalOperator.get_output())
    if np.rint(logicalOperator.get_output())[0] == inpt[1][0]:
        tot+=1

print tot/4.

plt.plot(Poop[:,0])
plt.plot(Poop[:,1])
plt.plot(Poop[:,2])
plt.plot(Poop[:,3])
plt.plot(Poop[:,4])
plt.plot(Poop[:,5])
plt.show()

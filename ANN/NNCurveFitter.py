from neural_network import *
import matplotlib.pyplot as plt


x = np.linspace(-np.pi,np.pi,100)
f = np.sin



NNsqrt = generate_neural_network([1,10,1])

trainingData = []
for i in range(50):
    inpt = (np.random.random()-.5)*2*np.pi
    outpt = f(inpt)
    trainingData.append([[inpt],[outpt]])

# print trainingData
NNsqrt.train(trainingData)

y = []
for i in x:
    NNsqrt.feed_forward([i])
    y.append(NNsqrt.layers[-1][0].raw)
plt.plot(x,y)
plt.plot(x,f(x))
plt.show()

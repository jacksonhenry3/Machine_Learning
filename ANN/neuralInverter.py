from neural_network import *

length = 10
inverter = generate_neural_network(length,length,length)
trainingData = []
for i in range(1):
    inData = np.floor(np.random.random(10)*2)
    outData = np.abs(inData-1)
    trainingData.append([inData,outData])
inverter.train(trainingData)
inverter.feed_forward(np.ones(10))
print np.rint(inverter.get_output())

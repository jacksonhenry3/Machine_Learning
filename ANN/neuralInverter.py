from neural_network import *
import matplotlib.pyplot as plt
acuracy = []

length = 7
inverter = generate_neural_network([length,14,length])
trainingData = []
for i in range(int(2**length/5)):
    out = np.zeros(length)
    inData  = np.floor(np.random.random(length)*2)
    idx = np.sum(inData)-1
    out[idx] = 1
    trainingData.append([inData,out])
inverter.train(trainingData)

tot = 0
for i in range(1000):
    a = np.floor(np.random.random(length)*2)
    b = np.zeros(length)
    idx = np.sum(a)-1
    b[idx] = 1
    inverter.feed_forward(a)
    out = np.rint(inverter.get_output())
    if np.sum(np.abs(b-out))==0:
        tot+=1

print tot/1000.*100

import sys
sys.path.insert(0, '../../../network')
from neuralNetwork import network

import numpy as np
import matplotlib.pyplot as plt

trainingData = []

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
data = np.loadtxt('train.csv',delimiter = ',',dtype = str)[1:][:5]
data[data == ''] = '0'
data[data == 'male'] = '0'
data[data == 'female'] = '1'

data[data == 'C'] = '0'
data[data == 'Q'] = '1'
data[data == 'S'] = '2'
print data[:,11]
for i,d in enumerate(data[:,11]):
    data[:,11][i]=d.replace('C','0')
    data[:,11][i] = d.replace('A','0')
    data[:,11][i] = d.replace('B','0')
    data[:,11][i] = d.replace('C','0')
    data[:,11][i] = d.replace('D','0')
    data[:,11][i] = d.replace('E','0')
    data[:,11][i] = d.replace('F','0')
    data[:,11][i] = d.replace('G','0')

# inData = data[:,[2,5,6,7,8,10]].astype(float)
# inData = data[:,[2,5]].astype(float)
# outData = data[:,1].astype(float)
# trainingData = np.transpose(np.array([inData,outData]))

print data[:,11]
# titanicNet = network([2,1000,1])
#
# titanicNet.train(trainingData,verbose = True,errorThreshold = .25,eta = .00001,minibatchSize = 25)
#
# t = 0
# for n in range(len(inData)):
#     out = np.rint(titanicNet.feedForward(inData[n])[-1])
#     if out == outData[n]:
#         t+=1
#
#
# print str(float(t)/len(inData)*100)[:4]+"% acurate"

#
# testData = np.loadtxt('test.csv',delimiter = ',',dtype = str)[1:]
# testData[testData == ''] = '0'
# testData[testData == 'male'] = '0'
# testData[testData == 'female'] = '1'
#
# testData[testData == 'C'] = '0'
# testData[testData == 'Q'] = '1'
# testData[testData == 'S'] = '2'
#
# inData = testData[:,[1,4,5,6,7,9]].astype(float)
#
# passID = testData[:,0]
# result = []
# for i,inpt in enumerate(inData):
#     o  = np.rint(titanicNet.feedForward(inpt)[-1][0])
#     result.append([passID[i],o])
# result = np.rint(np.array(result).astype(float)).astype(int)
# print result.shape
# np.savetxt('results.csv',result,fmt = '%i',delimiter = ',',header = "PassengerId , Survived")

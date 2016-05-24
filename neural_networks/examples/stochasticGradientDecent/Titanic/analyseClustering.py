import sys


import numpy as np
import matplotlib.pyplot as plt

trainingData = []

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
data = np.loadtxt('train.csv',delimiter = ',',dtype = str)[1:]
data[data == ''] = '0'
data[data == 'male'] = '0'
data[data == 'female'] = '1'

data[data == 'C'] = '0'
data[data == 'Q'] = '1'
data[data == 'S'] = '2'
data[:,10]

data = data[:,[1,2,5,6,7,8,10]].astype(float)
survivedMean = np.mean(data[data[:, 0] == 1],axis=0)[1:]
diedMean = np.mean(data[data[:, 0] == 0],axis=0)[1:]


testData = np.loadtxt('test.csv',delimiter = ',',dtype = str)[1:]
testData[testData == ''] = '0'
testData[testData == 'male'] = '0'
testData[testData == 'female'] = '1'

testData[testData == 'C'] = '0'
testData[testData == 'Q'] = '1'
testData[testData == 'S'] = '2'


passID = testData[:,0]
testData = testData[:,[1,4,5,6,7,9]].astype(float)
result = []
for i,inpt in enumerate(testData):
    if np.linalg.norm(inpt-survivedMean)<np.linalg.norm(inpt-diedMean):
        result.append([passID[i],1])
    else:
        result.append([passID[i],0])
result = np.rint(np.array(result).astype(float)).astype(int)
print result.shape
np.savetxt('resultsClustering.csv',result,fmt = '%i',delimiter = ',',header = "PassengerId , Survived")

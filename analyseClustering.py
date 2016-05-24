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


data = data[:,[1,2,5,6,7,8,10]].astype(float)
print np.mean(data[data[:, 0] == 1],axis=0)

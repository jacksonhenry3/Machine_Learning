import sys


import numpy as np
import matplotlib.pyplot as plt

trainingData = []

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
data = np.loadtxt('train.csv',delimiter = ',',dtype = str)[1:]
#
# data = data[:,5].astype(float)
#


# data = np.loadtxt('test.csv',delimiter = ',',dtype = str)[1:]


passID = data[:,0]
gender = data[:,5]
result = []
t=0
for i,inpt in enumerate(data):
    if gender[i] == 'female':
        survived = 1
    else:
        survived = 0
    if survived ==int(data[:,1][i]):
        t+=1
    result.append([passID[i],survived])
result = np.rint(np.array(result).astype(float)).astype(int)
print result.shape
print float(t)/len(data)
np.savetxt('resultsGender.csv',result,fmt = '%i',delimiter = ',',header = "PassengerId , Survived")

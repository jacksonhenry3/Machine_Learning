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

data =  data[:,[2,5,6,7,8,10,1]].astype(float)
class split(object):
    def __init__(self, data,n):
        super(split, self).__init__()
        self.data = data
        self.axis = np.random.randint(6)
        self.split = self.get_split()
        self.lessData = []
        self.greaterData = []
        self.lessClass = np.zeros(n)
        self.greaterClass = np.zeros(n)
        self.create_classification()

    def get_split(self):
        mx = np.max(self.data[:,self.axis])
        mn = np.min(self.data[:,self.axis])
        return((np.random.random()*(mx-mn)+mn))

    def create_classification(self):
        for data in self.data:
            if data[self.axis]<self.split:
                self.lessData.append(data)
                self.lessClass[int(data[-1])]+=1
            else:
                self.greaterData.append(data)
                self.greaterClass[int(data[-1])]+=1

    def vote(self,pnt):
        if pnt[self.axis]<self.split:
            return(self.lessClass)
        else:
            return(self.greaterClass)
t=0
for i in range(10):
    idx = np.random.randint(len(data))
    testPnt = data[idx][:-1]
    votes = np.zeros(2)
    for i in range(20000):
        np.random.shuffle(data)
        data_subset = data[:13]
        a = split(data_subset,2)
        votes+= a.vote(testPnt)

    if np.argmax(votes) == int(testPnt[1]):
        t+=1
print t*10

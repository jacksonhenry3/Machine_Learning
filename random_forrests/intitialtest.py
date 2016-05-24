import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('Data',skiprows = 1,dtype = 'str')
x = data[:,0].astype(float)
y = data[:,1].astype(float)
C = data[:,2]
C[C == 'apartment'] = '0'
C[C == 'house'] = '1'
C[C == 'flat'] = '2'
C = C.astype(float)

data = np.transpose(np.array([x,y,C]))







class split(object):
    def __init__(self, data,n):
        super(split, self).__init__()
        self.data = data
        self.axis = np.random.randint(2)
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
for i in range(100):
    idx = np.random.randint(len(data))
    testPnt = [x[idx],y[idx],C[idx]]
    votes = np.zeros(3)
    for i in range(100):
        np.random.shuffle(data)
        data_subset = data[:13]
        a = split(data_subset,3)
        votes+= a.vote(testPnt)
    if np.argmax(votes) == int(testPnt[-1]):
        t+=1
print t

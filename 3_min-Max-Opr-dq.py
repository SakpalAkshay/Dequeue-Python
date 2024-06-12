from collections import deque

class MyDq:
    def __init__(self):
        self.dq = deque()
    
    def insertMin(self,x):
        self.dq.appendleft(x)
    
    def insertMax(self,x):
        self.dq.append(x)

    def getMin(self):
        return self.dq[0]
    
    def getMax(self):
        return self.dq[-1]

    def extractMin(self):
        return self.dq.popleft()
    
    def extractMax(self):
        return self.dq.pop()
    
    def getDq(self):
        return self.dq

mydq = MyDq()
mydq.insertMin(1)
mydq.insertMax(20)
mydq.insertMax(45)
mydq.insertMin(0)

print(mydq.getMin())
print(mydq.getMax())

min = mydq.extractMin()
max = mydq.extractMax()
print(min,max)

getdq = mydq.getDq()
print(getdq)
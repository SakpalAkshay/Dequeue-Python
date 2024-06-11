#understanding Dequeue in Python

from collections import deque

dq = deque() #creates an Empty deque
dq.append(10) #Add element to the Rear End
print(dq) # => deque([10])
dq.appendleft(20) # adds element to the front
print(dq) # => deque([20, 10])
dq.append(30)
dq.append(40)
dq.append(50)
print(dq) # => deque([20, 10, 30, 40, 50])
dq.pop() #removes element from Rear
print(dq) # => deque([20, 10, 30, 40])
dq.popleft() #removes element from the Front
print(dq) # => deque([10, 30, 40])

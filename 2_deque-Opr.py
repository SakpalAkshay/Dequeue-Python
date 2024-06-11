from collections import deque

dq = deque([1,2,4,5,6,7]) # => Deque from a List

print(dq[0]) # => Access first element 1
print(dq[-1]) # => Access last element 7

dq.insert(2,10) # => Insert 10 at 2nd Index  deque([1, 2, 10, 4, 5, 6, 7])
print(dq)
dq.remove(5) # =>  removes element deque([1, 2, 10, 4, 6, 7])
print(dq)
dq.extendleft([10,20]) # => Add list to Start of deque 
dq.extend([50,60]) #=> Add list to the rear end 
print(dq)  # deque([20, 10, 1, 2, 10, 4, 6, 7, 50, 60])

dq.append(20)
print(dq)  # deque([20, 10, 1, 2, 10, 4, 6, 7, 50, 60, 20])
print(dq.count(20)) # => Count the Number of times an element appeared  2


dq.rotate(2) #=> Clockwise rotation of 2 elements
print(dq) # deque([60, 20, 20, 10, 1, 2, 10, 4, 6, 7, 50])
dq.rotate(-3) # => Counterclockwise rotation of 3 elements
print(dq) # deque([10, 1, 2, 10, 4, 6, 7, 50, 60, 20, 20])


#Note Deque doesnt support Slicing like List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class MyDq():
    def __init__(self):
        self.front = None
        self.rear = None
        self.sz = 0
    
    def size(self):
        return self.sz
    
    def isEmpty(self):
        return self.sz == 0

    def insertFront(self,x):
        #Now lets create a Node firt
        node = Node(x)

        #check if DQ is empty
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.front.prev = node
            node.next = self.front
            self.front = node
        self.sz +=1
    
    def insertRear(self,x):
        # lets create a Node
        node = Node(x)
        #checking for empty deque
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            node.prev = self.rear
            self.rear.next = node
            self.rear = node
        self.sz +=1
    
    def deleteFront(self):

        #check if Deque is Empty
        if self.isEmpty():
            return -1
        else:
            temp = self.front
            self.front = self.front.next
            # what if there was only one Element
            if self.front is None:
                self.rear = None
            else:
                self.front.prev = None
            self.sz -=1
            #removing connection of Prev node is existed
            temp.next = None
            return temp.data

    def deleteRear(self):

        if self.isEmpty():
            return -1
        else:
            temp = self.rear
            self.rear = self.rear.prev

            if self.rear is None:
                self.front = None
            else:
                self.rear.next = None
            self.sz -=1
            # Ensure temp node doesn't retain pointers
            temp.prev = None
            return temp.data



            
    

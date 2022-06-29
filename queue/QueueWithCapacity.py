
import re
from sys import maxsize


class Queue:
    def __init__(self, maxSize):
        self.items = maxSize *[None]
        self.maxSize = maxSize
        self.top = -1
        self.start = -1
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and  self.top + 1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        return self.top == -1
        
    def enqueue(self, value):
        if self.isFull():
            return "there is no more space to enqueue element"
        if self.top + 1 == self.maxSize:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return "the element is inserted at the end of the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "there is not any element to dequeue"
        first_element = self.items[self.start]
        start = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.maxSize:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element
    
    def peek(self):
        if self.isEmpty():
            return "there is not any element in the queue"
        return self.items[self.start]
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1
    
customeQueue = Queue(4)
customeQueue.enqueue(10)
customeQueue.enqueue(11)
customeQueue.enqueue(12)
customeQueue.enqueue(13)
customeQueue.enqueue(14)

print(customeQueue)

customeQueue.dequeue()
customeQueue.dequeue()

print(customeQueue)
print(customeQueue.delete())
print(customeQueue.peek())
print(customeQueue)

print(customeQueue.isFull())
print(customeQueue.isEmpty())
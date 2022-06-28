from calendar import c
import re


class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, value):
        self.items.append(value)
        return "The element is added to the queue successfully"
    
    def dequeue(self):
        if self.isEmpty():
            return "there is no element in the queue"
        else:
            return self.items.pop(0)
        
    def peek(self):
        if self.isEmpty():
            return "there is no element in the queue"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
    


customeQueue = Queue()
customeQueue.enqueue(10)
customeQueue.enqueue(11)
customeQueue.enqueue(12)
customeQueue.enqueue(13)
customeQueue.enqueue(14)    
customeQueue.enqueue(15)
print(customeQueue)
customeQueue.dequeue()
print(customeQueue)
print(customeQueue.peek())
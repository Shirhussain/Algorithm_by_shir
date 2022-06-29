# empyt one stace in a queue order and added to another empyt stack then remove and bring back to the original stack
from calendar import c


class Stack:
    def __init__(self):
        self.list = []
        
    def __len__(self):
        return len(self.list)
    
    def push(self, value):
        return self.list.append(value)
    
    def pop(self):
        return None if len(self.list) == 0 else self.list.pop()
    

class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
        
    def enqueue(self, value):
        self.inStack.push(value)
        
    def dequeue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

custome_queue = QueueViaStack()
custome_queue.enqueue(1)
custome_queue.enqueue(2)
custome_queue.enqueue(3)
custome_queue.enqueue(4)
print(custome_queue.dequeue())
custome_queue.enqueue(5)
print(custome_queue.dequeue())
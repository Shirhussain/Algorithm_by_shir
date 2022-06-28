
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self):
        values = sorted(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        return self.list == []
    
    
    def isFull(self):
        return len(self.list) == self.maxSize 
    
    def push(self, value):
        if self.isFull():
            return "The stack is full.\n"
        else:
            self.list.append(value)
            print("the element is added to the stack successfully.\n")
        
    def pop(self):
        if self.isEmpty():
            return "there is no element in the stack.\n"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "there is no element in the stack.\n"
        else:
            return self.list[len(self.list) - 1]
        
    def delete(self):
        self.list = None
        

custome_stack = Stack(5)
print(custome_stack.isEmpty())
print(custome_stack.isFull())

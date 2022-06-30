#just do it
class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        return self.list == []
    
    def push(self, value):
        self.list.append(value)
        return "The element successfully pushed to the stack"
    
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[len(self.list) - 1]
    
    def delete(self):
        self.list = None


custome_stack = Stack()
custome_stack.push(1)
custome_stack.push(2)
custome_stack.push(3)
custome_stack.push(4)
custome_stack.pop()
print(custome_stack.peek())
print(custome_stack)

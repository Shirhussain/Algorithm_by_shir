# return the minimum value

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
        
    def __str__(self) -> str:
        if string := str(self.value):
            string += f',{str(self.next)}'
            return string
        
class Stack:
    def __init__(self):
        self.top = None
        self.min_Node = None
        
    def min(self):
        return self.min_Node.value if self.min_Node else None
    
    def push(self, item):
        if self.min_Node and self.min_Node.value < item:
            self.min_Node = Node(value = self.min_Node.value, next = self.min_Node)
        else:
            self.min_Node = Node(value = item, next = self.min_Node)
        self.top  = Node(value = item, next = self.top)
    
    def pop(self):
        if not self.top:
            return None
        self.min_Node = self.min_Node.next
        item = self.top.value
        self.top = self.top.next
        return item
    

custome_stack = Stack()
custome_stack.push(7)
custome_stack.push(8)
custome_stack.push(2)
custome_stack.push(1)
custome_stack.pop()
print(custome_stack.min())

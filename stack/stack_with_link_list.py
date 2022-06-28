import re


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


class Stack:
    def __init__(self):
        self.link = LinkedList()
        
    def __str__(self):
        values = [str(x.value) for x in self.link]
        return '\n'.join(values)
        
    def isEmpty(self):
        return self.link.head is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.link.head
        self.link.head = new_node
    
    def pop(self):
        if self.isEmpty():
            return "there is no element in the stack"
        node_value = self.link.head.value
        self.link.head = self.link.head.next
        return node_value
    
    def peek(self):
        if self.isEmpty():
            return "there is no element in the stack"
        return self.link.head.value
    
    def delete(self):
        self.link.head = None
        
custome_stack = Stack()
print(custome_stack.isEmpty())
custome_stack.push(10)
custome_stack.push(11)
custome_stack.push(12)
custome_stack.push(13)
# custome_stack.pop()
print(custome_stack)
print("---------")
print(custome_stack.peek())
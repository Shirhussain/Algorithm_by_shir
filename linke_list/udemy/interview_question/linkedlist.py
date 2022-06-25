from tkinter import Y


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
            
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)


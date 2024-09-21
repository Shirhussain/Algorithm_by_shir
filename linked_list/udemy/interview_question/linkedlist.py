from random import randint

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self, values = None):
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

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result
    
    def add(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self, number_of_node, min_value, max_value):
        self.head = None
        self.tail = None
        for _ in range(number_of_node):
            self.add(randint(min_value, max_value))
        return self
    
    
# custome_link_list = LinkedList()
# custome_link_list.generate(10,0,100)
# print(custome_link_list)
# print(len(custome_link_list))
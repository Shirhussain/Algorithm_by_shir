from tempfile import tempdir


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        

class CircularDoublyLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createCDLL(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        return "CDLL is created successfully"
    
    def insert(self, new_value, location):
        if self.head is None:
            print("the circular doubly linked list doese not exist")
        else:
            new_node = Node(new_value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            return "The node has been successfully inserted into the circular doubly linked list"
    
    def traversalDLL(self):
        if self.head is None:
            print("The node doese not exist in the circular doubly linked list")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                if temp_node == self.tail:
                    break
                temp_node = temp_node.next
    
    def reverseTraversal(self):
        if self.head is None:
            print("There is not any node in circular doubly linked list")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                if temp_node == self.head:
                    break
                temp_node = temp_node.prev
                

    def search(self, node_value):
        if self.head is None:
            print("No head found")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                if temp_node == self.tail:
                    return "the value does not exist in the node"
                temp_node = temp_node.next
        
    def delete(self, location):
        if self.head is None:
            print("head is not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.tail.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
            else:
                current_node = self.head
                index = 0
                while index < location -1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print("the node has been successfully deleted")
            
    def deleteEnitreCDLL(self):
        if self.head is None:
            print("there is no element exist")
        else:
            self.tail.next = None
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The CircularDoublyLinkList is delete successfully")
            
            
cdll = CircularDoublyLinkList()
print(cdll.createCDLL(100))
print(cdll.insert(12,0))
print(cdll.insert(1,-1))
print(cdll.insert(2,-1))
print(cdll.insert(32,3))
print(cdll.insert(20,2))

cdll.traversalDLL()
cdll.reverseTraversal()
# cdll.delete(0)
cdll.delete(-1)
# cdll.delete(2)
print(cdll.search(100))

cdll.deleteEnitreCDLL()
print([node.value for node in cdll])

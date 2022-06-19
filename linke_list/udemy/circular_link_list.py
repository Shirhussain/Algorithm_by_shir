
from hashlib import new
from tempfile import tempdir


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        

class Circular_singly_link_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node :
            yield node
            node = node.next
            if node == self.tail.next:
                break 

    # Creattion of Circular_singly_link_list
    def createCSLL(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular_singly_link_list has been created"
    
    def insertCSLL(self, node_value, location):
        if self.head is None:
            print("The head refreance is not available")
        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            return "The insertion hass been successfully completed."
        
    def traverseCSLL(self):
        if self.head is None:
            print("ther is not any element for travsersal")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    break
                
    def searchCSLL(self, node_value):
        if self.head is None:
            print("ther is not any node in this linked list")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == node_value:
                    return temp_node.value
                temp_node = temp_node.next
                if temp_node == self.tail.next:
                    return "The node does not exist in the linked list"
                
    def deleteCSLL(self, location):
        if self.head is None:
            print("the link list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None 
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next 
        
    def delete_EntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        

csll = Circular_singly_link_list()
csll.createCSLL(2)
csll.insertCSLL(0,0)
csll.insertCSLL(2,1)
csll.insertCSLL(3,1)
csll.insertCSLL(2,1)
csll.insertCSLL(3,1)
csll.insertCSLL(4,2)
csll.insertCSLL(10,-1)


print([node.value for node in csll])
# csll.traverseCSLL()

# print(csll.searchCSLL(10))
csll.deleteCSLL(0)
csll.deleteCSLL(-1)
csll.deleteCSLL(2)

csll.delete_EntireCSLL()

print([node.value for node in csll])

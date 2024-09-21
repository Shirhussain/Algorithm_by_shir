
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self, node_value):
        node = Node(node_value)
        self.head = node
        self.tail = node
        self.prev = None
        self.next = None
        return "The dubully linked list created successfully"
    
    def insertNode(self, node_value, location):
        if self.head is None:
            print("Then node can not be inserted first you should created")
        else:
            new_node = Node(node_value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = None
                self.head.prev = new_node
                self.head = new_node
            # insert at the end
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail
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
                
    def traverseDll(self):
        if self.head is None:
            print("there is no node to traverse")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.next
        
    
    def revrseTraverseal(self):
        if self.head is None:
            print("there is no any element to traverse")
        else:
            temp_node = self.tail
            while temp_node:
                print(temp_node.value)
                temp_node = temp_node.prev
    
    def search(self, nodeValue):
        if self.head is None:
            print("there is not any node")
        else:
            temp_node = self.head
            while temp_node:
                if temp_node.value == nodeValue:
                    return temp_node.value
                temp_node = temp_node.next
            return "There is not anything found"
        
    def deleteNode(self, location):
        if self.head is None:
            print("There is no node exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.taill = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current_node = self.head
                index = 0
                while index < location -1:
                    current_node = current_node.next
                    index =+ 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            print("node has been delete it successfully")
            
    def deleteEntireDLL(self):
        if self.head is None:
            print("There is no element int the node")
        else:
            temp_node = self.head
            while temp_node:
                # becase it's dubbley linked list so we have to delete the previoius refrance before head and tail to be none
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None
            print("The Entire node has been successfully deleted")
        
                
                    
            

dll = DoublyLinkedList()
dll.createDLL("50")

print([node.value for node in dll])

dll.insertNode(0,0)
dll.insertNode(10,-1)
dll.insertNode(1,1)
dll.insertNode(3,2)
dll.insertNode(4,3)
print([node.value for node in dll])

# dll.traverseDll()
# dll.revrseTraverseal()

print(dll.search(300))

dll.deleteNode(0)
# dll.deleteNode(-1)
# dll.deleteNode(1)
dll.deleteEntireDLL()
print([node.value for node in dll])


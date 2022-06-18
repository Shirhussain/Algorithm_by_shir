# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next
    
#     def insertSLL(self, value, location):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             if location == 0:
#                 new_node.next = self.head
#                 self.head = new_node
#             elif location == -1:
#                 new_node.next = None
#                 self.tail.next = new_node
#                 self.tail = new_node
#             else:
#                 temp_node = self.head
#                 index = 0
#                 while index < location -1:
#                     temp_node = temp_node.next
#                     index += 1
#                 next_node = temp_node.next
#                 temp_node.next = new_node
#                 new_node.next = next_node
#                 if temp_node == self.tail:
#                     self.tail = new_node

# singleLL = SinglyLinkedList()
# singleLL.insertSLL(1,1)
# singleLL.insertSLL(2,1)
# singleLL.insertSLL(3,1)
# singleLL.insertSLL(4,1)
# singleLL.insertSLL(0,0)
# singleLL.insertSLL(0,3)
# print([node.value for node in singleLL])

from re import T


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self,value, location):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
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
                if temp_node == new_node:
                    self.tail = new_node
                    
                    
    def traverseSLL(self):
        # traverse throw the linklist
        if self.head is None:
            print("Ths singlyLinkList does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self, node_value):
        if self.head is None:
            return "The singlyLinkList does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return "The value dose not exist in the lsit"  
        
    def delete_node(self, location):
        if self.head is None:
            print("The singlyLinkList does not exist")
        else:
            if location == 0:
                # check if the list have only one element, it means that head and tail are one node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # it means that delte first node and connect to the next node
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # otherwise we have to traverse the list tail reach the end
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            
            else:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
                
    def deleteEntireSLL(self):
        if self.head is None:
            print("The link does not exist")
        else:
            # all you need to do to delte entire link is to assign head and teail to None
            # the garbage collector will delete nodes
            self.head = None
            self.tail = None
            

sll = SinglyLinkedList()
sll.insert(1,1)
sll.insert(2,1)
sll.insert(3,1)
sll.insert(10,2)
sll.insert(11,2)
sll.insert(100,2)


print([node.value for node in sll])

# sll.traverseSLL()
# print(sll.searchSLL(10))
# sll.delete_node(2)

sll.deleteEntireSLL()

print([node.value for node in sll])



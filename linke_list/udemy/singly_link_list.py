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

sll = SinglyLinkedList()
sll.insert(1,1)
sll.insert(2,1)
sll.insert(3,1)
sll.insert(10,2)


print([node.value for node in sll])
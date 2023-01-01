# Singly Linked List - Set

# Implement the following on the SinglyLinkedList class:

# Set

# This function should accept an index and a value and update the value of the node in the SinglyLinkedList at the index with new value. It should return true if the node is updated successfully or false if an invalid index is passed in.

# Examples

# (Note: you do not need to re-implement push, the test will be provided with it)

#     singlyLinkedList = SinglyLinkedList()
#     singlyLinkedList.push(1)
#     singlyLinkedList.push(2)
#      
#     singlyLinkedList.set(0,10)  # True
#     singlyLinkedList.set(1,20)  # True
#     singlyLinkedList.length    # 2
#     singlyLinkedList.head.val  # 10
#      
#     singlyLinkedList.set(10,10) # False
#     singlyLinkedList.set(2,100) # False
#      
#     singlyLinkedList.head.next.val # 20
#      
#      

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False

        node = self.head
        for _ in range(index):
            node = node.next
        node.value = value
        return True


sll = LinkedList()
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
sll.set(0, 10)
sll.set(10, 10)

print([node.value for node in sll])


# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next

#     def push(self, data):
#         node = Node(data)
#         if self.head == None:
#             self.head = node
#         else:
#             self.tail.next = node
#         self.tail = node
#         self.length += 1
#         return "Success"

#     def set(self, index, value):
#         if self.head is None:
#             self.head = Node(value)
#             self.tail = Node(value)
#         else:
#             currentNode = self.head
#             for i in range(index):
#                 currentNode = currentNode.next

#                 if currentNode == None:
#                     return False
#             currentNode.val = value
#         return True


# sll = SinglyLinkedList()

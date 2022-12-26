# Singly Linked List - Push

# Implement the following on the SinglyLinkedList class:

# push

# This function should take in a value and add o node to the end of the SinglyLinkedList. It should return the SinglyLinkedList.

# Examples

#     singlyLinkedList = SinglyLinkedList()
#     singlyLinkedList.push(5)  # Success
#     singlyLinkedList.length   # 1
#     singlyLinkedList.head.val # 5
#     singlyLinkedList.tail.val # 5
#      
#     singlyLinkedList.push(10)    # Success
#     singlyLinkedList.length      # 2
#     singlyLinkedList.head.val    # 5
#     singlyLinkedList.head.next.val  # 10
#     singlyLinkedList.tail.val    # 10

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return "Success"


SLL = SinglyLinkedList()
SLL.push(5)
print(SLL.length)
print(SLL.head.value)
print(SLL.tail.value)
SLL.push(100)
print(SLL.head.next.value)
print(SLL.length)

print([node.value for node in SLL])

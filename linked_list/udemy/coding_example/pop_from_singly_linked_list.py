# Singly Linked List - Pop

# Implement the following on the SinglyLinkedList class:

# pop

# This function should remove a node at the end of the SinglyLinkedList. It should return the node removed.

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
#      
#      
#     singlyLinkedList.pop().val # 10
#     singlyLinkedList.tail.val  # 5
#     singlyLinkedList.length    # 1
#     singlyLinkedList.pop().val # 5
#     singlyLinkedList.length    # 0
#     singlyLinkedList.pop()     # Undefined

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Singly_Linked_List:
    def __init__(self) -> None:
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
        return "Success"

    def pop(self):
        if self.head is None:
            return "Undefined"
        if self.head == self.tail:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        temp_node = self.head
        while temp_node.next != self.tail:
            temp_node = temp_node.next

        popped_node = self.tail
        self.tail = temp_node
        self.tail.next = None
        self.length -= 1
        return popped_node


sll = Singly_Linked_List()
sll.push(5)
sll.push(11)
sll.push(20)

print(sll.head.value)
print(sll.tail.value)
print(sll.length)

print([node.value for node in sll])

print(sll.pop().value)

print([node.value for node in sll])

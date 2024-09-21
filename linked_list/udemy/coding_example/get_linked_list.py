# Singly Linked List - Get

# Implement the following on the SinglyLinkedList class:

# get

# This function should find a node at a specified index in a  SinglyLinkedList. It should return the found node.

# Examples

#     singlyLinkedList = SinglyLinkedList()
#     singlyLinkedList.push(5)  # Success
#     singlyLinkedList.push(10)  # Success
#     singlyLinkedList.push(15)  # Success
#     singlyLinkedList.push(20)  # Success
#      
#      
#     singlyLinkedList.get(0).val    # 5
#     singlyLinkedList.get(1).val    # 10
#     singlyLinkedList.get(2).val    # 15
#     singlyLinkedList.get(3).val    # 20
#     singlyLinkedList.get(4).val    # None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length or self.head is None:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


sll = Linked_list()
sll.push(10)
sll.push(20)
sll.push(30)

print([node.value for node in sll])

print(sll.get(2).value)

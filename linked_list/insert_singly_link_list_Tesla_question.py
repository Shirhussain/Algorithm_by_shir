my_list = [10, 20, 30, 40, 50]
# how to insert at the end of this list

# Write a program to insert a new node at the end of the singly linked list
# Linked List [10, 20, 30, 40, 50]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLingList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSinglyLinkList(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = None
        self.tail.next = new_node
        self.next = new_node


my_list = [10, 20, 30, 40, 50]

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

SLL = SLingList()
SLL.head = node1
SLL.head.next = node2
SLL.head.next.next = node3
SLL.head.next.next.next = node4
SLL.head.next.next.next.next = node5
# SLL.head.next.next.next = node4
SLL.tail = node5


SLL.insertSinglyLinkList(60)

print([node.value for node in SLL])

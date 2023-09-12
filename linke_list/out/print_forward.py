""" 
    print forward linked list
"""


class LinkListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        new_node = LinkListNode(node)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


lst = [1, 5, 7, 10]

sll = SinglyLinkedList()
for i in lst:
    sll.insert(i)

sll.display()

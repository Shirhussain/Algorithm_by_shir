# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class SLinkList:
#     def __init__(self):
#         self.head = None
#         self.tail = None


# singleLinkList = SLinkList()

# node1 = Node(1)
# node2 = Node(2)

# singleLinkList.head = node1
# singleLinkList.head.next = node2
# singleLinkList.tail = node2


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

SLL = SinglyLinkedList()
SLL.head = node1
SLL.head.next = node2
SLL.tail = node2

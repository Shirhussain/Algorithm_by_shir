from cmath import sin


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLinkList:
    def __init__(self):
        self.head = None
        self.tail = None


singleLinkList = SLinkList()

node1 = Node(1)
node2 = Node(2)

singleLinkList.head = node1
singleLinkList.head.next = node2
singleLinkList.tail = node2

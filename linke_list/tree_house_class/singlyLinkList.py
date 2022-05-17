class Node:
    def __init__(self, value):
        self.value = value
        self.node = None

    def __repr__(self):
        return f"This is node value: {self.value}"

n1 = Node(10)
print(n1)


class LinkList:
    def __init__(self):
        self.head = None

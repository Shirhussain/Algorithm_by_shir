class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, new_node):
        node = Node(new_node)
        if self.value is None:
            self.value = node

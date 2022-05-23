class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Circular_singly_link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.head:
                break

    def create_c_l_l(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular singly link_list has been created"
    

sll = Circular_singly_link_list()
sll.create_c_l_l(2)

print([node.value for node in sll])


    
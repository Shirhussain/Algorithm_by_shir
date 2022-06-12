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
            if node == self.tail.next:
                break

    def create_c_l_l(self, node_value):
        node = Node(node_value)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular singly link_list has been created"
    
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head refreance is None"
        else:
            new_node = Node(value)
            if location == 0:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
            elif location == -1:
                new_node.next = self.tail.next
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location-1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            return "Node has been successfully inserted"
sll = Circular_singly_link_list()
sll.create_c_l_l(2)
sll.insertCSLL(0,0)
sll.insertCSLL(1,1)
sll.insertCSLL(2,1)
sll.insertCSLL(3,1)
sll.insertCSLL(2,2)


print([node.value for node in sll])


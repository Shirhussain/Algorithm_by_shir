class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def reverse_link_list(self):
        prev = None
        curr = self.head

        while curr:
            # we need to have a reference to catch up
            ref = curr.next
            curr.next = prev
            prev = curr
            curr = ref

        self.head = prev
        return self.head

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next


lst = [1, 3, 5, 7, 10]

sll = SinglyLinkedList()
for i in lst:
    sll.insert(i)
sll.reverse_link_list()
sll.display()

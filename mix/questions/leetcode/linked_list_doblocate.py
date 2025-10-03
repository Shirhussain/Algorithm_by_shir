class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add_node(self, node):
        new_node = Node(node)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def remove_duplicates(self):
        temp = self.head
        while temp:
            if temp.next and temp.next.value == temp.value:
                temp.next = temp.next.next
            else:
                temp = temp.next

        for node in self:
            print(node.value)
        return self.head


link = LinkedList()
link.add_node(1)
link.add_node(1)
link.add_node(2)
link.add_node(3)
link.add_node(3)
link.add_node(3)
print([l.value for l in link])

print("Original linked list:")
for node in link:
    print(node.value)

link.remove_duplicates()
print("Removed duplicates:")
for node in link:
    print(node.value)

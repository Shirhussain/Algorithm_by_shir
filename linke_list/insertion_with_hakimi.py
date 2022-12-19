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

    def insert(self, val, pos=-1):
        temp = self.head
        new_node = Node(val)

        if not temp:
            self.head = new_node
            return

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        if pos == -1:
            while temp.next:
                temp = temp.next

        for i in range(pos-1):
            if temp.next:
                temp = temp.next

        next_node = temp.next
        temp.next = new_node
        new_node.next = next_node


def delete(self, pos):
    temp = self.head

    if self.head is None:
        raise Exception('Out of range')

    if pos == 0:
        self.head = temp.next
        return

    if pos == -1:
        while temp.next.next:
            temp = temp.next

    for i in range(pos-1):
        if temp.next:
            temp = temp.next

    if not temp.next:
        raise Exception('Out of range')
    temp.next = temp.next.next

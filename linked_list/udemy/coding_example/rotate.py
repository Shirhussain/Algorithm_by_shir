class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def rotate(self, number):
        index = (number + self.length) if number < 0 else number
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return "No Rotation"
        prevNode = self.head
        for i in range(index-1):
            prevNode = prevNode.next
        if prevNode == None:
            return "No Rotation"
        self.tail.next = self.head
        self.head = prevNode.next
        self.tail = prevNode
        prevNode.next = None
        return "Success"


sll = SingleLinkedList()
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
sll.push(5)

sll.rotate(-1)


print([node.value for node in sll])

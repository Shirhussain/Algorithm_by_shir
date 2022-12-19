class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLingList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSiglyLinkList(self, location, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.next = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def search(self, data):
        if self.head is None:
            return "The node does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == data:
                    return node.value
                else:
                    return "the value does not exist on the list"

    def traverseLList(self):
        if self.head is None:
            print("The singlyLinkList does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


singleLL = SLingList()
singleLL.insertSiglyLinkList(1, 1)
singleLL.insertSiglyLinkList(2, 1)
singleLL.insertSiglyLinkList(3, 1)
singleLL.insertSiglyLinkList(4, 1)

print([node.value for node in singleLL])

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
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

    def display_backward_recursive(self):
        node = self.head

        def helper(curr):
            if curr is None:
                return
            helper(curr.next)
            print(curr.data)

        helper(node)

    def display_backward_arr(self):
        node = self.head
        curr = node
        result = []

        while curr:
            result.append(curr.data)
            curr = curr.next

        for i in range(len(result)-1, -1, -1):
            print(result[i])


lst = [1, 5, 7, 10]

sll = LinkedList()
for i in lst:
    sll.insert(i)

sll.display_backward_recursive()
sll.display_backward_arr()

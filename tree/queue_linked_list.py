class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self) -> str:
        values = [str(x) for x in self.linked_list]
        return ' '.join(values)

    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def isEmpty(self):
        return self.linked_list.head is None

    def dequeue(self):
        if self.isEmpty():
            return "there is no element in the queue"
        temp_node = self.linked_list.head
        if self.linked_list.head == self.linked_list.tail:
            self.linked_list.head = None
            self.linked_list.tail = None
        else:
            self.linked_list.head = self.linked_list.head.next
        return temp_node

    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        return self.linked_list.head

    def delete(self):
        self.linked_list.head = None
        self.linked_list.tail = None


customeQueue = Queue()
customeQueue.enqueue(10)
customeQueue.enqueue(11)
customeQueue.enqueue(12)
customeQueue.enqueue(13)
print(customeQueue)

# print(customeQueue.peek())

customeQueue.dequeue()
print(customeQueue)

customeQueue.dequeue()
customeQueue.delete()
print(customeQueue)

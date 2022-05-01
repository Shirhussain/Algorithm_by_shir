class Node:
    """
    An object for sorting a single node of a linked list.
    Models two attributes - data and link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"information of Node data is {self.data}"


class LinkedList:
    """
    Singly Linked list
    """

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        """
        return the number of node in the list 
        which take Linear time O(n)
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        search for the first node which contain data, if you have more than one 
        it's just return the first one
        take O(n) in worst case
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        inserting a new node contaning data at index position
        insertion takes O(1) time but finding a node in the node take O(n) time
        take overall O(n)
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head

        while position > 1:
            current = node.next_node
            position -= 1
        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node

    def remove(self, key):
        """
        remove the node containig data taht matahces the key
        Return the Node or None if the key dose not exist.
        take O(n) in wors case.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and  current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current

    def __repr__(self):
        """
        return string representation of the list which take O(n) time
        """

        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            current = current.next_node
        return "-> ".join(nodes)

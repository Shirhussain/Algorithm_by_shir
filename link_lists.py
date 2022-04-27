class Elements:
    def __init__(self, value):
        self.value = None
        self.next = None

class Link_list:
    def __init__(self, head):
        self.head = None

    def add(self, new_ele):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_ele
        else:
            self.head = new_ele

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        if position < 1:
            return None
        while counter and current <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

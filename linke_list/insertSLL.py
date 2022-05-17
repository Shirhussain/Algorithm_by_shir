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
        while node :
            yield node
            node = node.next
    
    def insert(self, value, location):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
            self.tail = new_node
        else :
            if location == 0:
                #it means taht change the refrance of previous head to node and node to be head
                new_node.next = self.head
                self.head = new_node
            #it means taht if we add at the tail of node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0 
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if self.temp_node == self.tail:
                    self.tail = new_node
                
single_link_list = SLingList()
single_link_list.insert(1,1)
single_link_list.insert(2,1)
# single_link_list.insert(3,1)
# single_link_list.insert(4,1)
print([node.value for node in single_link_list])




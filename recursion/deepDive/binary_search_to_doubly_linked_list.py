class Node():
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 
        
    
    def add_node(self, new_value):
        if new_value > self.value:
            if self.right is None:
                self.right = Node(new_value)
            else:
                self.right.add_node(new_value)
        elif  new_value < self.value:
            if self.left is None:
                self.left = Node(new_value)
            else:
                self.left.add_node(new_value)




def convert_tree_to_linked_list(root):
    if root is None:
        return 
    left_part = convert_tree_to_linked_list(root.left)
    right_part = convert_tree_to_linked_list(root.right)
    
    return combinator(left_part, right_part, root)


        
def combinator(left, right, node):
    if left is None and right is None:
        # Single node - make it circular
        node.left = node
        node.right = node
        return node
    elif left is None:
        # Only right subtree exists
        # Insert node between right's tail and head
        right_tail = right.left
        node.left = right_tail
        node.right = right
        right_tail.right = node
        right.left = node
        return node
    elif right is None:
        # Only left subtree exists  
        # Insert node between left's tail and head
        left_tail = left.left
        node.left = left_tail
        node.right = left
        left_tail.right = node
        left.left = node
        return left
    else:
        # Both subtrees exist
        # Connect: left_tail -> node -> right_head
        # and: right_tail -> left_head (to complete circle)
        left_tail = left.left
        right_tail = right.left
        
        # Insert node between left and right
        left_tail.right = node
        node.left = left_tail
        node.right = right
        right.left = node
        
        # Complete the circle by connecting right_tail to left_head
        right_tail.right = left
        left.left = right_tail
        
        return left


def print_circular_list(head):
    if head is None:
        print("Empty list")
        return
    
    current = head
    values = []
    
    # Traverse forward
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    
    print("Forward:", " -> ".join(map(str, values)))
    
    # Traverse backward
    current = head.left
    values = []
    while True:
        values.append(current.value)
        current = current.left
        if current == head.left:
            break
    
    print("Backward:", " -> ".join(map(str, values)))

tree = Node(10)
tree.add_node(6)
tree.add_node(14)
tree.add_node(4)
tree.add_node(8)
tree.add_node(12)
tree.add_node(16)

result = convert_tree_to_linked_list(tree)
print_circular_list(result)
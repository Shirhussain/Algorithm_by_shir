
from queue_linked_list import Queue

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insert_node(root_node, node_value):
    if root_node.data is None:
        root_node.data = node_value
    elif node_value < root_node.data:
        if root_node.leftChild is None:
            root_node.leftChild = BinarySearchTree(node_value)
        else:
            insert_node(root_node.leftChild, node_value)
    elif root_node.rightChild is None:
        root_node.rightChild = BinarySearchTree(node_value)
    else:
        insert_node(root_node.rightChild, node_value)
    return "Then node hass been inserted successfully"

def pre_order_traversal(root_node):
    if root_node is None:
        return
    print(root_node.data)
    pre_order_traversal(root_node.leftChild)
    pre_order_traversal(root_node.rightChild)

def in_order_traversal(root_node):
    if not root_node:
        return 
    in_order_traversal(root_node.leftChild)
    print(root_node.data)
    in_order_traversal(root_node.rightChild)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.leftChild)
    post_order_traversal(root_node.rightChild)
    print(root_node.data)


def level_order_traversal(root_node ):
    if not root_node:
        return
    custome_queue = Queue()
    custome_queue.enqueue(root_node)
    while not custome_queue.isEmpty():
        root = custome_queue.dequeue()
        print(root.value.data)
        if root.value.leftChild is not None:
            custome_queue.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            custome_queue.enqueue(root.value.rightChild)
                


bst = BinarySearchTree(None)

insert_node(bst, 70)
insert_node(bst, 50)
insert_node(bst, 90)
insert_node(bst, 30)
insert_node(bst, 60)
insert_node(bst, 80)
insert_node(bst, 100)
insert_node(bst, 20)
insert_node(bst, 40)

# print(bst.data)
# print(bst.leftChild.data)


pre_order_traversal(bst)

print("\n================================")

in_order_traversal(bst)

print("\n================================")

post_order_traversal(bst)

print("\n================================")
level_order_traversal(bst)
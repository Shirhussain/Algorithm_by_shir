import queue_linked_list as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        

new_binary_tree = TreeNode("Drink")
left =  TreeNode("Hot")
tea = TreeNode("Tea")
coffee =  TreeNode("Coffee")
left.leftChild = tea
left.rightChild = coffee
right = TreeNode("Cold")
new_binary_tree.leftChild = left
new_binary_tree.rightChild = right


# Pre Order traversal
def pre_order_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.leftChild)
    pre_order_traversal(rootNode.rightChild)

pre_order_traversal(new_binary_tree)
print("\n\n\n")


def in_order_traversal(rootNode):
    if not rootNode:
        return
    in_order_traversal(rootNode.leftChild)
    print(rootNode.data)
    in_order_traversal(rootNode.rightChild)

in_order_traversal(new_binary_tree)
print("\n\n\n")



def post_order_traversal(rootNode):
    if not rootNode:
        return
    post_order_traversal(rootNode.leftChild)
    post_order_traversal(rootNode.rightChild)
    print(rootNode.data)

post_order_traversal(new_binary_tree)
print("--------------------------------")

def level_order_traversal(rootNode):
    if not rootNode:
        return
    customeQueue = queue.Queue()
    customeQueue.enqueue(rootNode)
    while not (customeQueue.isEmpty()):
        root = customeQueue.dequeue()
        print(root.value.data)
        if (root.value.leftChild is not None):
            customeQueue.enqueue(root.value.leftChild)
        if (root.value.rightChild is not None):
            customeQueue.enqueue(root.value.rightChild)


level_order_traversal(new_binary_tree)
from logging import root
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
print("\n================================")


def serach_binary_tree(rootNode, nodeValue):
    if not rootNode:
        return "Binary tree does not exist"
    custome = queue.Queue()
    custome.enqueue(rootNode)
    while not (custome.isEmpty()):
        root= custome.dequeue()
        if root.value.data == nodeValue:
            return "sucess"
        if (root.value.leftChild is not None):
            custome.enqueue(root.value.leftChild)
        if (root.value.rightChild is not None):
            custome.enqueue(root.value.rightChild)
    return "not found"
print(serach_binary_tree(new_binary_tree, "Coffee"))
print("--------------------------------")


def insert_binary_tree(rootNood, new_value):
    if not rootNood:
        rootNood = new_value
    custome_Queue = queue.Queue()
    custome_Queue.enqueue(rootNood)
    while not custome_Queue.isEmpty():
        root = custome_Queue.dequeue()
        if root.value.leftChild is not None:
            custome_Queue.enqueue(root.value.leftChild)
        else:
            root.value.leftChild = new_value
            return "successfully inserted"
        if root.value.rightChild is not None:
            custome_Queue.enqueue(root.value.rightChild)
        else:
            root.value.rightChild = new_value
            return "successfully inserted value"

new_node = TreeNode("cola")
print(insert_binary_tree(new_binary_tree, new_node))
level_order_traversal(new_binary_tree)
print("--------------------------------")


def getDeepestNode(rootNode):
    if not rootNode:
        return
    custome_qu = queue.Queue()
    custome_qu.enqueue(rootNode)
    while not custome_qu.isEmpty():
        root = custome_qu.dequeue()
        if root.value.leftChild is not None:
            custome_qu.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            custome_qu.enqueue(root.value.rightChild)
    deepestNode = root.value
    return deepestNode

deepest_node = getDeepestNode(new_binary_tree)
print(deepest_node.data)
print("\n ----------------------------------------------------------------")



def deleteDeepestNode(rootNode, deep_node):
    if not rootNode:
        return 
    custome_que = queue.Queue()
    custome_que.enqueue(rootNode)
    while not custome_que.isEmpty():
        root = custome_que.dequeue()
        if root.value is deep_node:
            root.value = None
            return 
        if root.value.rightChild:
            if root.value.rightChild is deep_node:
                root.value.rightChild = None
                return
            else:
                custome_que.enqueue(root.value.rightChild)
        if root.value.leftChild:
            if root.value.leftChild is deep_node:
                root.value.leftChild = None
                return 
            else:
                custome_que.enqueue(root.value.leftChild)

new_nod = getDeepestNode(new_binary_tree)
deleteDeepestNode(new_binary_tree, new_nod)
level_order_traversal(new_binary_tree)
print("\n ----------------------------------------------------------------")


def delete_node_BT(rootNode, data_node):
    if not rootNode:
        return "The binary tree does not exist."
    custome_que = queue.Queue()
    custome_que.enqueue(rootNode)
    while not custome_que.isEmpty():
        root = custome_que.dequeue()
        if root.value.data == data_node:
            deepest_node = getDeepestNode(rootNode)
            root.value.data = deepest_node.data 
            deleteDeepestNode(rootNode, deepest_node)
            return "The nood has been successfully deleted"
        if root.value.leftChild is not None:
            custome_que.enqueue(root.value.leftChild)
            
        if root.value.rightChild is not None:
            custome_que.enqueue(root.value.rightChild)
    return "Failed to delete"

# you can see that when I delete "Hot" then coffee will be replaced with "Hot".
delete_node_BT(new_binary_tree, "Hot")
level_order_traversal(new_binary_tree)
print("\n ----------------------------------------------------------------")



def delete_whole_binary_tree(root_node):
    root_node.data = None
    root_node.leftChild = None
    root_node.rightChild = None
    return "The binary complitly deleted successfully"

print(delete_whole_binary_tree(new_binary_tree))
level_order_traversal(new_binary_tree)
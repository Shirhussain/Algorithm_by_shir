# AVL tree is that one which the gith of tree is balanced it is good for searchign
# some tiem it happend that binary search tre is not balanced then the big(O) will be O(n) like a list
# we have to make that kind of tree to AVL tree and balance the tree

# balance factor = hgiht of left subtree - hgiht of right subtree and it should be {-1, 0, 1}
# bf = hl - hr = {-1,0,1}
# bf = |hr-hr| <= 1
# then it will be a AVL

from hashlib import blake2b
from queue_linked_list import Queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def pre_order_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.leftChild)
    pre_order_traversal(rootNode.rightChild)


def in_order_traversal(rootNode):
    if not rootNode:
        return
    in_order_traversal(rootNode.leftChild)
    print(rootNode.data)
    in_order_traversal(rootNode.rightChild)


def post_order_traversal(rootNode):
    if not rootNode:
        return
    post_order_traversal(rootNode.leftChild)
    post_order_traversal(rootNode.rightChild)
    print(rootNode.data)


def level_order_traversal(rootNode):
    if not rootNode:
        return
    else:
        customeQueue = Queue()
        customeQueue.enqueue(rootNode)
        while not customeQueue.isEmpty():
            root = customeQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customeQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customeQueue.enqueue(root.value.rightChild)


def searchNode(rootNode, node_value):
    if rootNode.data == node_value:
        print("The value is found")
    elif node_value < rootNode.data:
        if rootNode.leftChild.data == node_value:
            print("the value is foudn on left child")
        else:
            searchNode(rootNode.leftChild, node_value)
    else:
        if rootNode.rightChild.data == node_value:
            print("the value is foudn on right child")
        else:
            searchNode(rootNode.rightChild, node_value)


def get_hight(root_node):
    if not root_node:
        return 0
    return root_node.height


def right_rotate(disbalance_node):
    new_root = disbalance_node.leftChild
    disbalance_node.leftChild = disbalance_node.leftChild.rightChild
    new_root.rightChild = disbalance_node
    disbalance_node.hight = 1 + \
        max(get_hight(disbalance_node.leftChild),
            get_hight(disbalance_node.rightChild))
    new_root.hight = 1 + max(get_hight(new_root.leftChild),
                             get_hight(new_root.rightChild))
    return new_root


def left_rotate(disbalance_node):
    new_root = disbalance_node.leftChild
    disbalance_node.rightChild = disbalance_node.rightChild.leftChild
    new_root.leftChild = disbalance_node
    disbalance_node.hight = 1 + \
        max(get_hight(disbalance_node.leftChild),
            get_hight(disbalance_node.rightChild))
    new_root.hight = 1 + max(get_hight(new_root.leftChild),
                             get_hight(new_root.rightChild))
    return new_root


def get_balance(root_node):
    if not root_node:
        return 0
    return get_hight(root_node.leftChild) - get_hight(root_node.rightChild)


def insert_node(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.leftChild = insert_node(root_node.leftChild, node_value)
    else:
        root_node.rightChild = insert_node(root_node.rightChild, node_value)
    root_node.hight = 1 + \
        max(get_hight(root_node.leftChild), get_hight(root_node.rightChild))
    balance = get_balance(root_node)
    # left left condation ---> then you need to rotate right
    if balance > 1 and node_value < root_node.leftChild.data:
        return right_rotate(root_node)
    # left right condation ---> then you need to rotate left then right
    if balance > 1 and node_value > root_node.leftChild.data:
        root_node.leftChild = left_rotate(root_node.leftChild)
        return right_rotate(root_node)
    # right right condation ---> then you need to rotate left
    if balance < -1 and node_value > root_node.rightChild.data:
        return left_rotate(root_node)
    # right left condation ---> then you need to rotate right then left
    if balance < -1 and node_value < root_node.rightChild.data:
        root_node.rightChild = right_rotate(root_node.rightChild)
        return left_rotate(root_node)

    return root_node


AVL = AVLNode(5)

AVL = insert_node(AVL, 10)
AVL = insert_node(AVL, 20)
AVL = insert_node(AVL, 15)

level_order_traversal(AVL)
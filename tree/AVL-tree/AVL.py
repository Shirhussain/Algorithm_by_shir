# AVL tree is that one which the gith of tree is balanced it is good for searchign
# some tiem it happend that binary search tre is not balanced then the big(O) will be O(n) like a list
# we have to make that kind of tree to AVL tree and balance the tree

# balance factor = hgiht of left subtree - hgiht of right subtree and it should be {-1, 0, 1}
# bf = hl - hr = {-1,0,1}
# bf = |hr-hr| <= 1
# then it will be a AVL

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
        while not customeQueue.is_empty():
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


AVL = AVLNode(11)

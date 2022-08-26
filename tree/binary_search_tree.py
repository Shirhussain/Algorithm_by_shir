
from logging import root
from queue_linked_list import Queue


class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insert_node(root_node, node_value):
    # in binary search tree if the value is small than root we go to left otherwise we go to rightChild
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


def level_order_traversal(root_node):
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


def search_node(root_node, node_value):
    if root_node.data == node_value:
        print("The value is found")
    elif node_value < root_node.data:
        if root_node.leftChild.data == node_value:
            print("found the value")
        else:
            search_node(root_node.leftChild, node_value)
    else:
        if root_node.rightChild.data == node_value:
            print("found the result")
        else:
            search_node(node_value.rightChild, node_value)


# for deleting we need to fined the minmum value, which means it's located in leftChild.
# becase of that we need to traverse to leftChild.

# in deleting we have tree cases:
# 1- if the node is at the end of the tree we just traverse from the root to that and find then delete
# 2- if you have a node which have one child then, traverse from root to that then delete the node and
        # repleace the child with that.
# 3- if you have a node which have two children then, traverse from root to that then
        # then find the once wich is bigger than root and delte root then repalce the one which is
        # bigger than root in root.

def minimum_value_node(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def delete_node(rootNode, node_value):
    if rootNode is None:
        return rootNode
    if node_value < rootNode.data:
        rootNode.leftChild = delete_node(rootNode.leftChild, node_value)
    elif node_value > rootNode.data:
        rootNode.rightChild = delete_node(rootNode.rightChild, node_value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # now delting if the node has two children, we need to find the minimum value in the right subtree
        # becase the sucesser of minimum is located in the right subtree
        # it means that if the root is 80 we go to rught subtree and find for 85 which is biger that not 90 or 100
        # then replace it with the root
        temp = minimum_value_node(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = delete_node(rootNode.rightChild, temp.data)
    return rootNode


def delete_All_node(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None
    return "Binary search tree hass been successfully deleted"


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


print("\n================================")
print("Search result   ")
search_node(bst, 70)

print("================================ Deleteing =================================================================")

delete_node(bst, 70)
delete_node(bst, 50)

level_order_traversal(bst)
in_order_traversal(bst)


print("\n================================ Delete All =================================================================")
print(delete_All_node(bst))
in_order_traversal(bst)

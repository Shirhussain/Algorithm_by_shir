# it means that find that what's next after this current inserting value?
# one of the best way is that you don't even need to calculate the value which is less then the current value value
# but sometime it's better to do that do make sure that is correct value.
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minimum_value(node):
    # want to find the minimum value or the most left value
    current = node
    while (current is not None):
        # while we have the minimum value go to the left
        if current.left is None:
            break
        current = current.left
    return current


def in_order_successor(root, n):
    # n is the current node
    if n.right is not None:
        return minimum_value(n.right)
    p = n.parent
    while p is not None:
        # it means that we riche the right most value
        if n != p.right:
            break
        n = p
        p = p.parent
    return p


def insert(node, data):
    if node is None:
        return BinaryTree(data)
    else:
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node


root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

# 3 ---> i want to check that it should show the parent which is next in order traversal (4)
temp = root.left.right

successor = in_order_successor(root, temp)

if successor is not None:
    print(f"the successor for {temp.data} is {successor.data}")
else:
    print("Inorder successor does not exist")

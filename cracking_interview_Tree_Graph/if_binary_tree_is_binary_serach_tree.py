class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def helper(node, min_value=float('-inf'), max_value=float('inf')):
    # this is te base case for recursion
    if not node:
        return True
    val = node.value
    if val < min_value or val > max_value:
        return False
    if not helper(node.right, val, max_value):
        return False
    if not helper(node.left, min_value, val):
        return False
    return True


def isValidBST(root):
    return helper(root)


bst = BinaryTree(4)
bst.left = BinaryTree(2)
bst.right = BinaryTree(7)

print(isValidBST(bst))

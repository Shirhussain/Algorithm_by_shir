class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def get_height(root):
    if root is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


def isBalanced(root):
    # the tree is balanced when
    if root is None:
        return True
    return isBalanced(root.left) and \
        isBalanced(root.right) and \
        abs(get_height(root.left) - get_height(root.right)) <= 1


n1 = Node("N1")
n2 = Node("N2")
n3 = Node("N3")
n4 = Node("N4")
n5 = Node("N5")
n6 = Node("N6")

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6


print(isBalanced(n1))

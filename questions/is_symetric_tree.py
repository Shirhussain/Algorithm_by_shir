# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to check if subtree rooted at `X` and `Y` mirror each other
def isSymmetric(X, Y):

    # base case: if both trees are empty
    if X is None and Y is None:
        return True

    # return true if
    # 1. Both trees are non-empty, and
    # 2. The left subtree is the mirror of the right subtree, and
    # 3. The right subtree is the mirror of the left subtree
    return (X is not None and Y is not None) and \
        isSymmetric(X.left, Y.right) and \
        isSymmetric(X.right, Y.left)


# Function to check if a given binary tree has a symmetric structure or not
def isSymmetricTree(root):

    # base case
    if not root:
        return True

    # return true if left and right subtree mirror each other
    return isSymmetric(root.left, root.right)


if __name__ == '__main__':

    ''' Construct the following tree
          1
        /   \
       /     \
      2       3
       \     /
        5   6
    '''

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(5)

    if isSymmetricTree(root):
        print('The binary tree is symmetric')
    else:
        print('The binary tree is not symmetric')


# lett code

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_mirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if (root1 is not None and root2 is not None):
            if root1.val == root2.val:
                return self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)

        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root, root)


# or
def are_symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 is None) != (root2 is None) and (root1.val != root2.val):
        return False
    return are_symmetric(root1.left, root2.right) and are_symmetric(root1.right, root2.left)


def is_symmetric(root):
    # if root is None:
    #     return True
    # return are_symmetric(root.left, root.right)
    return True if root is None else are_symmetric(root.left, root.right)

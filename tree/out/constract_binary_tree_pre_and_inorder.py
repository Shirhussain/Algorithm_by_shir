""" 
 Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root_index = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = buildTree(preorder, inorder[:root_index])
    root.right = buildTree(preorder, inorder[root_index + 1:])
    return root


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")


# Test the tree printing
tree = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print("\nTree structure:")
print_tree(tree)


def tree_to_list(root):
    if not root:
        return []

    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

    # Remove trailing nulls
    while result and result[-1] is None:
        result.pop()

    return result


# Replace the print and print_tree calls with:
tree = buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(tree_to_list(tree))

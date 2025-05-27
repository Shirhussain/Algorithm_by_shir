""" 
Construct Binary Tree from Inorder and Postorder Traversal
Medium
Topics
Companies

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder.pop()
    root_index = inorder.index(root_val)
    root = TreeNode(root_val)
    root.right = buildTree(inorder[root_index + 1:], postorder)
    root.left = buildTree(inorder[:root_index], postorder)
    return root


def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

    while result and result[-1] is None:
        result.pop()
    return result


print(tree_to_list(buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])))

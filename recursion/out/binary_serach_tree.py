# Definition for a binary tree node.
""" 
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []


"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={self.left}, right={self.right})"

    def addNode(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.addNode(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.addNode(val)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        How do I solve a recursion problem systematically?
        Answer these questions:
        - What is the base case?
            For an empty tree: we just retrun NONE
        - What are the subproblems?
            - Either of these case:
            1. search left
            2. search right
            3. if it's the root, return it!    

        - What is the combinator?
            OR

        '''
        if not root:
            return
        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


# node = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
node = TreeNode()

arr = [4, 2, 7, 1, 3]
sol = Solution()
for i in arr:
    node.addNode(i)
node.printTree()
print(sol.searchBST(node, 2))

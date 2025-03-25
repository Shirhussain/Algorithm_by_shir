

"""
Solution:
    It involes a tree, so chances are there is a recursive solution.
    
    What is the simplest instance of this problem?
        - If tree is empty: return None
        - LCA of any node and the root is the root

    What's my recursive relationship?  LCA(root, p, q)
        - Subproblem 1: left =  LCA(root.left, p, q)
        - Subproblem 2: right = LCA(root.right, p, q)
        - return Combine(left, right) 

    Combine:
        Either
            - p and q are on different subtrees, in which case the root is the answser
            - p and q are on the same subtree, either left or right is None and the LCA of the overall problem is the same as
                the subtree that returns non-none

"""
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def combine(left, right, root):
            # The root of left subtree was p (or q) and the root of the right subtree was q (or p)
            if left and right:
                return root

            # Otherwise, one of them is None
            if left:
                # this means p, q are on the left subtree, so whatever LCA we found on the left is the solution to the overal problem.
                return left

            else:
                # this means p, q are on the right subtree, so whatever LCA we found on the right is the solution to the overal problem.
                return right

        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # post order traversal, first it means going from the bottom up
        # process the left and right subtrees then process the root
        return combine(left, right, root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from tree.binary_tree import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        # result = 0
        # q = deque([root])

        # while q:
        #     result += 1
        #     my_len = len(q)
        #     for i in range(my_len):
        #         node = q.popleft()
        #         if node:
        #             if node.left is None and node.right is None:
        #                 return result
        #             q.append(node.left)
        #             q.append(node.right)
        # return result

        if root is None:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

        # if root is None:
        #     return 0

        # min_depth = float('inf')

        # def in_order_traversal(node, depth):
        #     nonlocal min_depth  # Use the minimum depth from the outer scope

        #     if node is None:
        #         return

        #     # If the current node is a leaf node, update the minimum depth
        #     if node.left is None and node.right is None:
        #         min_depth = min(min_depth, depth)

        #     # Continue the in-order traversal
        #     in_order_traversal(node.left, depth + 1)
        #     in_order_traversal(node.right, depth + 1)

        # in_order_traversal(root, 1)

        # return min_depth

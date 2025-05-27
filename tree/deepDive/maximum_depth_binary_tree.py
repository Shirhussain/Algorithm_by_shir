from collections import deque
from typing import Optional

from tree.binary_tree import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        if root is None:
            return 0
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if node:
                if node.left:
                    q.append((node.left, depth+1))
                if node.right:
                    q.append((node.right, depth+1))
        return depth

        # if root is None:
        #     return 0
        # result = 0

        # q = deque([root])
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             if node.left is not None:
        #                 q.append(node.left)
        #             if node.right:
        #                 q.append(node.right)
        #     result +=1
        # return result

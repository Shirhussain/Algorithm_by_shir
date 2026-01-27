"""
Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
"""

from typing import Optional, List 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        result = []

        q = deque([root])

        while q:
            row_max = float("-inf")
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                row_max = max(row_max, node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            result.append(row_max)
        return result

        

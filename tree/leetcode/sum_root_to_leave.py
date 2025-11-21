""" 
Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left = None, right = None ):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
            4
            4 * 10 + 9 = 49 
            49 * 10 + 5 = 495


            49 * 10 + 1 = 491
            4
            4*10 + 0 = 40
            495 + 491 + 40 = 1026
        """
        
        def pre_order(root, curr_val):
            if root is None:
                return 0
            
            new_value = curr_val * 10 + root.val 
            if root.left is None and root.right is None:
                return new_value 
            return pre_order(root.left, new_value) + pre_order(root.right, new_value)

        return pre_order(root, 0)


tree = TreeNode(1)

tree.left = TreeNode(2)
tree.right = TreeNode(3)

s = Solution()
print(s.sumNumbers(tree))


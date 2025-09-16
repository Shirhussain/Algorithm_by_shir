# https://leetcode.com/problems/binary-tree-pruning/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

                        1A
            0B                          1C
        1D                          0F       1G               


root: 1A
   left_sum: 1

# don't forget edge case

pruneTree(root):

    def postorder(root):
        if root is null
            return 0
        set left_sum = postorder(root.left)
        set right_sum = postorder(root.right)
        if left_sum == 0 
            set root.left to null
        if right_sum == 0 
            set root.right to null
        return left_sum + right_sum + root.val

    if postorder(root) is 0
        return null
    else
        return root

                        1
            1                           0
        1       1                   0       1
    0



'''
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:



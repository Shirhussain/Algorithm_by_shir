# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/?utm_source=chatgpt.com
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''

                    1
            2               3
    4              6,5              9


{-2: {2: [4]},
 -1: {1: [2]}
  0: {0: [1], 2: [5,6]},
  1: {1: [3]},
  2: {2: [7]}}


structure: {}

def verticalTraversal(root):
    #convert tree to a dict of dict of list of int

    define structure as an empty dictionary

    def preorder(root, row, col):

        if root is null
            return
        # visit
        if col is not a key in structure
            create an empty dictionary at structure[col]
        if row is not a key in structure[col]
            create an empty array at structure[col][row]
        add root.val to structure[col][row]

        preorder(root.left, row+1, col-1)
        preorder(root.right, row+1, col+1)

    preorder(root, 0, 0)

    #convert that structure to the output list of list of int


'''

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

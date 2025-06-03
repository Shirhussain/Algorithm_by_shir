# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def post(node):
            if node is None:
                return (0,0)
            (left_child, left_grand) = post(node.left)
            (right_child, right_grand) = post(node.right)
            left_return = node.val + left_grand + right_grand
            right_return = max(left_child,left_grand) + max(right_child, right_grand)
            return (left_return, right_return)

        (child, grand_child) = post(root)
        return max(child, grand_child)
        
'''
Diagram:

                3

        2               3
         ^(3,0)           ^(1,0)
           3                1


Example 3:
              (1+4+5, 6+5)
                    1
        (6+0+0,1+3)     (1+0+0,0+5)
            6               1
      (1,0)   (3,0)           (5,0)
        1       3               5

Output: 11 (6+5)

Example 4:
                (4+2, 4)
                    4
          (1+3,max(2,3))
             1
      (2,3)
        2
(3,0)   
3

'''
'''
Pseudocode

def house_robber(root)

    def post(node)
        if node is null
            return (0,0)
        (left_child, left_grand) = post(node.left)
        (right_child, right_grand) = post(node.right)
        left_return = node.val + left_grand + right_grand
        right_return = left_child + right_child
        return (left_return, right_return)

    (child, grand_child) = post(root)
    return max(child, grand_child)


'''
        
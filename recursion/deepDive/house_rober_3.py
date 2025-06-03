       
'''
https://leetcode.com/problems/house-robber-iii/

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
        
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def print_tree(self):
        if self.val is None:
            print("Tree is empty")
            return
        q = [self]
        
        while q:
            curr = q.pop(0)
            print(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

def build_tree_from_array(arr):
    """Build binary tree from LeetCode array format"""
    if not arr or arr[0] is None:
        return None
    
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        node = queue.pop(0)
        
        # Add left child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Add right child  
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    
    return root

from typing import Optional
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def post(node):
            if node is None:
                return (0,0)
            (left_child, left_grand) = post(node.left)
            (right_child, right_grand) = post(node.right)
            pick_curr_val = node.val + left_grand + right_grand
            not_pick_curr_val = max(left_child,left_grand) + max(right_child, right_grand)
            return (pick_curr_val, not_pick_curr_val)

        (child, grand_child) = post(root)
        return max(child, grand_child)



root = [3,2,3,None,3,None,1]

tree = build_tree_from_array(root)

print(tree.print_tree())

s = Solution()
result = s.rob(tree)
print(result)
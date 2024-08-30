""" 
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        state = {}
        level = 0
        return self.helper_func(root, state, level)

    def helper_func(self, root: Optional[TreeNode], state={}, level=0) -> List[List[int]]:
        if root is None:
            return []
        level += 1
        state[level] = state.get(level, []) + [root.val]
        self.helper_func(root.left, state, level)
        self.helper_func(root.right, state, level)
        return state.values()

    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     result = []
    #     q = collections.deque()
    #     q.append(root)
    #     while q:
    #         len_q = len(q)
    #         level = []
    #         for i in range(len(q)):
    #             node = q.popleft()
    #             if node:
    #                 level.append(node.val)
    #                 q.append(node.left)
    #                 q.append(node.right)
    #         if level:
    #             result.append(level)
    #     return result

    #     return result

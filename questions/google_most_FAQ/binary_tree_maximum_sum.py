from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [root.val]

        #max sum wihtout spliting
        def dfs(root):
            if not root:
                return 0
            max_left = dfs(root.left)
            max_right = dfs(root.right)

            # when it's become negative value then I chose zero instad.
            max_left = max(max_left, 0)
            max_right = max(max_right, 0)

            #sum the max of value when it's spliting it means form the root get left and right jsut tree number
            result[0] = max(result[0], root.val + max_left + max_right)
            return root.val + max(max_left, max_right)
        dfs(root)
        return result[0]

            

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)

solutaion = Solution()

natija = solutaion.maxPathSum(tree)
print(natija)



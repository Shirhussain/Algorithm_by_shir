'''
Longest Path of a Binary Tree

Given a binary tree node, return the number of nodes in the longest path between the root and a leaf node

Input: Node in a Binary Tree
Output: Integer


            1
      /         \
      2            3
                      \
                       4

Output: 3

Time Complexity: O(N)
Auxiliary Space Complexity: O(N)
Use a recursive dfs
Make good use of postorder search

max_path_length(node)

  dfs(node)
     if node is not null
        left_max_length = dfs(node's left child)
        right_max_length = dfs(node's right child)
        return max(left_max_length, right_max_length) + 1
      else
        return 0

  return dfs(node)

'''


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def lst_to_tree(nums):
    nums.sort()

    def helper(lst):
        mid = len(lst)//2
        root = TreeNode(lst[mid])
        root.left = TreeNode(lst[:mid])
        root.right = TreeNode(lst[mid+1:])
        return root
    return helper(nums)


lst = [1, 2, 3, 4]
sample_tree = lst_to_tree(lst)


def max_depth(root):
    def dfs(node):
        if node:
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            return max(left_max, right_max) + 1
        else:
            return 0
    return dfs(root)


print(max_depth(sample_tree))


def max_depth_tree(root):
    def helper(node):
        return 0 if node is None else max(helper(node.left), helper(node.right)) + 1
    return helper(root)


print(max_depth_tree(sample_tree))


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


print_tree(sample_tree)

""" 
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:

Input: root = [1]
Output: ["1"]

"""


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def lst_to_binary_tree(nums):
    nums.sort()

    def helper(lst):
        if not lst:
            return
        mid = len(lst)//2
        root = TreeNode(lst[mid])
        root.left = helper(lst[:mid])
        root.right = helper(lst[mid+1:])
        return root
    return helper(nums)


nums = [1, 2, 3, 5]
sample_tree = lst_to_binary_tree(nums)


def tree_paths(root):
    from collections import deque
    q = deque([(root, str(root.value))])
    result = []

    while q:
        node, path = q.popleft()

        # if it's a leave node, means no children left and right
        if not node.left and not node.right:
            result.append(path)

        if node.left:
            q.append((node.left, f'{path}->{str(node.left.value)}'))

        if node.right:
            q.append((node.right, f'{path}->{str(node.right.value)}'))
    return result


print(tree_paths(sample_tree))


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


print_tree(sample_tree)

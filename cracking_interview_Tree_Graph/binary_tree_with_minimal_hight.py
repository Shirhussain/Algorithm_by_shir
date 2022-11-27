# sortedArray = [1,2,3,4,5,6,7,8,9]
# minimalTree(sortedArray)

# #Output

#    _5__
#   /    \
#   3    8
#  / \  / \
#  2 4  7 9
# /    /
# 1    6
# Minimal Binary Search Tree
# for displaying this tree you can use this code on stack Overflow
# https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def minimalTree(sortedArray):
    if len(sortedArray) == 0:
        raise None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    mid = len(sortedArray) // 2
    left = sortedArray[:mid]
    right = sortedArray[mid+1:]
    return BSTNode(sortedArray[mid], left, right)


sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9]
binary_search_tree = minimalTree(sortedArray)


# from queue import Queue


# class BSTNode:
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right


# def minimalTree(sortedArray):
#     if sortedArray is None:
#         return 0
#     left_height = minimalTree(sortedArray.left)
#     right_height = minimalTree(sortedArray.right)
#     max_height = left_height
#     if right_height > max_height:
#         max_height = right_height
#     return max_height


# def insert(root, new_value):
#     if root is None:
#         root = BSTNode(new_value)
#         return root
#     if new_value < root.data:
#         root.left = insert(root.left, new_value)
#     else:
#         root.right = insert(root.right, new_value)
#     return root


# root = insert(None, 5)
# insert(root, 3)
# insert(root, 8)
# insert(root, 2)
# insert(root, 4)
# insert(root, 7)
# insert(root, 9)
# insert(root, 1)
# insert(root, 6)

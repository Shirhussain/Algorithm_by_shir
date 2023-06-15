"""
Example Tree:
               4
             /   \
           2       5
         /   \       \
       1       3       7
                     /   \
                   6      8

#!/bin/python3

Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


Complete the 'treeBFS' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts TreeNode root as parameter.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left= None 
        self.right= None

    

def bfsTree(root):
    result = []
    if root is None:
        return result
    q = [root]
    while q:
        node = q.pop(0)
        result.append(node.value)
        
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return result


tree = Node(4)
tree.left = Node(2)
tree.right = Node(5)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right.right = Node(7)
tree.right.right.left = Node(6)
tree.right.right.right = Node(8)

# Perform BFS traversal on the tree
bfs_result = bfsTree(tree)

# Output the list
print(list(bfs_result))
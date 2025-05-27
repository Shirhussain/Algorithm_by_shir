""" 

What are some indicators I should use a Tree to solve a problem?

- Given a tree (data structure) ...
- Hierarchical data structure (outline)
  == HTML, JSON, XML
- Easily divisible, subproblem

How do I solve a (binary) Tree problem?

- Breadth-first search
  == Optimal solution: find node closest to the root with a specified property
  == Not recursive: no concern about exceeding system stack size
- Depth-first search
  == Cleaner/easier to write
  == Push-down and pull-up algorithms

  Three types of DFS:
  --- Preorder: push-down recursion
  --- Inorder: left-to-right
  --- Postorder: pull-up recursion


Write a template for a recursive DFS tree traversal

pre-dfs(node, path):
  if node is not empty
    process node: add node to path
    pre-dfs(node.left, path)
    pre-dfs(node.right, path)

in-dfs(root):
  if root is not empty
    in-dfs(root.left)
    process root
    in-dfs(root.right)


Write a template for a BFS binary tree traversal

bfs(root):
  create an empty queue
  add root to queue
  while queue is not empty
    remove node from queue
    process node
    add children to queue

What is the runtime & space complexity of a Tree Traversal?

Space:
BFS: O(max width of tree + output size)
DFS: O(max depth of tree + output size)
  
Time: O(size of tree)

"""


'''
Valid Binary Search Tree
Given a binary tree root node, check if the tree is a valid binary search tree.

Note: A binary search tree is a binary tree with the property that at every node, the values of 
all of the nodes in the left subtree must be less than the parent value and similarly 
the values of all of the nodes in the right subtree must be greater than the parent value.

Input: Node in a Binary Tree
Output: Boolean
'''
''' 
Constraints:

Time: O(size of the tree)
Auxilliary space: O(max depth of the tree)

Questions:

- Can there be duplicate node values? Yes, but if there are, answer "false".
'''
'''
Example: 
Input:
          5
      /       \
     2         7
            /    \
           4      9
           
Output: false
Explanation: 4 is to the right of 5 but is less than 5.

Edge cases:
Input: [ 5 ]
Output: true

Example 2:
Input:
      5
  /       \
 2         7
        /    \
       6      9
       
Output: true

'''

'''
Diagram:

      5
  /       \
 2         7
        /    \
       6      9

5:
 dfs check all nodes on left: are they < 5?
   preorder dfs
   visit 2: is < 5
   
 dfs check all nodes on right: are they > 5?
   visit 7: ok
   visit 6: ok
   visit 9: ok
2:
7:
6:
9:

'''
'''
Pseudocode

Solution 1 (fails run time)

check_bst(root):

  # process nodes in the order of a breadth-first search
  create an empty queue
  add root to queue
  while queue is not empty
    remove node from queue
    # visit node
    if pre-dfs(node.left, node.value, "left")
      return false
    if pre-dfs(node.right, node.value, "right")
      return false
    add node.left to queue
    add node.right to queue
    
  return true

pre-dfs(node, value, direction):
  if node is empty
    return true
  if direction is "left" and node.value >= value
    return false
  if direction is "right" and node.value <= value
    return false
  if pre-dfs(node.left, value, direction) is false
    return false
  return pre-dfs(node.right, value, direction)


Solution 2:

Do an inorder traversal and record the values in an array
Scan the array left-to-right. If any pair is not in ascending order, return false.
Return true.


Solution 3: 

set previous to -infinity 
Do an inorder traversal wtih "process node" defined as follows:
    if node.value <= previous
       return false
    set previous to node.value
    AND add checks for return values from recursive calls
    AND add return true at end

Alternate good solution: pushdown recursiion passing ranges to children

'''














# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# DO NOT EDIT
# generate tree from list
def deserialize(lst):
    if len(lst) == 0:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        if i + 1 < len(lst) and lst[i + 1] is not None:
            current.right = TreeNode(lst[i + 1])
            queue.append(current.right)
        i += 2
    return root

# DO NOT EDIT
lst = [4, 2, 5, 1, 3, None, 7, None, None, None, None, 6, 8]
'''
              4
      2                5
  1       3                7
                          6 8
'''

sample_tree = deserialize(lst)

def valid_BST(node):
  pass
  
print(valid_BST(sample_tree))

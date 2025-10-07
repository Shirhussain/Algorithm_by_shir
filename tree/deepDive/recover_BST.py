# https://leetcode.com/problems/recover-binary-search-tree/description/

'''
Understanding:
 Cannot change the structure of the tree
 Can only swap values of exactly two nodes
 2 <= n <= 1000

Diagram:

input tree:
      2
  1       4
        3

prev_node: 2
node: 3
  node: 4
    node: 3

  
inorder traversal:
  1   3 2 4

output:
      2
    1    4
        3
        
build a bst:
      3
  1       4
     2

Note: Inorder traversal is an easy way to check for binary search tree

Pseudocode:

def rec_bst(root):

  define prev_node = null

  def inorder(node):

    if node is null
      return false
    if inorder(node.left) return true
    if prev_node is not null
      if prev_node.value > node.value
        swap values
        return true
    else
      prev_node = new node
    prev_node.value = node.value
    if inorder(node.right) return true
    return false

  inorder(root)
'''
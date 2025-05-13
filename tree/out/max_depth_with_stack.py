'''
Find the maximum depth of node in a binary tree using an explicit stack rather than recursion.
An empty tree has max depth of 0, a tree with a single node max depth of 1.
'''

'''

preorder_stack(node):
  if node is null
    return 0
  create empty stack
  initialize max_depth to 1
  store (node, 1) in stack
  while stack is not empty
    pop (node, depth) from stack
    # visit(node)
    if depth > max_depth set max_depth to depth
    push (node.right, depth+1) (if node.left is not null)
    push (node.left, depth+1) (if node.right is not null)
  return max_depth


          
               1,1
          2,2         3,2
                  4,3




'''

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
Example: 
Input:
          5
      /       \
     2         7
            /    \
           4      9
           
Output: false
Explanation: 4 is to the right of 5 but is less than 5.

'''
'''
Constraints:

Time Complexity: O(N)
Auxiliary Space Complexity: O(D), D=depth of the tree
'''

'''
Diagram: Postorder

                      5
                  /       4\10
                 2          7
                        4/4   9\10
                       4        9
                                10\10
                                  10
                       
'''
'''
Pseudocode: Postorder approach

def check_bst(node):

  set answer to true

  def helper(node):
    if node is null
      return true
    if node.left is null
      if node.right is null
        return (node.val, node.val)
      right_value = helper(node.right)
      if right_value[0] <= node.val
        set answer to false
      else 
        return (node.val, right_value[1])
    else
      left_value = helper(node.left)
      if left_value[1] >= node.val
        set answer to false
      if node.right is not null
        right_value = helper(node.right)
        if right_value[0] <= node.val
          set answer to false
        return (left_value[0], right_value[1])
      else 
        return (left_value[0], node.val)
      
  helper(node)
  return answer
           
'''

'''
Diagram: Preorder

      -inf,inf
          5
-inf/5      5\inf
   2           7
            5/7   7\inf
           4        9

'''
'''
Diagram: Inorder

      5
  /       \
 2          7
         /    \
        4      9

2 5 4 7 9
'''
'''

def check_bst(node)

  initialize prev_value to negative infinity

  def helper(node)

    if node is not null
      if helper(node.left) is false return false
      
      if node.val <= prev_value
        return false 
      else 
        set prev_value to node.value
        return true

      return helper(node.right)
      
  return helper(node)

'''

'''
BFS
                5
            /       \
           2         7
                  /    \
                 4      9



'''











'''
Pseudocode


'''
'''
Runtime: O(N)
Space: O(D)
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


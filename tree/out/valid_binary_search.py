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

Edge cases:
Input: []
Output: true

'''
'''
Constraints:

Time Complexity: O(N)
Auxiliary Space Complexity: O(D), D=depth of the tree
'''

'''

          5
    /            \ 
 2                   7
                 /        \
              4             9
       


prev 5
> inorder(2)
> check 5
> inorder(7)
  > inorder(4)
    > inorder([])
    > check 4


'''
'''
Pseudocode

def valid_bst(node):

    set prev to negative infinity

    def inorder(node):

        if node is empty
            return true
        else
            if inorder(node.left) is False
                return false
            if node.value <= prev
                return False
            set prev to node.value
            return inorder(node.right)
            
    return inorder(node)
    
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

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
  1          /    \
            4      9

Output: false
Explanation: 4 is to the right of 5 but is less than 5.


solution: 
    1. if we want to go level by level from top to bottom, we need to use level order traversal 
    2. if we need to access first to root we have to use pre order traversal
    3. if we need to go column vise(if we put each node in a column) from left to right --> use in order traversal
    4. if we want to got bottom up then use post order traversal
    
    in this question we need to check left and right with root 
    the best way if in order because it's automatically become sorted if the tree is
    binary search tree.


valid_bst(node)
  prev_node = -inf
  inorder(node)
    if node is not null
       if not inorder(node.left)
         return false
       # visit node
       if node.value < prev_node
          return false
       prev_node = node.value
       if not inorder(node.right)
          return false
     return true
  return inorder(node)

conversion to iterative:

Input:
          5
      /       \
     2         7
  1          /    \
           4      9

prev_node = 5
stack: (7, false)
curr: 4
first: false

valid_bst_iterative(node)
  prev_node = -inf
  create stack containing (node, first=true)
    (first=true means that the first part of the code should
     be executed. first=false means that we have returned from
     the first recursive call and should execute from there.
     We only need one "return false" in the iterative version.)
  while stack is not empty
     (curr,first) = pop top of stack
     if first
       if curr is not null
          # Return to this instance of the recursion
          # once the left child has been processed.
          push (curr, first=false) on top of stack
          push (curr.left, first=true) on top of stack
     else
       if curr.value < prev_node
          return false
       prev_node = curr.value
       push (curr.right, first=true) on stack
  return true
    

stack: 2, 5
prev_node = 1
curr: 

Constraints:

Time Complexity: O(N)
Auxiliary Space Complexity: O(D)

   dfs(node)
     if node is empty return true
     create empty stack
     push node on stack
     prev_node = -infinity
     while stack is not empty
       curr = stack.pop()
       while curr is not null
         push curr onto stack 
         curr = curr.left
       curr = stack.pop()
       if curr <= prev_node
         return false
       prev_node = curr.value
       curr = curr.right
       
    return true
       
         

'''


'''
Diagram


'''


'''
Pseudocode

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

# or


def build_binary_tree_from_list(lst):
    if not lst:
        return None

    # Create the root node from the first element in the list
    root = TreeNode(lst[0])
    queue = [root]  # Use a queue to keep track of parent nodes

    i = 1  # Start from the second element in the list
    while i < len(lst):
        current_node = queue.pop(0)  # Get the next parent node

        # Create the left child node if there is an element in the list
        if lst[i] is not None:
            current_node.left = TreeNode(lst[i])
            queue.append(current_node.left)

        i += 1  # Move to the next element in the list

        # Create the right child node if there is an element in the list
        if i < len(lst) and lst[i] is not None:
            current_node.right = TreeNode(lst[i])
            queue.append(current_node.right)

        i += 1  # Move to the next element in the list

    return root

# or


def list_to_tree(lst):
    if not lst:
        return None
    mid = len(lst) // 2
    root = TreeNode(lst[mid])
    root.left = list_to_tree(lst[:mid])
    root.right = list_to_tree(lst[mid+1:])
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


def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")


print_tree(sample_tree)


def is_valid_tree(root):
    # in order is the best way because in in order we move form left to the right column vise
    # at the end of the day it's going to be sorted if the tree is correct
    prev_node = float('-inf')

    def in_order(node):
        nonlocal prev_node
        if node is not None:
            if not in_order(node.left):
                return False

            # visit
            if node.value <= prev_node:
                return False
            prev_node = node.value

            if not in_order(node.right):
                return False
        return True

    return in_order(root)


print(is_valid_tree(sample_tree))


# or

def is_valid_tree_recursive(root):

    def valid(node, left, right):
        if node is None:
            return True
        if not (node.value < right and node.value > left):
            return False

        return valid(node.left, left, node.value) and valid(node.right, node.value, right)

    return valid(root, float('-inf'), float('inf'))


print(is_valid_tree_recursive(sample_tree))


def is_valid_iterative(root):
    if root is None:
        return True
    stack = [(root, float('-inf'), float('inf'))]

    while stack:
        node, left, right = stack.pop()
        if node.value > right or node.value < left:
            return False
        if node.left:
            stack.append((node.left, left, node.value))
        if node.right:
            stack.append((node.right, node.value, right))
    return True


print(is_valid_iterative(sample_tree))


def is_valid_iterative_2(root):
    stack = []
    prev_node = float('-inf')

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()

        if root.value <= prev_node:
            return False

        prev_node = root.value
        root = root.right
    return True


print(is_valid_iterative_2(sample_tree))

""" 
Tree Isomorphism Problem
Given two Binary Trees, the task is to check whether they are isomorphic or not. Two trees are called isomorphic if one of them can be obtained from the other by a series of flips, i.e. by swapping left and right children of several nodes. Any number of nodes at any level can have their children swapped.

Note:

If two trees are the same (same structure and node values), they are isomorphic.
Two empty trees are isomorphic.
If the root node values of both trees differ, they are not isomorphic.

Examples:

Input:


Tree-Isomorphism-Problem
Output: True
Explanation: The above two trees are isomorphic with following sub-trees flipped: 2 and 3, NULL and 6, 7 and 8. 


Try it on GfG Practice
redirect icon
Table of Content

[Expected Approach – 1] Using Recursion – O(n) Time and O(n) Space
[Expected Approach – 2] Using Iteration – O(n) Time and O(n) Space
[Expected Approach – 1] Using Recursion – O(n) Time and O(n) Space
The idea is to traverse both trees recursively, comparing the nodes n1 and n2. Their data must be the same, and their subtrees must either be identical or mirror images (flipped). This ensures that the trees are structurally isomorphic.


Follow the steps to solve the problem:

Let the current internal nodes of the two trees be n1 and n2. For the subtrees rooted at n1 and n2 to be isomorphic, the following conditions must hold:

The data of n1 and n2 must be the same.
One of the following two conditions must be true for the children of n1 and n2:
The left child of n1 is isomorphic to the left child of n2, and the right child of n1 is isomorphic to the right child of n2.
The left child of n1 is isomorphic to the right child of n2, and the right child of n1 is isomorphic to the left child of n2.
This ensures that the trees are either structurally identical or have been “flipped” at some levels while still being isomorphic.








Another approach: 

# https://www.geeksforgeeks.org/tree-isomorphism-problem/
'''
                1
      > 2                3
   4       5          6
         7  8

                1
        3                  > 2
            6          4           5
                                7    8


def iso(root1, root2)
  if root1 is null and root2 is null
    return true
  if root1 is null or root2 is null
    return false
  if root1.value is not equal to root2.value
    return false

  create empty queue1 and queue2
  push (root1,null) onto queue1 and (root2,null) onto queue2

  while both queues are not empty
    if queues are unequal length
      return false
    remove (tree1, parent1) from queue1 and (tree2, parent2) from queue2
    if parent1.value is not equal to parent2.value
      return false
    if tree1.left.value == tree2.left.value then
      # need tests for left/right null
      add (tree1.left, tree1) to queue1 and (tree2.left, tree2) to queue2
      add (tree1.right, tree1) to queue1 and (tree2.right, tree2) to queue2
    else
      add (tree1.left, tree1) to queue1 and (tree2.right, tree2) to queue2
      add (tree1.right, tree1) to queue1 and (tree2.left, tree2) to queue2 
    
  return true
  

def iso(tree1, tree2)
  if tree1 is null and tree2 is null
    return true
  if tree1 is null or tree2 is null
    return false
  if tree1.value is not equal to tree2.value
    return false
  if child values of tree1 are not the same as the child values of tree 2
    return false
  if tree1.left.value == tree2.left.value
    first = tree2.left
    second = tree2.right
  else
    first = tree2.right
    second = tree2.left
  if not iso(tree1.left, first)
    return false
  return iso(tree1.right, second)

'''
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class IsomorphicTree:
    def __init__(self):
        pass

    def is_isomorphic(self, root1, root2):
        # preorder traversal
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
        return (self.is_isomorphic(root1.left, root2.left) and
                self.is_isomorphic(root1.right, root2.right)) or \
               (self.is_isomorphic(root1.left, root2.right) and
                self.is_isomorphic(root1.right, root2.left))


if __name__ == "__main__":
    tree1 = Node(1)
    tree1.left = Node(2)
    tree1.right = Node(3)
    tree1.left.left = Node(4)
    tree1.left.right = Node(5)

    tree2 = Node(1)
    tree2.right = Node(2)
    tree2.left = Node(3)
    tree2.right.right = Node(4)
    tree2.right.left = Node(5)

    print(IsomorphicTree().is_isomorphic(tree1, tree2))

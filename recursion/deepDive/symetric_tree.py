# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

                                1
                  3                            3

              4                                      4
            6   7                                  7   6

'''
'''
Base cases:
  if root1 and root2 are empty, then return true
  if either root is null, then return false
  if values differ, then return false
  
                  L                           R
                                  
                  3                            3

              4       8                     8        4
            6   7                                  7   6


                               (3L,3R)
              (4L,4R)                   (8L,8R)
      (6L,6R)    (7L,7R)
 (N,N)  (N,N)
                    
'''
'''
Pseudocode

def symmetric(root):

  # return true if tree rooted at root1 is mirror of tree rooted at root2
  def helper(root1, root2):
    # Base cases
    if root1 and root2 are empty, then return true
    if either root is null, then return false
    if root1.val != root2.val, then return false

    # Recursive case
    # Both root1 and root2 are non-null and have the same values
    return helper(root1.left, root2.right) and helper(root1.right, root2.left)

  return helper(root.left, root.right)

'''
'''
https://www.geeksforgeeks.org/dsa/boundary-traversal-of-binary-tree/

Given the root of a binary tree, traverse the "outside" nodes of the tree in a 
counter-clockwise order, beginning at the root. "Outside" is left-most nodes
excluding leaf, rightmost nodes excluding leaf, and leaves.  

Input:
                   1
              2          3

Output: [1 2 3]



Input:
                   1
              2          3

          4      5     6    7
        8   9  10 11

Output: [1 2 4 8 9 10 11 6 7 3]

Depth of tree is at most 10
Integer values
At least 1 node in the tree

O(n) space/time complexity

'''

'''
Input:
                         1
                2                3
          
            4       5          6    7
          8   9  10  11
                      12

Output: [1 2 4 -- 8   9   10      12   6   7 -- 3]
Inorder:         [8 4 9 2 10 5 11 12 1 6 3 7 ]


                          1
                  2           3
              4     6             5
                      7
                        8


                            1
                2                         3
          4           5                          6
   7               8      9                            10
     11                                             12
        13

       
Preorder: [1 2 4 7 11 13]


[ 1 2 4 7 11 13   8 9    12 10 6 3 ]
''' 



'''
Pseudocode:
  process the left nodes of the tree from root to leaf (leave leaf out)
  process the bottom nodes of the tree from left to right
  process the right nodes of the tree from leaf to root (leave leaf and root out)

def ccw(root):

  if root has no children
    return [root.val]

  set answer to an empty list
  if root has no left child
    set answer to [root.val]
  else
    # process left side of tree
    set node to root
    while node is not a leaf
      add node.val to answer
      if node.left is not null
        set node to node.left
      else
        set node to node.right
  
  # process leaves

  def inorder(node)
    if node is null
      return
    inorder(node.left)
    if node is a leaf
      add node.val to answer
    inorder(node.right)
    
  inorder(root)

  # process right side of tree
  set part_answer to empty list
  set node to root.right
  if node is not null
    while node is not leaf
      add node to part_answer
      if node.right is not null
        set node to node.right
      else
        set node to node.left
    add reverse of part_answer to end of answer
  return answer


  # alt left side of tree:
  def preorder(root):
    if root is leaf
      return 
    add root.val to answer
    if root.left is not null preorder(root.left)
    else preorder(root.right)
    
'''
'''
Given the root of a binary tree with integer values at the nodes and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

                            5
              4                         8
        11                        13         4
      7    2                                   1
      
targetSum = 22
Output: true

                1
            2      3
            
targetSum = 5
Output: false

targetSum = 3
Output: true

               3
targetSum = 3
Output: true


Input: [], targetSum = 0
Output: false

Range of values: [-1000, 1000]

'''

'''
targetSum: 22

                       5,22,[]
            4,17,[5]                     8,17,[5]
      11,13,[5,4]                     13         4
  7,2,[5,4,11]    2,2,[5,4,11]                                  1

Output: [5, 4, 11, 2]

Seems like preorder because we want to create paths

5,22 --> true
   4,17 --> true
       11,13 --> true
          7,2 --> false
          2,2 --> true

   8,17 XXXXXX
'''

'''
def path_sum(node, targetValue)

  path = []
  
  def preorder(node, remainingTarget):
    nonlocal path (Python)
    if node is null
      return false
    if node is a leaf 
      if node's value == remainingTarget
        add node to path
      return node's value == remainingTarget
        
    newRemainingTarget = remainingTarget - node's value
    push node onto path
  
    result = preorder(node.left, newRemainingTarget) or
             preorder(node.right, newRemainingTarget)
    if result is false
      remove node from path

    return result

  preorder(node, targetValue)
  return path
'''

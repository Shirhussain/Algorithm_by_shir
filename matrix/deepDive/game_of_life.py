# https://leetcode.com/problems/game-of-life/description/

# Initial version:
'''
Diagram:

[[0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]]

 [[0,0,0],
  [1,0,1],
  [1,1,1],
  [0,0,0]]
'''
'''
Pseudocode

def life(board):
  make a copy of board
  for each element of board
    if element should change based on neighbors
      change it in the copy

'''
# Aux space O(1)
'''
Diagram:

[[ 2,-1, 2],
 [-2, 2, 1],
 [ 1, 1, 1],
 [ 2, 2, 2]]



'''
'''
Pseudocode

def life(board):
  replace each 0 with a 2
  for each element of board
    if element should change based on absolute values of neighbors
      negate it
  replace each 2 with a 0, -2 with a 1, and each -1 with a 0

'''

'''
            1
          1 0 1
        1 0 0 0 1
          1 0 1
            1

'''

'''
Variation: no bounds

[[0,1,0],
 [0,0,1],
 [1,1,1],
 [0,0,0]]


[
 [0,0,0,0,0]
 [0,0,1,0,0],
 [0,0,0,1,0],
 [0,1,1,1,0],
 [0,0,0,0,0],
 [0,0,0,0,0]
 ]


'''
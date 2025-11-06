# https://leetcode.com/problems/game-of-life/description/

# Initial version:
'''
Diagram:

Initial:

    V
> [[0,1,0],
   [0,0,1],
   [1,1,1],
   [0,0,0]]

diff:
[
[0,1],
[1,0],
...
]

Final:
 [[0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]]
'''
'''
Pseudocode

def life_update(board):
  # create an empty diff list
  for i taking on every row index value
    for j taking on every col index value
      let count be number of 1 or 2 neighbors of board[i][j]
      if board[i][j] == 1
        if count is not 2 or 3
          # add (i,j) to diff
          set board[i][j] to 2
      else
        if count == 3
          # add (i,j) to diff
          set board[i][j] to 3
  # for each element of diff list
    # toggle board at the element
  for each element of the board
    if board element is 3 
      set it to 1
    else if board element is 2
      set it to 0

    


'''
# Aux space O(1)
'''
Diagram:



'''
'''
Pseudocode


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



'''

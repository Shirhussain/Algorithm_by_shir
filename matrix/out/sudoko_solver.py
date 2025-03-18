'''
https://leetcode.com/problems/sudoku-solver/
'''

'''
1. Understanding:
Run time: Exponential time (don't worry about it)
'''
'''
2. Diagram

                          Board 0 : 51 empty squares
                        [["5","3",".",".","7",".",".",".","."]

      Board 1 ............................................ Board 9 : 50 empty squares
[["5","3","1",".","7",".",".",".","."]             [["5","3","9",".","7",".",".",".","."]
Board1.1...                     Board1.9 : 49 empty squares
[["5","3","1","1","7",".",".",".","."]
'''
'''
3. Pseudocode

// Top-level: tree search
// Helper method: matrix scan (row and column) for empty square

def sudoku(board):

  def helper(board, number_empty_squares):

    if board is invalid (solve this using valid_sudoku.py)
      return false
    if board is filled (number_empty_squares is 0)
      return true

    next_empty_square = find_next_empty_square(board)
    # for each child (try 1-9 in the next empty square)
    for i from 1 through 9
      child = board with i substituted at next_empty_square
      if helper(child, number_empty_square-1)
        return true
    return false

  helper(board, count_number_of_empty_squres(board))
  return


'''

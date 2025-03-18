'''
https://leetcode.com/problems/valid-sudoku/
'''
'''
1. Understand
Time constraints?
O(Size of board)
'''
'''
2. Diagram

set: 5, 3
              c==1
r==0  [["5","3",".",".","7",".",".",".","."]
       ["6",".",".","1","9","5",".",".","."]
       [".","9","8",".",".",".",".","6","."]
      ,["8",".",".",".","6",".",".",".","3"]
      ,["4",".",".","8",".","3",".",".","1"]
      ,["7",".",".",".","2",".",".",".","6"]
      ,[".","6",".",".",".",".","2","8","."]
      ,[".",".",".","4","1","9",".",".","5"]
      ,[".",".",".",".","8",".",".","7","9"]]

'''
'''
3. Pseudocode

def check_sub_grid_at(i,j)
  create an empty set
  for ii from 0 to 2
    for jj from 0 to 2
      if board[i+ii][j+jj] is in set
        return false
      if board[i+ii][j+jj] is not '.'
        add board[i+ii][j+jj] to set
  return true
        
create a set
for each row r (r takes on values 0 through 8)
  clear set
  for each column element c of row (c takes on values 0 through 8)
    if board[r][c] is in set
      return false
    if board[r][c] is not '.'
      add board[r][c] to set

# handle columns similarly

for r from 0 to 8 by 3
  for c from 0 to 8 by 3
    if not check_sub_grid_at(r,c)
      return false

return true



'''


from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        curr_value = set()

        # Validate rows
        for i in range(9):
            curr_value.clear()
            for j in range(9):
                if board[i][j] in curr_value:
                    return False
                if board[i][j] != ".":
                    curr_value.add(board[i][j])

        # Validate columns
        for j in range(9):
            curr_value.clear()
            for i in range(9):
                if board[i][j] in curr_value:
                    return False
                if board[i][j] != ".":
                    curr_value.add(board[i][j])

        # Validate 3x3 subgrids
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                if not self.sub_board_valid(board, r, c):
                    return False
        return True

    def sub_board_valid(self, board, row_start, col_start):
        curr_set = set()
        for i in range(3):
            for j in range(3):
                val = board[row_start + i][col_start + j]
                if val in curr_set:
                    return False
                if val != ".":
                    curr_set.add(val)
        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

sol = Solution()
print(sol.isValidSudoku(board))

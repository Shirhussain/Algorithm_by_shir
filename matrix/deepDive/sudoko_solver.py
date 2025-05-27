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
Tree Visualization of Backtracking:

                                   Initial Board (51 empty cells)
                                            |
                         -----------------------------------------
                        /       /           |          \          \
                       /       /            |           \          \
                      /       /             |            \          \
                     /       /              |             \          \
            (0,2)=1  (0,2)=2  ...        (0,2)=4       ... (0,2)=9
                    /           \
                   /             \
                  /               \
           (0,3)=1 ... (0,3)=9     INVALID (backtrack)
                 /
                /
               /
        (0,4)=1 ... (0,4)=9
              \
               \
                \
                 INVALID (backtrack)
                    \
                     \
                      \
                       Try next value (0,3)=2
                             |
                             V
                        And so on...

Legend:
- (r,c)=n means placing digit n at position (row r, column c)
- Each node is a state of the board
- Each level represents filling one empty cell
- Branches that lead to invalid boards are pruned
- When backtracking occurs, we go up the tree and try the next value
- Solution is found when we reach a leaf node with all cells filled
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


class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(board, row, col, num):
            # Check row
            for x in range(9):
                if board[row][x] == str(num):
                    return False

            # Check column
            for x in range(9):
                if board[x][col] == str(num):
                    return False

            # Check 3x3 box
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == str(num):
                        return False
            return True

        def find_next_empty_square(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        return (i, j)
            return None

        def count_number_of_empty_squares(board):
            count = 0
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        count += 1
            return count

        def helper(board, number_empty_squares):
            # If board is filled
            if number_empty_squares == 0:
                return True

            # Find next empty square
            next_empty_square = find_next_empty_square(board)
            if not next_empty_square:
                return True

            row, col = next_empty_square

            # Try 1-9 in the next empty square
            for num in range(1, 10):
                if is_valid(board, row, col, num):
                    # Place the number
                    board[row][col] = str(num)

                    # Recursively try to solve the rest
                    if helper(board, number_empty_squares - 1):
                        return True

                    # If not successful, backtrack
                    board[row][col] = "."

            return False

        empty_squares = count_number_of_empty_squares(board)
        helper(board, empty_squares)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

sol = Solution()
sol.solveSudoku(board)
print(board)

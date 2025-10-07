""" 
N-Queens
Solved
Hard
Topics
Companies

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:

Input: n = 1
Output: [["Q"]]


"""


class NQueens(object):
    def __init__(self, n):
        self.n = n
        self.board = [["." for _ in range(n)] for _ in range(n)]

    def solveNQueens(self):
        result = []
        self.backtrack(0, result)
        return result

    def backtrack(self, row, result):
        if row == self.n:
            result.append(["".join(row) for row in self.board])
            return

        for col in range(self.n):
            if self.can_place(row, col):
                self.board[row][col] = "Q"
                self.backtrack(row + 1, result)
                self.board[row][col] = "."

    # can place in this row and col
    def can_place(self, row, col):
        # check if the column has a queen
        for i in range(row):
            if self.board[i][col] == "Q":
                return False

        # Check upper-left diagonal has a queen
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == "Q":
                return False

        # or
        # i, j = row - 1, col - 1
        # while i >= 0 and j >= 0:
        #     if self.board[i][j] == "Q":
        #         return False
        #     i -= 1
        #     j -= 1

        # check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == "Q":
                return False

        return True

    def print_chessboard(self):
        result = self.solveNQueens()
        for res in result:
            for row in res:
                print(row)
            print("\n")


sol = NQueens(4)
sol.print_chessboard()

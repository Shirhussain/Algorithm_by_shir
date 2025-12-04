""" 
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, index):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            # visited:
            temp = board[i][j]
            board[i][j] = "#"

            for neighbor in get_neighbors(i, j):
                n_i, n_j = neighbor
                if dfs(n_i, n_j, index+1):
                    return True
            # unvisted
            board[i][j] = temp

            return False

        def get_neighbors(i, j):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            neighbors = []

            for dr, dc in directions:
                new_row, new_col = i+dr, j+dc
                neighbors.append((new_row, new_col))
            return neighbors

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False

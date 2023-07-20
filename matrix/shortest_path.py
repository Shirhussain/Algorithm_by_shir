# Given an n x n binary matrix grid, return the length of the shortest clear path
# in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell
# (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected
# (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.
# Input: grid = [[0,1],[1,0]]
# Output: 2

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1
from collections import deque


def shortest_path_binary_matrix(grid):
    if grid[0][0] == 1:
        return -1

    # (0, 0, 1) is row, co, path_to_go
    q = deque([(0, 0, 1)])

    # ways can go to 8 directions from each cell, (i.e. 0,0)
    ways_can_go = [[-1, 0], [-1, 1], [0, 1],
                   [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    while q:
        curr_row, curr_col, curr_path_count = q.popleft()
        if (curr_row < 0 or curr_col < 0 or
            curr_row > len(grid)-1 or
            curr_col > len(grid[0])-1 or
                grid[curr_row][curr_col] == 1):
            continue

        if curr_row == len(grid)-1 and curr_col == len(grid[0])-1:
            return curr_path_count

        grid[curr_row][curr_col] = 1  # mark as visited
        for go in ways_can_go:
            row, col = go
            q.append((curr_row + row, curr_col + col, curr_path_count + 1))
    return -1


grid = [[0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
        ]

print(shortest_path_binary_matrix(grid))

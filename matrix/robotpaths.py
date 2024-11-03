def robotPaths(matrix):
    # Write your code here
    # moving in for direction row +- col +-

    #                                       (0,0)
    #                              /.    /.    \.   \
    #                           (1,0) (-1,0) (0,1,) (0,-1)
    # .                     /.  /. \ \        /. /\  \
    #                (1,1) (1,-1) (2,0)    (1,1)(-1,1)(0,2)(0,0)

    result = 0

    def traverse(row, col):
        nonlocal result
        # check out of bounce
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
            return

        # check if we visited already
        if matrix[row][col] == 1:
            return

        # check reaching destination
        if row == len(matrix)-1 and col == len(matrix[0])-1:
            result += 1
            return

        # when you visited then cell should become "1"
        matrix[row][col] = 1

        traverse(row-1, col)
        traverse(row+1, col)
        traverse(row, col-1)
        traverse(row, col+1)

        # back track to the place you start and after you went to distention
        # come back and put 0 instead
        matrix[row][col] = 0
    traverse(0, 0)
    return result


# based on key value for mapping
def robotPath(matrix):
    result = 0
    visited = set()

    def traverse(row, col):
        nonlocal result
        key = f'{row}_{col}'
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
            return

        if key in visited:
            return

        if row == len(matrix)-1 and col == len(matrix[0])-1:
            result += 1
            return

        # when I visit then put a key on that cell
        visited.add(key)

        traverse(row-1, col)
        traverse(row+1, col)
        traverse(row, col-1)
        traverse(row, col+1)

        # backtracking
        visited.remove(key)
    traverse(0, 0)
    return result


matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(robotPaths(matrix))


matrix1 = [
    [0, 0],
    [0, 0],
]


matrix2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
print(robotPath(matrix1))
print(robotPath(matrix2))


def robo_path_8_dir(matrix):
    result = 0
    row = len(matrix) - 1
    col = len(matrix[0]) - 1

    def dfs(i, j):
        nonlocal result
        # out of bounds and bas condition
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)}

        # directions = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        if i < 0 or i > row or j < 0 or j > col or matrix[i][j] == 1:
            return

        if i == row and j == col:
            result += 1
            return

        # visit and change to 1 to be counted as visited
        matrix[i][j] = 1

        for dir in directions:
            dfs(i + dir[0], j + dir[1])

        # backtrack
        matrix[i][j] = 0
    dfs(0, 0)
    return result


matrix3 = [
    [0, 0],
    [0, 0],
]

print("roboatpat with 8 dir: ", robo_path_8_dir(matrix3))


def robo_path_with_count(matrix):
    row = len(matrix)-1
    col = len(matrix[0]) - 1

    def dfs(i, j):
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1),
                      (-1, -1), (-1, 1), (1, -1), (1, 1)}
        # base case and boundaries
        if i < 0 or i > row or j < 0 or j > col or matrix[i][j] == 1:
            return 0
        if i == row and col == j:
            return 1

        # visited
        matrix[i][j] = 1

        sum = 0
        for dir in directions:
            sum += dfs(i + dir[0], j + dir[1])
        matrix[i][j] = 0
        return sum

        # or

        # down = dfs(i+1, j)
        # up = dfs(i-1, j)
        # right = dfs(i, j+1)
        # left = dfs(i, j-1)
        # # (-1, -1), (-1, 1), (1, -1), (1, 1)
        # nw = dfs(i-1, j-1)
        # ne = dfs(i-1, j+1)
        # sw = dfs(i+1, j-1)
        # se = dfs(i+1, j+1)

        # # backtrack
        # matrix[i][j] = 0

        # return down + right + left + up + nw + ne + sw + se
    return dfs(0, 0)


matrix5 = [
    [0, 0],
    [0, 0],
]

matrix6 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print("counting: ", robo_path_with_count(matrix5))

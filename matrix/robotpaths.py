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
print(robotPath(matrix1))

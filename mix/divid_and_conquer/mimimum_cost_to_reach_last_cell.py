# minium cost to reach to the last cell in 2D arrays
# 2D matrix is given
# each cell has a cost asociated with for accessing
# we need to start from (0.0) cell and go to (n-1,n-1) cell
# we can go to right or down cell form current cell
# find the way in which the cost is minium


def find_min_cost(twoArray, row, col):
    # it means it's in the end and no way to go
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoArray[0][0]
    else:
        # going form last cell to up because we have to option to go up or left
        option1 = find_min_cost(twoArray, row-1, col)
    # if the they reach to the first cell we need to return the value of fist cell
        option2 = find_min_cost(twoArray, row, col-1)
        return twoArray[row][col] + min(option1, option2)


TowDlist = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3]
]

print(find_min_cost(TowDlist, 4, 4))

# number of path to reach the last cell with the given cost
# problem statment
# 2D matrix is givin
# each cell has cost asociated with it for accessing
# we need to start from (0,0) cell and go till (n-1, n-1) cell
# we can go only to right or down cell from current cell
# we are given total cost to reach to the last cell
# find the number of ways to reach end of matrix with the given "total cost"

def number_of_path(two_D_Array, row, col, cost):
    if cost < 0:
        return 0
    # if it's ond the fist cell
    elif row == 0 and col == 0:
        # if it has a value or not
        if two_D_Array[0][0] - cost == 0:
            return 1
        else:
            return 0
    # if we are at teh first row
    elif row == 0:
        # move from right to left in colomn
        return number_of_path(two_D_Array, 0, col-1, cost - two_D_Array[row][col])
    # if we are at the first column
    elif col == 0:
        # move form bottom to the top
        return number_of_path(two_D_Array, row-1, 0, cost - two_D_Array[row][col])
    else:
        option1 = number_of_path(
            two_D_Array, row-1, col, cost - two_D_Array[row][col])
        option2 = number_of_path(
            two_D_Array, row, col-1, cost - two_D_Array[row][col])
        return option1 + option2


TowDlist = [
    [4, 7, 1, 6],
    [5, 7, 3, 9],
    [3, 2, 1, 2],
    [7, 1, 6, 3],
]


print(number_of_path(TowDlist, 3, 3, 25))

# it means there is two path to reach to teh end

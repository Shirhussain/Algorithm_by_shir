# In each of the examples below, lattice diagrams are provided, along with row/column coordinates.


# Input 1: (2, 3)

#     (2 x 3 lattice of squares)
    
#    0 __1__2__3 
#    1|__|__|__|
#    2|__|__|__|

# Output 1: 10 (number of unique paths from top left corner to bottom right corner)





# Input 2: (2, 2)

#     (2 x 2 lattice of squares)

#    0 __1__2
#    1|__|__|
#    2|__|__|

# (2,2) ==> Output 2: 6 (number of unique paths from top left corner to bottom right corner)


def latticePaths(row, col):
    """
        I'm comming form the destination to the start like (2,2) to (0,0)
        because it's very easy to find outband paths or find edge and base cases
    """
    if row < 0 or col < 0:
        return 0 
    if row == 0 and col == 0:
        return 1 
    up = latticePaths(row -1, col)
    left = latticePaths(row, col-1)
    return left + up 


print(latticePaths(2,2))

# time complexity is (2^m+n)
# A simple Python program to
# find sum of diagonals

# # Driver code
a = [[9, 2, 3, 4],
     [5, 6, 7, 8],
     [1, 2, 3, 4],
     [5, 6, 7, 8]]

# def printDiagonalSums(mat, n):

#     principal = 0
#     secondary = 0
#     for i in range(0, n):
#         for j in range(0, n):

#             # Condition for principal diagonal
#             if (i == j):
#                 principal += mat[i][j]

#             # Condition for secondary diagonal
#             if ((i + j) == (n - 1)):
#                 secondary += mat[i][j]

#     print("Principal Diagonal:", principal)
#     print("Secondary Diagonal:", secondary)


# printDiagonalSums(a, 4)

# # This code is contributed
# # by ihritik


# def diagonal_sum(arr):
#     first = 0
#     second = 0
#     arr_len = len(arr)
#     for i in range(arr_len):
#         for j in range(arr_len):
#             if i == j:
#                 first += arr[i][j]
#             if (i+j) == (arr_len-1):
#                 second += arr[i][j]
#     print("sum of first diagnonal: ", first)
#     print("sum of second diagonal: ", second)

# diagonal_sum(a)
# print(a, )





def printDiagonalSums(mat, n):

    principal = 0
    secondary = 0
    for i in range(n):
        principal += mat[i][i]
        secondary += mat[i][n - i - 1]

    print("Principal Diagonal:", principal)
    print("Secondary Diagonal:", secondary)



# This code is contributed
# by ihritik
# def sumDiagonal(a):
#     sum = 0
#     for i in range(len(a)):
#         sum += a[i][i]
#     return sum

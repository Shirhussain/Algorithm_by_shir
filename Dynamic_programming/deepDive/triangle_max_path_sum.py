""" What are some indicators I should use dynamic Programming?

- Overlapping substructure/subproblems

How do I solve a dynamic programming problem?

- Top-down (recurision + memoization)
- Bottom-up (tabulation)

Write a template for memoizing a function

def fib(n)
	create an int array of n elements called "memo" initialized to "undefined"
  
  def helper(n)
  
  	if n < 2
    	return n
    if memo[n] is underfined
    	set memo[n] to helper(n-1) + helper(n-2)
    return memo[n]
  
  return helper(n)


What is the runtime & space complexity of a memoized recursive function?

Runtime and space: O(n)

memo
[2]: 1
[3]: 2
[4]: 3
[5] :5

helper(5) -> 5
	helper(4) -> 3
  	helper(3) -> 2
    	helper(2) -> 1
      	helper(1) -> 1
        helper(0) -> 0
      helper(1) -> 1
    helper(2) [1]
  helper(3) [2]

helper(5) -> 5
	helper(4) -> 3
  	helper(3) -> 2
    	helper(2) -> 1
      	helper(1) -> 1
        helper(0) -> 0
      helper(1) -> 1
    helper(2) -> 1
    	helper(1) -> 1
      helper(0) -> 0
  helper(3) -> 2
    helper(2) -> 1
      helper(1) -> 1
      helper(0) -> 0
    helper(1) -> 1
    
    
    Problem 1: Triangle
    
                    7
                   /  \
                  3   8
                 / \ /  \
                8   1    0
               / \ /  \ /  \
              2   7    4    4
             / \ / \  / \ /  \
            4   5   2    6    5

[
[7],
[3, 8],
[8, 1, 0],
[2, 7, 4, 4],
[4, 5, 2, 6, 5]
]

If depth of the tree is d
then number of nodes N in the tree is d(d+1)/2 ~ d^2.


Given a number triangle like the one above, calculate the highest sum of 
numbers passed on a route that starts at the top and ends somewhere on the 
bottom. Each step can go either diagonally down to the left of diagonally down to the right.
In terms of indices, if we are at node [i][j], the next node can be either
[i+1][j] or [i+1][j+1].


"""


matrix = [
[7],
[3, 8],
[8, 1, 0],
[2, 7, 4, 4],
[4, 5, 2, 6, 5]
]


matrix_memo = [
    [81],
    [14, 3],
    [94, 35, 31],
    [28, 17, 94, 13],
    [86, 94, 69, 11, 75],
    [54, 4, 3, 11, 27, 29],
    [64, 77, 3, 71, 25, 91, 83],
    [89, 69, 53, 28, 57, 75, 35, 0],
    [97, 20, 89, 54, 43, 35, 19, 27, 97],
    [43, 13, 11, 48, 12, 45, 44, 77, 33, 5],
    [93, 58, 68, 15, 48, 10, 70, 37, 80, 79, 46],
    [73, 24, 90, 8, 5, 84, 29, 98, 37, 10, 29, 12],
    [48, 35, 58, 81, 46, 20, 47, 45, 26, 85, 34, 89, 87],
    [82, 9, 77, 81, 21, 68, 93, 31, 20, 59, 48, 34, 81, 88],
    [71, 28, 87, 41, 98, 99, 7, 29, 4, 40, 51, 34, 8, 27, 72],
    [91, 40, 27, 83, 63, 50, 82, 58, 18, 33, 17, 31, 95, 71, 68, 33],
    [95, 74, 54, 74, 51, 46, 28, 17, 65, 63, 11, 96, 6, 14, 19, 80, 20],
    [87, 54, 76, 8, 49, 48, 76, 59, 67, 32, 70, 1, 87, 92, 14, 87, 68, 96],
    [34, 98, 82, 43, 14, 37, 55, 20, 58, 0, 92, 92, 33, 64, 97, 22, 64, 13, 80],
    [38, 81, 64, 77, 25, 19, 47, 97, 20, 69, 99, 67, 0, 76, 41, 62, 2, 14, 46, 39],
    [30, 7, 30, 72, 10, 10, 93, 62, 8, 97, 68, 98, 16, 16, 84, 60, 70, 21, 33, 67, 77],
    [54, 27, 69, 96, 93, 88, 25, 91, 39, 51, 85, 83, 47, 56, 66, 57, 15, 31, 28, 8, 43, 2],
    [75, 70, 29, 75, 28, 0, 9, 90, 80, 7, 29, 8, 4, 42, 9, 65, 30, 35, 85, 62, 27, 69, 16],
    [92, 73, 73, 60, 31, 60, 52, 24, 12, 12, 84, 55, 45, 54, 52, 59, 93, 6, 86, 83, 82, 12, 7, 51],
    [93, 43, 13, 31, 24, 24, 68, 57, 17, 54, 23, 35, 59, 31, 9, 56, 70, 12, 6, 83, 69, 1, 11, 96, 30],
    [21, 52, 62, 61, 27, 51, 7, 21, 48, 0, 49, 33, 58, 36, 54, 89, 93, 71, 84, 91, 62, 19, 24, 37, 27, 7],
    [74, 94, 69, 7, 95, 40, 7, 6, 74, 61, 64, 67, 20, 7, 65, 10, 23, 8, 76, 8, 86, 30, 51, 15, 72, 31, 74],
    [76, 5, 79, 10, 53, 84, 74, 72, 66, 40, 33, 26, 85, 91, 40, 30, 33, 50, 16, 85, 82, 38, 58, 40, 96, 9, 1, 58],
    [79, 72, 12, 9, 68, 27, 64, 33, 16, 44, 8, 31, 47, 36, 20, 56, 69, 90, 38, 78, 83, 67, 1, 85, 70, 38, 84, 13, 17],
    [33, 14, 13, 95, 70, 19, 34, 36, 77, 26, 91, 43, 26, 87, 81, 33, 64, 62, 32, 6, 11, 81, 54, 35, 5, 0, 42, 98, 16, 81],
    [33, 20, 94, 56, 70, 90, 54, 71, 1, 14, 9, 88, 19, 69, 4, 47, 74, 70, 18, 55, 16, 5, 39, 46, 5, 45, 26, 87, 31, 85, 13],
    [45, 99, 71, 52, 79, 95, 19, 30, 20, 22, 52, 3, 22, 94, 42, 52, 85, 94, 31, 34, 20, 89, 13, 48, 4, 60, 28, 25, 58, 44, 39, 29],
    [28, 3, 84, 24, 51, 42, 35, 8, 98, 35, 44, 82, 65, 51, 86, 68, 42, 3, 14, 33, 22, 74, 33, 4, 13, 76, 55, 44, 93, 40, 55, 77, 65],
    [14, 49, 73, 24, 32, 5, 90, 55, 0, 66, 68, 87, 92, 94, 94, 85, 25, 46, 55, 8, 85, 42, 79, 40, 84, 15, 92, 38, 64, 39, 85, 52, 41, 51],
    [89, 37, 70, 16, 24, 53, 85, 48, 86, 95, 22, 78, 72, 38, 51, 70, 0, 38, 36, 26, 55, 74, 77, 83, 41, 59, 56, 56, 86, 27, 65, 60, 94, 21, 84],
]

def triangle(matrix):
    m = len(matrix)
    n = len(matrix[0])


    def helper(i,j):
        if i == m-1: 
            return matrix[i][j]

        # if you look at the matrix, the child exist in the same column for the left
        #  and other child is in i+1, j+1 next column nad next row. 
        left_child = helper(i+1, j)
        right_child = helper(i+1, j+1)

        return matrix[i][j] + max(left_child, right_child)

    return helper(0,0)

print("value: ", triangle(matrix))



def triangle_memo(matrix):
    m = len(matrix)

    def helper(i,j, memo):
        cell = f"{i}-{j}"
        if cell in memo:
            return memo[cell]

        if i == m-1:
            return matrix[i][j]

        left = helper(i+1, j, memo)
        right = helper(i+1, j+1, memo)

        memo[f"{i}-{j}"] = matrix[i][j] + max(left, right)
        return memo[f"{i}-{j}"]

    return helper(0,0, {})


print(triangle_memo(matrix_memo))




def tiangel_with_matrx(matrix):
    m = len(matrix)
    n = len(matrix)

    for i in range(m-2,-1,-1):
        for j in range(i, -1, -1):
            max_val = max(matrix[i+1][j], matrix[i+1][j+1])
            curr_val = matrix[i][j]
            matrix[i][j] = curr_val + max_val

    return matrix[0][0]

print("matrix solution buttom up ", tiangel_with_matrx(matrix))
            
            

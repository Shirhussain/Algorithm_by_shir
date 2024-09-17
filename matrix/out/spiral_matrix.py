'''
Given an (MxN) (rectangular, not jagged) matrix of integers, return an array in spiral order.


Input: [[1,2,3],
        [4,5,6],
        [7,8,9]]

Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]


Input: [[]]

Output: []

Time Complexity: O(MN)
Auxiliary Space Complexity: O(MN)

The elements are all digits 0 through 9

Input: [[1,2,3,4]]

Output: [1, 2, 3, 4]







Diagram:
         j
i      [[1,2,3],
        [4,5,6],
        [7,8,9]]

i: 0
j: 0

i_start 2
i_end   1
j_start 1
j_end   1

output: [1, 2, 3, 6, 9, 8, 7, 4]

'''
'''

initialize output to []

do "forever":

        set i to istart
        for j from j_start to j_end
                add matrix[i][j] to output
        increment i_start
        if i_start > i_end: break
        
        set j to j_end
        for i from i_start to i_end
                add matrix[i][j] to output
        decrement j_end
        if j_end < j_start: break
        
        set i to i_end
        for j from j_end to j_start
                add matrix[i][j] to output
        decrement i_end
        if i_end < i_start: break
        
        set j to j_start
        for i from i_end to i_start
                add matrix[i][j] to output
        increment j_start
        if j_start > j_end: break

return output
'''

""" 
    input: [1,2,3,4,5]
    output: [-3, -1, 1, 3, 5]
    because index 0 the number is 1 then prefix is 4 --> 1-4 = -3 
    index 1 number is 2 prefix is 3 --> 2-3 = -1
    index 2 number is 3 prefix is 2 --> 3-2 = 1 
    ....
    
    
"""


def distinct_diff(arr):
    return [arr[i] - (len(arr)-(i+1)) for i in range(len(arr))]


lst = [1, 2, 3, 4, 5]
print(distinct_diff(lst))

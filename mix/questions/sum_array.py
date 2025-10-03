def sum_array(arr):
    jam = 0
    for i in arr:
        jam += i 
    return jam 

arr = [12, 3, 4, 15]
# print(sum_array([1,2,3]))
print(sum_array(arr))      

# or
print(sum(arr))

array = [100, 10, 5, 25, 35, 14]

def multipication(arr,n):
    zarb = 1 
    for i in arr:
        zarb *= i 
    print(zarb%n)


print(multipication(array,11))




# or 


from functools import reduce

arr = [100, 10, 5, 25, 35, 14]


def reminder(arr, n):
    result = reduce(lambda x,y: x*y, arr)
    print(result%n)
    
    
reminder(arr,11)

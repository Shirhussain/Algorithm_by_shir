def keyob(n):
    new_num = 0 
    for i in range(n+1):
        result = pow(i,3)
        new_num += result
    return new_num

print(keyob(5))
    
        
        
# or

def cube(n):
    return (n *( n + 1 ) // 2) ** 2 
    
print(cube(5))
    

# or
# Efficient Python program to find sum of cubes
# of first n natural numbers that avoids
# overflow if result is going to be withing
# limits.
 
# Returns the sum of series
def sumOfSeries(n):
    x = 0
    if n % 2 == 0 :
        x = (n/2) * (n+1)
    else:
        x = ((n + 1) / 2) * n
         
    return (int)(x * x)
 
  
# Driver Function
n = 5
print(sumOfSeries(n))

# Python Program for Sum of squares of first n natural numbers
# Input : N = 4
# Output : 30
# 12 + 22 + 32 + 42
# = 1 + 4 + 9 + 16
# = 30

# Input : N = 5
# Output : 55


def natural_number_sequance(num):
    new_num = 0
    for i in range(num+1):
        result = i**2 
        new_num += result
    return new_num
    
print(natural_number_sequance(4))



# Sum of Squares Formula for “n” numbers = 12 + 22 + 32 ……. n2 = [n(n + 1)(2n + 1)] / 6

def sum_square_natural_num(n):
    result = (n*(n + 1)*(2*n + 1)) // 6
    return result 

print(sum_square_natural_num(4))



# Avoiding early overflow:
# For large n, the value of (n * (n + 1) * (2 * n + 1)) would overflow. We can avoid overflow up to some extent using the fact that n*(n+1) must be divisible by 2.

# Python Program to find sum of square of first
# n natural numbers. This program avoids
# overflow upto some extent for large value
# of n.y
  
def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
  
# main()
n = 4
print(squaresum(n));
  
# Code Contributed by Mohit Gupta_OMG <(0_o)>

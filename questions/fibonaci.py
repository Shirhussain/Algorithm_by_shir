def fib(num):
    if num < 0:
        return 
    if num == 0 or num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(6))




#or 
# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi


#or 

# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci numbers as 0 and 1

FibArray = [0, 1]

def fibonacci(n):
	if n<0:
		print("Incorrect input")
	elif n<= len(FibArray):
		return FibArray[n-1]
	else:
		temp_fib = fibonacci(n-1)+fibonacci(n-2)
		FibArray.append(temp_fib)
		return temp_fib

# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi





#or 
# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
	a = 0
	b = 1
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return a
	elif n == 1:
		return b
	else:
		for i in range(2, n):
			c = a + b
			a = b
			b = c
		return b

# Driver Program

print(fibonacci(9))

# This code is contributed by Saket Modi



def fibonaci(n):
    a = 0
    b = 1 
    for i in range(n+1):
        yield a 
        a,b = b, a+b 
        
print(list(fibonaci(9)))


#Python Program for nth multiple of a number in Fibonacci Series



#Input: k = 2, n = 3
#Output: 9, 3rd multiple of 2 in Fibonacci Series is 34 that appears at position 9.

#Input: k = 4, n = 5 
#Output: 30, 5th multiple of 5 in Fibonacci Series is 832040 which appears at position 30.
def find_position(k, n):
    a = 0 
    b = 1 
    i =2 
    while i != 0:
        c = a +b 
        a = b 
        b = c 
        if b % k == 0:
            return n*i 
        i += 1 
    return 

print(find_position(4,5))


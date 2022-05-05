def fib(num):
    if num < 0:
        return "Incorrect number just positive is accepted"
    elif num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

print(fib(10))

# or

def fib(num):
    if num < 0:
        return "Incorrect number just positive is accepted"
    elif num <2:
        return num
    else:
        return fib(num-1) + fib(num-2)

print(fib(0))
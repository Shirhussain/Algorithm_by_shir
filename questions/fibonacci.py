def find_n_fib(n):
    result = [0,1]
    def helper(i):
        if i > n:
            return 
        result.append(result[i-2]+result[i-1])
        helper(i+1)
    
    helper(2)
    return result
print(find_n_fib(10))


def fib(n):
    if n < 0:
        return 
    return n if n < 2 else fib(n-1) + fib(n-2)

print(fib(10))

    
from functools import cache, lru_cache

@cache
def fib_cache(n):
    if n == 0 or n == 1:
        return 1
    return fib_cache(n-1) + fib_cache(n-2)

print(fib_cache(40))

# or pass a memo 

def fib_memo(n, memo):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1 
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

print(fib_memo(40,{}))



fibonacciCache = {} # Create the global cache.
def fibonacci(nthNumber, indent=0):
    global fibonacciCache
    indentation = '.' * indent
    print(indentation + 'fibonacci(%s) called.' % (nthNumber))
    
    if nthNumber in fibonacciCache:
        # If the value was already cached, return it.
        print(indentation + 'Returning memoized result: %s' % (fibonacciCache[nthNumber]))
        return fibonacciCache[nthNumber]
    
    if nthNumber == 1 or nthNumber == 2:
        # BASE CASE
        print(indentation + 'Base case fibonacci(%s) returning 1.' % (nthNumber))
        fibonacciCache[nthNumber] = 1 # Update the cache.
        return 1
    else:
        # RECURSIVE CASE
        print(indentation + 'Calling fibonacci(%s) (nthNumber - 1).' % (nthNumber - 1))
        result = fibonacci(nthNumber - 1, indent + 1)
        print(indentation + 'Calling fibonacci(%s) (nthNumber - 2).' % (nthNumber - 2))
        result = result + fibonacci(nthNumber - 2, indent + 1)
        print('Call to fibonacci(%s) returning %s.' % (nthNumber, result))
        fibonacciCache[nthNumber] = result # Update the cache.
        return result
print(fibonacci(10))
print(fibonacci(10))



@lru_cache
def fib_cache(n):
    if n == 0 or n == 1:
        return 1
    return fib_cache(n-1) + fib_cache(n-2)

print(fib_cache(40))
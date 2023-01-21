def fib_memo(n, memo):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


my_dic = {}
print(fib_memo(10, my_dic))

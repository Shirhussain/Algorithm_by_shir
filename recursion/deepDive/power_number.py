
def is_Even(n):
    return n % 2 == 0

def is_Odd(n):
    return not is_Even(n)

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        # x^n = 1/x^-n
        return 1 / power(x, -n)
    if is_Odd(n):
        # x^n = x*x^n-1
        return x * power(x, n - 1)
    if is_Even(n):
        # x^n = x^n = x^n/2*x^n/2
        result = power(x, n // 2)
        return result * result


print(power(2, 4))  # Output: 0.0625




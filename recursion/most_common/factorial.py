def find_factorial(n):
    return 1 if n == 0 else n * find_factorial(n-1)


print(find_factorial(5))


def fib(n):
    if n < 0:
        return " please input only positive numbers"
    if n == 0:
        return 0
    result = [0] * n

    result[0] = 0
    result[1] = 1
    for i in range(2, n):
        result[i] = result[i-1] + result[i-2]
    return result


print(fib(10))


def reverse_string(string):
    result = ''

    # def helper(i):
    #     nonlocal result
    #     if i == len(string) - 1:
    #         return
    #     result += string[i]
    #     print(result)
    #     helper(i+1)
    # helper(0)

    def helper(i):
        nonlocal result
        if i < 0:
            return
        result += string[i]
        helper(i-1)

    helper(len(string)-1)
    return result


sentences = "I love you so much "
print(reverse_string(sentences))


# Implement a recursive function to find the sum of all elements in a list.
# 1234
# 1234 % 10 = 4 + 3 + 2 + 1


def sum_up(num):
    result = 0
    temp = num
    while temp > 0:
        result += temp % 10
        temp = temp // 10
    return result


print(sum_up(1234))

# or


def sum_recursive(numbers):
    result = 0

    def helper(num):
        nonlocal result
        if num <= 0:
            return
        result += num % 10
        helper(num//10)
    helper(numbers)
    return result


print(sum_recursive(1234))

# or


def sum_of_recurs(n):
    return 0 if n == 0 else n % 10 + sum_of_recurs(n//10)


print(sum_of_recurs(1234))


# Create a recursive function to find the maximum value in a list of integers.
def find_max_recursive(numbers):
    result_max = float('-inf')

    def helper(i):
        nonlocal result_max
        if i >= len(numbers):
            return
        if numbers[i] >= result_max:
            result_max = numbers[i]
        helper(i+1)
    helper(0)
    return result_max


nums = [1, 5, 7, 10, 0, -10, 1, -100, 13, 2, 7, 9]
print(find_max_recursive(nums))


# Solve the classic "Towers of Hanoi" problem using recursion.
def towers_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n - 1, auxiliary, target, source)


# Test the function
towers_of_hanoi(3, 'A', 'C', 'B')

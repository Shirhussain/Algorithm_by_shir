""" 
you have to multiply two numbers without using the * operator and the loop is not allowed to use.
"""


def multiply(a, b):
    if a == 0:
        return 0
    return multiply(a-1, b) + b


print(multiply(3, 4))

""" 
it should work for negative numbers as well.
"""


def multiply_negative(a, b):
    if a < 0:
        return -multiply_negative(-a, b)
    if b < 0:
        return -multiply_negative(a, -b)
    if a == 0:
        return 0
    return multiply_negative(a-1, b) + b


print(multiply_negative(-3, -4))


# some the odd number in a list

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sum_odd_list(arr):
    return odd_sum(arr, 0)


def odd_sum(arr, index):
    if index == len(arr):
        return 0
    if arr[index] % 2 != 0:
        return arr[index] + odd_sum(arr, index + 1)
    else:
        return odd_sum(arr, index + 1)


print(sum_odd_list(arr))


#  product of all even numbers in a list

arr = [1, 2, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def product_even_list(arr):
    return product_even(arr, 0)


def product_even(arr, index):
    if index == len(arr):
        return 1
    if arr[index] % 2 == 0:
        return product_even(arr, index + 1) * arr[index]
    else:
        return product_even(arr, index + 1)


print(product_even_list(arr))


# reverse a string

def reverse_string_iterative(string):
    value = ""
    for i in range(len(string)-1, -1, -1):
        value += string[i]
    return value


print(reverse_string_iterative("hello"))


def reverse_string_recursive(string, index):
    if index == len(string):
        return ""
    return reverse_string_recursive(string, index + 1) + string[index]


""" 
call stack:
    [
    reverse_string_recursive(string, index + 1) + string[index] -> o
    reverse_string_recursive(string, index + 1) + string[index] -> l
    reverse_string_recursive(string, index + 1) + string[index] -> l
    reverse_string_recursive(string, index + 1) + string[index] -> e
    reverse_string_recursive(string, index + 1) + string[index] -> h
    ]
"""

print(reverse_string_recursive("hello", 0))


# reverse a string using recursion another way

def reverse_string(string):
    if len(string) <= 1:
        return string
    left = string[0]
    right = string[-1]
    return right + reverse_string(string[1:-1]) + left


print(reverse_string("shir danishyar"))


# is palindrome using recursion

def is_palindrome(string):
    return string == reverse_string(string)


# is palindrome using recursion another way

def is_palindrome_another_way(string):
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


print(is_palindrome("racecar"))
print(is_palindrome("shir danishyar"))
print(is_palindrome_another_way("racecar"))
print(is_palindrome_another_way("12321"))


# find the maximum number in a list using recursion

def find_max(arr):
    # return max_number(arr, 0)
    return find_max_another_way(arr, 0)


def max_number(arr, index):
    if index == len(arr):
        return 0
    return max(arr[index], max_number(arr, index + 1))


def find_max_another_way(arr, index):
    if index == len(arr):
        return None, None
    best_max, best_index = find_max_another_way(arr, index + 1)
    if best_max is None or arr[index] > best_max:
        return arr[index], index
    return best_max, best_index


print(find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# factorial:

def factorial(n):
    return 1 if n in [0, 1] else n * factorial(n-1)


print(factorial(3))


def fib(n):
    if n <= 0:
        return 0
    return 1 if n == 1 else fib(n-1) + fib(n-2)


print(fib(9))


def sum_of_digits_of_numbers(n):
    """
    Sum of digit of a number using recursion

    Input : 12345
    Output : 15

    Input : 45632
    Output :20
    """

    return 0 if n == 0 else n % 10 + sum_of_digits_of_numbers(n // 10)


num = 12345

print(sum_of_digits_of_numbers(num))


# Power Function: Create a recursive function to calculate the exponentiation of a base

def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent-1)


print(power(2, 10))


# Binary Search: Implement a recursive binary search function
# to find an element in a sorted array.

def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    def helper(arr, l, r):
        if l > r:
            return -1
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            return helper(arr, l, mid - 1)
        else:
            return helper(arr, mid+1, r)
    return helper(arr, l, r)


arr = [1, 2, 10, 16, 90, 100]
target = 90
print(binary_search(arr, target))


# Merge Sort: Write a recursive function to perform
# the merge sort algorithm on an array.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


arr = [1, 5, 2, 9, -2, -30, 100]
print(merge_sort(arr))


# Tower of Hanoi:

"""
The rules of the Tower of Hanoi are as follows:
    Only one disk can be moved at a time.
    A disk can only be placed on top of a larger disk or an empty peg.
    No disk can be placed on top of a smaller disk.

general steps of problem solving
    let f(n) be recursive function 
    1. show f(1) works as base case ---> if you put 1 
    2. Assume f(n-1) works
    3. show f(n) works by using f(n-1)
    
    
Strategy: move top 3 disk to road 2 
        move largest disk to road 3 
        move top 3 disk from road 2 to road 3 
        
    Moving 3 disks from peg 1 to peg 3 using the other peg:
    1  -->  3
    1  -->  2
    3  -->  2
    1  -->  3
    2  -->  1
    2  -->  3
    1  -->  3
"""


def hanoi(n, start, end):
    if n == 1:
        show(start, end)
    else:
        other = 6 - (start + end)
        hanoi(n-1, start, other)
        show(start, end)
        hanoi(n-1, other, end)


def show(start, end):
    print(start, " --> ", end)


hanoi(3, 1, 3)


def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Example usage with 3 disks and pegs named A, B, and C
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')

# for short


# for short
def h(n, s, ax, d):
    if n == 1:
        return
    h(n-1, s, d, ax)
    h(n-1, ax, s, d)


print(h(3, 'A', 'B', 'C'))


# Palindrome:
def is_palindrome(string):
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])


s = "racecar"
print(is_palindrome(s))


# Subset Sum: Given a set of integers and a target sum,
# find all possible subsets that add up to the target sum using recursion.


def find_subsets_with_sum(nums, target_sum):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(nums)):
            if nums[i] <= target:
                backtrack(i + 1, target - nums[i], path + [nums[i]])

    result = []
    backtrack(0, target_sum, [])
    return result


# Counting Paths: Given a grid with obstacles, find the number
# of possible paths from the top-left to the bottom-right using recursion.

def count_path(grid, row, col):
    if row == len(grid)-1 and col == len(grid[0])-1:
        return 1
    if row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 1:
        return 0
    return count_path(grid, row + 1, col) + count_path(grid, row, col + 1)


grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(count_path(grid, 0, 0))

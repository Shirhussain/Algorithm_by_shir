def binarySearch(needle, haystack, left=None, right=None):
    # By default, `left` and `right` are all of `haystack`:
    if left is None:
        left = 0 # `left` defaults to the 0 index.
    if right is None:
        right = len(haystack) - 1 # `right` defaults to the last index.
    print('Searching:', haystack[left:right + 1])
    if left > right: # BASE CASE
        return None # The `needle` is not in `haystack`.
    mid = (left + right) // 2
    if needle == haystack[mid]: # BASE CASE
        return mid # The `needle` has been found in `haystack`
    elif needle < haystack[mid]: # RECURSIVE CASE
        return binarySearch(needle, haystack, left, mid - 1)
    elif needle > haystack[mid]: # RECURSIVE CASE
        return binarySearch(needle, haystack, mid + 1, right)
print(binarySearch(13, [1, 4, 8, 11, 13, 16, 19, 19]))


import random
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    
    less_than = []
    equal_to = []
    greater_than = []
    
    for num in arr:
        if num < pivot:
            less_than.append(num)
        elif num > pivot:
            greater_than.append(num)
        else:
            equal_to.append(num)
    
    return quickSort(less_than) + [pivot] + quickSort(greater_than)

print("result of quick sort: ", quickSort([1,10,3,2,9,-1,17,100]))

def quickSort_2(arr):
    if len(arr) <= 1:
        return arr 
    pivot = random.choice(arr)
    return (
            quickSort_2([num for num in arr if num < pivot]) 
            + [num for num in arr if num == pivot] 
            + quickSort([num for num in arr if num > pivot])
            )

print("result quick sort: ", quickSort_2([1,10,3,2,9,-1,17,100]))            


def quicksort(items, left=None, right=None):
    # By default, `left` and `right` span the entire range of `items`:
    if left is None:
        left = 0 # `left` defaults to the 0 index.
    if right is None:
        right = len(items) - 1 # `right` defaults to the last index.
    print('\nquicksort() called on this range:', items[left:right + 1])
    print('................The full list is:', items)
    if right <= left:
        # With only zero or one item, `items` is already sorted.
        return # BASE CASE
    
    # START OF THE PARTITIONING
    i = left # i starts at the left end of the range.
    pivotValue = items[right] # Select the last value for the pivot.
    print('....................The pivot is:', pivotValue)
    
    # Iterate up to, but not including, the pivot:
    for j in range(left, right):
        # If a value is less than the pivot, swap it so that it's on the
        # left side of `items`:
        if items[j] <= pivotValue:
            # Swap these two values:
            items[i], items[j] = items[j], items[i]
            i += 1
    # Put the pivot on the left side of `items`:
    items[i], items[right] = items[right], items[i]
    # END OF THE PARTITIONING
    print('....After swapping, the range is:', items[left:right + 1])
    print('Recursively calling quicksort on:', items[left:i], 'and', items[i + 1:right + 1])
    # Call quicksort() on the two partitions:
    quicksort(items, left, i - 1) # RECURSIVE CASE
    quicksort(items, i + 1, right) # RECURSIVE CASE
    
myList = [0, 7, 6, 3, 1, 2, 5, 4]
quicksort(myList)
print(myList)



def merge_sor(arr):
    # divide in half each time, tell you get to the bae case
    # then start merging
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2 
    
    left = merge_sor(arr[:mid])
    right = merge_sor(arr[mid:])
    
    return merge(left, right)

def merge(left_half, right_half):
    l=r = 0
    result = []
    
    while l < len(left_half) and r < len(right_half):
        if left_half[l] > right_half[r]:
            result.append(right_half[r])
            r += 1
        else:
            result.append(left_half[l])
            l += 1
    
    result.extend(left_half[l:])
    result.extend(right_half[r:])
    return result
        
            

print("this is merge sort: ", merge_sor([0, 7, 6, 3, 1, 2, 5, 4]))



import math
def mergeSort(items):
    print('.....mergeSort() called on:', items)
    # BASE CASE - Zero or one item is naturally sorted:
    if len(items) == 0 or len(items) == 1:
        return items
    
    # RECURSIVE CASE - Pass the left and right halves to mergeSort():
    # Round down if items doesn't divide in half evenly:
    iMiddle = math.floor(len(items) / 2)
    print('................Split into:', items[:iMiddle], 'and', items[iMiddle:])
    left = mergeSort(items[:iMiddle])
    right = mergeSort(items[iMiddle:])
    
    # BASE CASE - Returned merged, sorted data:
    # At this point, left should be sorted and right should be
    # sorted. We can merge them into a single sorted list.
    sortedResult = []
    iLeft = 0
    iRight = 0
    while (len(sortedResult) < len(items)):
        # Append the smaller value to sortedResult.
        if left[iLeft] < right[iRight]:
            sortedResult.append(left[iLeft])
            iLeft += 1
        else:
            sortedResult.append(right[iRight])
            iRight += 1
            
        # If one of the pointers has reached the end of its list,
        # put the rest of the other list into sortedResult.
        if iLeft == len(left):
            sortedResult.extend(right[iRight:])
            break
        elif iRight == len(right):
            sortedResult.extend(left[iLeft:])
            break
        print('The two halves merged into:', sortedResult)
    return sortedResult # Returns a sorted version of items.
myList = [2, 9, 8, 5, 3, 4, 7, 6]
myList = mergeSort(myList)
print(myList)


def sumDivConq(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2 
    # dive in half tell you get to the base case
    left = sumDivConq(arr[:mid])
    right = sumDivConq(arr[mid:])
    
    return sum_arr(left, right)
    
    # sum left and right 

def sum_arr(left_half, right_half):
    result = 0
    l=r=0
    
    while l < len(left_half) and r < len(right_half):
        result += left_half[l]
        result += right_half[r]
        l +=1
        r += 1
        
    while l < len(left_half):
        result+= left_half[l]
        l +=1 
    while r < len(right_half):
        result += right_half[r]
        r += 1
    return [result]

print("sum of divide and conquer:", sumDivConq([1, 2, 3, 4, 5]))

def sumDivConq(numbers):
    if len(numbers) == 0: # BASE CASE
        return 0
    elif len(numbers) == 1: # BASE CASE
        return numbers[0]
    else: # RECURSIVE CASE
        mid = len(numbers) // 2
        leftHalfSum = sumDivConq(numbers[0:mid])
        rightHalfSum = sumDivConq(numbers[mid:len(numbers) + 1])
        return leftHalfSum + rightHalfSum

nums = [1, 2, 3, 4, 5]
print('The sum of', nums, 'is', sumDivConq(nums))
nums = [5, 2, 4, 8]
print('The sum of', nums, 'is', sumDivConq(nums))
nums = [1, 10, 100, 1000]
print('The sum of', nums, 'is', sumDivConq(nums))




import math
# Create a lookup table of all single-digit multiplication products:
MULT_TABLE = {}
for i in range(10):
    for j in range(10):
        MULT_TABLE[(i, j)] = i * j
        
def padZeros(numberString, numZeros, insertSide):
    """Return a string padded with zeros on the left or right side."""
    if insertSide == 'left':
        return '0' * numZeros + numberString
    elif insertSide == 'right':
        return numberString + '0' * numZeros
    
def karatsuba(x, y):
    """Multiply two integers with the Karatsuba algorithm. Note that
    the * operator isn't used anywhere in this function."""
    assert isinstance(x, int), 'x must be an integer'
    assert isinstance(y, int), 'y must be an integer'
    x = str(x)
    y = str(y)
    # At single digits, look up the products in the multiplication table:
    if len(x) == 1 and len(y) == 1: # BASE CASE
        print('Lookup', x, '*', y, '=', MULT_TABLE[(int(x), int(y))])
        return MULT_TABLE[(int(x), int(y))]
    
    # RECURSIVE CASE
    print('Multiplying', x, '*', y)
    # Pad with prepended zeros so that x and y are the same length:
    if len(x) < len(y):
        # If x is shorter than y, pad x with zeros:
        x = padZeros(x, len(y) - len(x), 'left')
    elif len(y) < len(x):
        # If y is shorter than x, pad y with zeros:
        y = padZeros(y, len(x) - len(y), 'left')
        
    # At this point, x and y have the same length.
    halfOfDigits = math.floor(len(x) / 2)
    # Split x into halves a & b, split y into halves c & d:
    a = int(x[:halfOfDigits])
    b = int(x[halfOfDigits:])
    c = int(y[:halfOfDigits])
    d = int(y[halfOfDigits:])
    # Make the recursive calls with these halves:
    step1Result = karatsuba(a, c) # Step 1: Multiply a & c.
    step2Result = karatsuba(b, d) # Step 2: Multiply b & d.
    step3Result = karatsuba(a + b, c + d) # Step 3: Multiply a + b & c + d.
    # Step 4: Calculate Step 3 - Step 2 - Step 1:
    step4Result = step3Result - step2Result - step1Result
    # Step 5: Pad these numbers, then add them for the return value:
    step1Padding = (len(x) - halfOfDigits) + (len(x) - halfOfDigits)
    step1PaddedNum = int(padZeros(str(step1Result), step1Padding, 'right'))
    step4Padding = (len(x) - halfOfDigits)
    step4PaddedNum = int(padZeros(str(step4Result), step4Padding, 'right'))
    print('Solved', x, 'x', y, '=', step1PaddedNum + step2Result + step4PaddedNum)
    return step1PaddedNum + step2Result + step4PaddedNum
# Example: 1357 x 2468 = 3349076
print('1357 * 2468 =', karatsuba(1357, 2468))
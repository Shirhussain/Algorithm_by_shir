# 852. Peak Index in a Mountain Array

# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

# Return the index of the peak element.

# Your task is to solve it in O(log(n)) time complexity.


# Example 1:

# Input: arr = [0,1,0]

# Output: 1

# Example 2:

# Input: arr = [0,2,1,0]

# Output: 1

# Example 3:

# Input: arr = [0,10,5,2]

# Output: 1


def peak_index(arr):
    left, right = 0, len(arr)-1

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        elif arr[mid] > arr[mid+1]:
            right = mid
    return left or right


arr = [0, 10, 5, 2]
print(peak_index(arr))

# this video is also great.   https://youtu.be/jx0JBHsx53U?list=PL7g1jYj15RUOjoeZAJsWjwV8XUo9r0hwc

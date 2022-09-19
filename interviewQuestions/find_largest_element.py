# my solution

arr = [200, 10, 20, 400, 100]

n = len(arr)
max = arr[0]
for i in range(1,n):
    if arr[i] > max:
        max = arr[i]
print(max)


# Python3 program to find maximum
# in arr[] of size n

# python function to find maximum
# in arr[] of size n


def largest(arr, n):

	# Initialize maximum element
	max = arr[0]

	# Traverse array elements from second
	# and compare every element with
	# current max
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

# This code is contributed by Smitha Dinesh Semwal




# or

arr = [10, 324, 45, 90, 98, 200]
def largest(arr):
    return max(arr)

print(largest(arr))



# or jsut 
max(arr)


arr = [10, 324, 45, 90, 98, 200]

sorted(arr)

print(arr[-1])

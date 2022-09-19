# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

new_arr = [1, 2, 3, 4, 5, 6, 7]
# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
arr_len = len(new_arr)

def shift_arr(arr, d, n):
    temp_arr = []
    for i in range(d):
        temp_arr.append(arr[i])
    next_arr = []
    for i in range(d, n):
        next_arr.append(arr[i])
    
    next_arr.extend(temp_arr)
    print(next_arr)

shift_arr(new_arr, 2, arr_len)

# or
# function to rotate array by d elements using temp array
def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr


# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))

# this code is contributed by Anabhra Tyagi






# or
#Function to left rotate arr[] of size n by d*/
def leftRotate(arr, d, n):
	for i in range(d):
		leftRotatebyOne(arr, n)

#Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):
	temp = arr[0]
	for i in range(n-1):
		arr[i] = arr[i+1]
	arr[n-1] = temp
		

# utility function to print an array */
def printArray(arr,size):
	for i in range(size):
		print ("%d"% arr[i],end=" ")


# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

# This code is contributed by Shreyanshi Arun


# or

#Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
	for i in range(gcd(d,n)):
		
		# move i-th values of blocks
		temp = arr[i]
		j = i
		while 1:
			k = j + d
			if k >= n:
				k = k - n
			if k == i:
				break
			arr[j] = arr[k]
			j = k
		arr[j] = temp

#UTILITY FUNCTIONS
#function to print an array
def printArray(arr, size):
	for i in range(size):
		print ("%d" % arr[i], end=" ")

#Function to get gcd of a and b
def gcd(a, b):
	if b == 0:
		return a;
	else:
		return gcd(b, a%b)

# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

# This code is contributed by Shreyanshi Arun


# or
# Python program using the List
# slicing approach to rotate the array
def rotateList(arr,d,n):
arr[:]=arr[d:n]+arr[0:d]
return arr
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr)))

# this code is contributed by virusbuddah

# https://www.geeksforgeeks.org/python-program-for-program-for-array-rotation-2/

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)


my_list = [2, 20, 1, 7, 0, 3, 13, 14, 15, 16]

bubble_sort(my_list)


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


selection_sort(my_list)


def insertion_sort(arr):
    for i in range(len(arr)):
        # current element is
        key = arr[i]
        # previous element before the key
        j = i-1
        # if current element is < than previous element then we change the position
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
        arr[j+1] = key
    # print(arr)
    return arr


insertion_sort(my_list)


def bucket_sort(custom_list):
    # with this system we create a bucket best on the following formula
    import math
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    array = [[] for _ in range(number_of_buckets)]
    for j in custom_list:
        index_b = math.ceil(j*number_of_buckets/max_value)
        # then we insert element inside the appropriate bucket
        # which start from zero
        array[index_b-1].append(j)
    for i in range(number_of_buckets):
        # then we need to sort element inside each bucket based on one of sorting algorithm.
        array[i] = insertion_sort(array[i])

    # then to merge this bucket we should do this.
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(array[i])):
            custom_list[k] = array[i][j]
            k += 1
    return custom_list


print(bucket_sort(my_list))


# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


# Driver code to test above
# arr = [12, 11, 13, 5, 6, 7]
n = len(my_list)

mergeSort(my_list, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    # print("%d" % my_list[i], end=" ")
    print(my_list[i], end=" ")


# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


# ================================================================= HeapSort==

def heapify(arr, number, index):
    smallest = index
    left = 2*index + 1
    right = 2*index + 2
    if left < number and arr[left] < arr[smallest]:
        smallest = left
    if right < number and arr[right] < arr[smallest]:
        smallest = right
    # if smallest is not eql to root
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        heapify(arr, number, smallest)


def heap_sort(array):
    n = len(array)
    # go down up to 0, first we need heapify it. which is min heap
    for i in range(int(n/2)-1, -1, -1):
        heapify(array, n, i)

    # after that we need to extract from heapify then it will automatically sorted
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    array.reversed()


print(heap_sort(my_list))

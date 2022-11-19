def binary_search(array, value):
    end = len(array)-1
    start = 0
    middle = (start + end)//2
    while not (array[middle] == value) and start < end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end)//2
    if array[middle] == value:
        return middle
    else:
        return -1


my_list = [1, 3, 5, 7, 9, 13, 15, 17, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

print(binary_search(my_list, 20))

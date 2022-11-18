def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return f"this is the index for your search {i}"
    return None


print(linear_search([1, 2, 33, 44, 23, 45, 63, 5, 37, 3, 7, 7, 567, 10], 5))

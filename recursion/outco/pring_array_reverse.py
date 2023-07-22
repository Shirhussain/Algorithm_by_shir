l = [1, 2, 4, 6]


def recursive(l):
    if len(l) == 0:
        return []  # base case
    else:
        return [l.pop()] + recursive(l)  # recusrive case


print(recursive(l))


def print_array_recursive(arr):
    if not arr:  # Base case: the array is empty
        return
    else:
        print(arr[0])  # Print the first element (head)
        # Recursive call with the remaining elements (tail)
        print_array_recursive(arr[1:])


# Example usage
my_array = [1, 2, 3, 4, 5]
print_array_recursive(my_array)


def rec_array(arr):
    if not arr:
        return
    rec_array(arr[1:])
    return arr


print(rec_array(my_array))

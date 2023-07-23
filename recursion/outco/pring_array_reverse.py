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


def reverse_str(string):
    result = ''

    def helper(index):
        nonlocal result
        if index < 0:
            return
        result += string[index]
        helper(index-1)
    helper(len(string)-1)

    return result


my_str = "Just do it!"
print(reverse_str(my_str))


def print_array_pairs(arr, i=0):
    """
    input: [1,2,3,4,5,6,7,8, 9]
    output: [[1,2], [3,4], [5,6], [7,8], [9,-1]]
    """
    result = []
    if i >= len(arr):
        return result
    pair = [arr[i], arr[i+1] if i+1 < len(arr) else -1]
    result.append(pair)
    return result + print_array_pairs(arr, i+2)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(print_array_pairs(l))


def print_arr_pairs(arr):
    result = []

    def traverse(i):
        if i >= len(arr):
            return result
        pair = [arr[i], -1]
        if i+1 < len(arr):
            pair[1] = arr[i+1]
        result.append(pair)
        traverse(i+2)
    traverse(0)
    return result


print(print_arr_pairs(l))

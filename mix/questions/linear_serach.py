from unittest import result


def linear_search(array_list, my_index):
    """
        find the index of number in a list
    """

    for i in range(0, len(array_list)):
        if array_list[i] == my_index:
            return i
    return None


def veryfiy(index_in_array):
    if index_in_array is not None:
        print("Index of this emement for theis array is: ", index_in_array)
    else:
        print("index is not found")

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

result = linear_search(my_list, 3)
veryfiy(result)
def binary_search(list_array, target):
    first = 0
    last = len(list_array)-1
    while first <= last:
        mid = (first + last)//2
        if list_array[mid] == target:
            return mid
        elif list_array[mid] < target:
            first = mid +1
        else:
            last = mid -1
    return None


my_list = [1,2,3,5,55,99,10,100,1000]

def verfiy(binary_search_fn):
    if binary_search_fn is not None:
        print("the target finde in index of ", binary_search_fn)
    else:
        print("target not found")

result = binary_search(my_list, 0)

verfiy(result)


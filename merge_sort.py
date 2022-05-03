def merge_sort(my_lsit):
    """
    sort the list in assinding order
    Return a new sorted list

    Divid: Find the mid point of the list and divid in into the sublist
    conqure: Recursively sort the sublist created in previous steps
    Combine: Merge the sorted sublist created in previous steps.
    Takes O(n log n) time.
    """
    if len(my_lsit) <=1:
        return my_lsit

    left_half, right_half = split(my_lsit)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(my_lsit):
    """
    Divide the unsorted list at midpoint in to too sublist left and right
    Takes over all O(log n) time.
    """
    mid = len(my_lsit)//2
    left = my_lsit[:mid]
    right = my_lsit[mid:]
    return left, right

def merge(left, right):
    """
    Merge to list and sorting them in the process
    then Return the new Merged list
    
    Runs in overall O(n) time.
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j +=1

    #the above merge sorte is work as long as it's even number of item in the list
    # if that's not the case we to implement this two more "while loop".
    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1
    return l

your_list = [11,22,0,3,17,100,9,12,11,11]

mlist = merge_sort(your_list)

def verify_sorted(list):
    len_list = len(list)
    if len_list in {0, 1}:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])

print(mlist)
print(verify_sorted(mlist))




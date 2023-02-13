def recursive_binary_search(listha, target):
    if len(listha) == 0:
        return False
    else:
        mid = len(listha)//2
        if listha[mid] == target:
            return True
        elif listha[mid] > target:
            return recursive_binary_search(listha[:mid], target)
        else:
            return recursive_binary_search(listha[mid+1:], target)


our_list = [1,2,3,4,5,66,77,88,90,100,1000]
result = recursive_binary_search(our_list, 3)

def verfiy(inx):
    print("target found: ", inx)

verfiy(result)



def non_repeating(arr):
    not_repeat = []
    for n in arr:
        if n in not_repeat:
            not_repeat.pop(not_repeat.index(n))
        else:
            not_repeat.append(n)
    return not_repeat

print(non_repeating([1, 1, 1, 5, 2, 1, 3, 4, 2]))


def counter(arr):
    mp = {}
    for n in arr:
        if n in mp:
            mp[n]+= 1
        else:
            mp[n]= 1
    for num in mp:
        if mp[num] == 1:
            yield num

print(list(counter([1, 1, 1, 5, 2, 1, 3, 4, 2])))


def count(arr):
    len_arr = len(arr)
    visited = [False for _ in range(len_arr)]
    for i in range(len_arr):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1, len_arr):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1
        if count == 1:
            print(arr[i])
            


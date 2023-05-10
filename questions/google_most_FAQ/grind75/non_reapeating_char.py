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
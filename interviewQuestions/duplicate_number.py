
lst = [1,2,3,4,1,1,2,2,2,3,8,6]

print(list(set(lst)))

#or
def duplicate(my_lst):
    new_unique = []
    for i in my_lst:
        if i not in new_unique:
            new_unique.append(i)
    return new_unique

print(duplicate(lst))
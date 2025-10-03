my_lst = [1,2,2,3,3,4,4,5,5,6,6,7,7,8,9,10,10,11,11]

#Shir solution first time
not_unique = []
repeated_one = []
for i in my_lst:
    if i in repeated_one:
        not_unique.append(i)
    else:
        repeated_one.append(i)

unique = list(set(repeated_one)-set(not_unique))

print(not_unique)
print(repeated_one)
print(unique)



# this slution is by teacher

# def is_unique(lst):
#     new_lst = []
#     for i in lst:
#         if i in new_lst:
#             print(i)
#             return False
#         else:
#             new_lst.append(i)
#     return True

# print(is_unique(my_lst))
# list = [1,3,4,5,64,4,8, 9], target = 9
my_list = [1,3,5,64,8,9]

# def two_sum(lst, target):
#     new_list = []
#     for i in lst:
#         New_target = target - i
#         new_list.append(New_target)
#         if i in new_list:
#             return [i, New_target]


# print(two_sum(my_list, 9))


# def two_sum(lst, target):
#     for i in range(len(lst)):
#         for j in range(i, len(lst)):
#             if lst[i] + lst[j] == target:
#                 return [lst[i], lst[j]]

# print(two_sum(my_list, 9))


# def two_sum(lst, target):
#     new_list = {}
#     for inx, value in enumerate(lst):
#         if target - value in new_list:
#             return [new_list[target-value], inx]
#         else:
#             new_list[value] = inx

# print(two_sum(my_list, 9))


def two_sum(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                continue
            elif lst[i] + lst[j] == target:
                print(i,j)

two_sum(my_list, 9)
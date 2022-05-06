#This is just nested recursion
# Input: [1,2,[3]]
# Output: 6

# Input: [[4,5],[7,8,[20]],100]
# Output: 144

# Input: [[1,2,3],[4,[5,6]],7]
# Output: 28

# def nested_even_sum(lst):
#     total = 0
#     for i in range(len(lst)):
#         if type(lst[i]) == list:
#             # call the same function if
#             # the element is a list
#             total += nested_even_sum(lst[i])
#         else:
#             # if it's a single element
#             # and not a list, add it to total
#             if lst[i] % 2 == 0:
#                 total += lst[i]
#     return total

# my_list = [[1,2,3],[4,[5,6]],7]
# result = nested_even_sum(my_list)
# print(result)


obj = {
    "a":2,
    "b":{"x":2, "y":{"foo":3, "z":{"bar":2}}},
    "c":{"p":{"h":2, "r":5}, "q":"ball", "r":5},
    "d":1,
    "e":{"nn":{"lil":2},"mm":"car"}}

# def recursive_sum(n):
#     current_sum = 0
#     for key in n:
#         if isinstance(n[key], dict):
#             current_sum = current_sum + recursive_sum(n[key])
#         elif not isinstance(n[key], str):
#             current_sum = current_sum + n[key]
#     return current_sum

# res = recursive_sum(obj)
# print(res)

def nested_even_sum_recursive(obj, sum=0):
    for key in obj:
        if isinstance(obj[key], dict):
            sum += nested_even_sum_recursive(obj[key])
        elif not isinstance(obj[key], str):
            if obj[key] % 2 == 0:
                sum += obj[key]
    return sum

res = nested_even_sum_recursive(obj)
print(res)
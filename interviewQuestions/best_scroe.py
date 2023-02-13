best_scor = [55, 66, 50, 85, 89, 90, 99, 99, 100, 10]

# Shir fist try


def find_bests(arr):
    new_lst = sorted(set(arr))
    first, second = new_lst[-1:-3:-1]
    return [first, second]


print(find_bests(best_scor))



# #udemy calas way
# def firstSecond(given_list):

#     a = given_list  # make a copy

#     a.sort(reverse=True)

#     print(a)

#     first = a[0]

#     second = None

#     for element in given_list:

#         if element != first:

#             second = element

#             return first, second

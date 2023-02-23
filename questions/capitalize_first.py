# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])


def capitalize_first(lst):
    new_list = []
    for word in lst:
        result = word.title()
        new_list.append(result)
    return new_list


name = ["shir", "hussain", "danishyar", "amir", "rana", "sidiqa"]

cpf = capitalize_first(name)
print(cpf)

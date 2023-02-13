
obj = {
    "a": 2,
    "b": {"x": 2, "y": {"foo": 3, "z": {"bar": 2}}},
    "c": {"p": {"h": 2, "r": 5}, "q": "ball", "r": 5},
    "d": 1,
    "e": {"nn": {"lil": 2}, "mm": "car"}}


# def stringify(obj):
#     new_list = obj
#     for key in new_list:
#         if isinstance(new_list[key], (dict, list)):
#             new_list[key] = stringify(new_list[key])
#         elif not isinstance(new_list[key], str):
#             if isinstance(new_list[key], (int, bool)):
#                 new_list[key] = str(new_list[key])
#     return new_list


# res = stringify(obj)
# print(res)


def stringifyNumbers(obj):
    newObj = obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key] = str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key] = stringifyNumbers(newObj[key])
    return newObj

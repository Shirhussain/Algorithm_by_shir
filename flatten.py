# def flatten(itr):
#     for i in itr:
#         try:
#             yield from flatten(i)
#         except Exception:
#             yield i

# my_list = [[1], 2, "Shir", ["name", [[[["Shir"]]]], "lastname"], ["Danishyar"]]

# result = list(flatten(my_list))

# print(result)


my_list = [[1], 2, "Shir", ["name", [[[["Shir"]]]], "lastname"], ["Danishyar"]]


def flatten(lst):
    # return sum((flatten(x) if isinstance(x, list) else [x] for x in lst), [])
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])


result = flatten(my_list)
print(result)

# nestedlist = [ [1, 2, 3, 4], ["Ten", "Twenty", "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]
# flatlist=[]
# for sublist in nestedlist:
#     for element in sublist:
#         flatlist.append(element)
# print(flatlist)


# def flatten(arr):
#     resultArr = []
#     for custItem in arr:
#         if type(custItem) is list:
#             resultArr.extend(flatten(custItem))
#         else:
#             resultArr.append(custItem)
#     return resultArr

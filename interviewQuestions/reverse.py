# def reverse(strng):
#     if len(strng) <= 1:
#         return strng
#     return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])


def reverse(string):
    li = ""
    for i in string:
        li = i+li
    return li


print(reverse("python"))

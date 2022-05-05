def reverse(string):
    li = ""
    for i in string:
        li = i+li
    return li
print(reverse("python"))
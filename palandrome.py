# def isPalindrome(strng):
#     if len(strng) == 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return isPalindrome(strng[1:-1])


def is_palandrome(strng):
    return strng == strng[::-1]


print(is_palandrome("nan"))

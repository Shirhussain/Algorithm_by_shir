def plandrom(string):
    return string == string[-1::-1]

print(plandrom("dod dod"))


# or

def is_landrom(string):
    left, right = 0, len(string)-1
    while right >= left:
        if not string[right] == string[left]:
            return False
        left += 1; right -= 1
        return True

print(is_landrom("redrum murder"))
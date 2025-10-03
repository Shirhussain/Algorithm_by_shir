def is_bad_version(version):
    return version >= 5

def first_bad_version(n):
    l = 1
    r = n
    while l < r:
        mid = (l+r)//2
        if is_bad_version(mid):
            r = mid
        else:
            l = mid+1
    # now because left and right are the same then return left or right 
    return l 


print(first_bad_version(100))

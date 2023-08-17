"""
can sum to target:  can_sum(7, [5,3,4,7])--> true 
for example if we sum 4+3 --> 7 or 
7 it self is part of the list and also True 

                                    7
                            -5/   -3 /    -4\    -7\
                            2       4        3      0 
                                -3/  -4\     -3|  
                                1      0      0 
                            

"""


def can_sum(nums, target):
    if target < 0:
        return False
    if target == 0:
        return True

    # for num in nums:
    #     if can_sum(nums, target - num) == True:
    #         return True
    # # I just called return False out side if it couldn't find any True inside the loop
    # return False

    # or
    return any(can_sum(nums, target - num) == True for num in nums)


lst = [5, 3, 4, 7]
print(can_sum(lst, 7))
print(can_sum([2, 4], 7))
# print(can_sum([7, 14], 300))


def can_sum_memo(nums, target, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in nums:
        if can_sum_memo(nums, target - num, memo) == True:
            memo[target] = True
            return True
    memo[target] = False
    return memo[target]


print(can_sum_memo([2, 14], 300))

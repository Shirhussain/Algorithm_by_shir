"""
                                [2,5,2,1,2]

                                        5
                                -2/  -5/  -2|  -1\  -2\
                                3     0      3    4     2 
                    -2/  5/ 2| 1\ 2\  -2/ -5/ 2| 1| 2|
                    1   -2  1   2  1    
                            
"""


def how_sum(nums, target):
    if target == 0:
        return []
    elif target < 0:
        return None

    result = []
    for num in nums:
        remain_target = how_sum(nums, target - num)
        if remain_target is not None:
            result.extend(remain_target)
            result.append(num)
            return result

    return None


# time O(n^m*n)
# space O(m)
print(how_sum([2, 3], 7))


def how_sum_memo(nums, target, memo={}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return

    result = []
    for num in nums:
        remain_target = how_sum_memo(nums, target - num, memo)
        if remain_target is not None:
            result.extend(remain_target)
            result.append(num)
            memo[target] = result
            return memo[target]
    memo[target] = None
    return


# time O(n*m*m)
# space = O(m*m)
print(how_sum_memo([2, 3], 7))
print(how_sum_memo([30, 14], 300))

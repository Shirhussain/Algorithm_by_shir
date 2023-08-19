"""
    find the best sum it means that you have to find out of those list of sum the 
    has the smallest length 
    best_sum(8, [2,3,5]) --> [2,2,2,2], [3,2, 3], [3,5]
    the answer is [3,5]
    
                                        8 
                                -2/     -3|       -5\
                                6       5           3
                        -2/  -3| -5\  -2/-3| -5\  -2/ -3| -5\ 
                        4    3     1  3   2    0   1    0    -2 
                        
                        
                        
                        finally this is going to be the path: [2,2,2,2], [3,2, 3], [3,5]
                        but we only chose [3,5]
                        
"""


def best_sum(nums, target):
    if target == 0:
        return []
    elif target < 0:
        return

    result = []
    for num in nums:
        remain_target = best_sum(nums, target-num)
        result.extend(remain_target)
        result.append(num)

        if len(result[-1]) > len(result[0]):
            result[0] = result[-1]
        return result[0]
    return None


print(best_sum([2, 3, 5], 8))

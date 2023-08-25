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

    shortest_path = None
    for num in nums:
        remain_target = best_sum(nums, target-num)

        if remain_target is not None:
            curr_path = [num] + remain_target
            if shortest_path is None or len(curr_path) < len(shortest_path):
                shortest_path = curr_path

    return shortest_path


print(best_sum([2, 3, 5], 8))
print(best_sum([5, 4, 3, 7], 7))
# print(best_sum([1, 2, 5, 25], 100))


def best_sum_memo(nums, target):
    if target == 0:
        return []
    if target < 0:
        return

    shortest_path = None
    for num in nums:
        remain_target = best_sum_memo(nums, target-num)
        if remain_target is not None:
            curr_path = [num] + remain_target
            if shortest_path is None or len(curr_path) < len(shortest_path):
                shortest_path = curr_path
    return shortest_path


print(best_sum_memo([2, 3, 5], 8))
print(best_sum_memo([5, 4, 3, 7], 7))

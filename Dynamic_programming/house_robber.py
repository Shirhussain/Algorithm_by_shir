# Given N numbers of houses along with the street with some amount of money
# Adjacent houses can't be stolen
# find the maximum amount that cna be stolen

def house_robber_top_down(houses, current_index, temp_dict):
    if current_index >= len(houses):
        return 0
    else:
        if current_index not in temp_dict:
            # here increasing index by to to skep one house
            steal_first_house = houses[current_index] + \
                house_robber_top_down(houses, current_index + 2, temp_dict)
            skipped_first_house = house_robber_top_down(
                houses, current_index+1, temp_dict)
            temp_dict[current_index] = max(
                steal_first_house, skipped_first_house)
        return temp_dict[current_index]


houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber_top_down(houses, 0, {}))


def houses_robber_bottom_up(houses, current_index):
    # i'm putting +2 because of the last index
    temp_arr = [0]*(len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i]+temp_arr[i+2], temp_arr[i+1])
    return temp_arr[0]


new_houses = [6, 7, 1, 30, 8, 2, 4]
print(houses_robber_bottom_up(new_houses, 0))


""" 
House Robber:
[1,2,3,1] -> 4
       Rob house 1, and rob house 3 : 4

[2,7,9,3,1] -> 12
 Rob house 1, 3, 5

Adjacent is bad:

0

1, [3,4]

2 [4]

house(0) = value(0) = 1
house(1) = max(value(0), value(1)) = max(1,2) = 2
house(2) = ??

dp invariant:
dp[i] -> maximum i can make from houses (0..i)
dp[n-1] -> my solution

dp[0] = houses[0] = 1
dp[1] = max(houses[0], houses[1]) = 2

dp[i] = max(houses[i] + dp[i-2], dp[i-1]



return dp[n-1]

house(i):
    my solution picks house i
        houses[i] + dp[i-2]
    or 
    it doesn't pick house i
        dp[i-1]

def house_robber(array):
    dp = [0]*n
    dp[0] = array[0]
    dp[1] = max(array[0], array[1])

    for i in range(2, n):
        dp[i] = max(array[i] + dp[i-2], dp[i-1])

    return dp[n-1]

         0 1  2  3 4
houses [2, 7, 9, 3, 1]

Goal: find most of money i can make robbing non-adjacent houses

can you tell me for any i:
    how much money i can make from robbing
    houses 0...i


dp[0] = houses[0]
dp[1] = max(houses[0], houses [1])


dp[i]
    rob i, houses[i] + dp[i-2]
    don't rob dp[i-1]





        0  1  2  3 4 5
houses [2, 7, 9, 3, 1, 0]

if somebody ask that which one of the house number you robbed? then we need to track ourself 
by putting '1' if we change the number otherwise put '0' then after we comeback we check
if it's included or not if two adjacent number is '1' it means that we need to talk the last one 
and skip one before that it means it was not part of the process. and continue 

dp        [2, 7, 11, 11, 12, 12]
indicator  [1, 1,  1, 0, 1, 0]

then if we come back from end to start we see that house '4', '2', '0' is robbed 
then or based on indicator also we can find.
sol: [4, 2,0]

"""


houses = [6, 7, 1, 30, 8, 2, 4]


def house_robber(arr):
    dp = [0]*len(arr)

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i])
    return dp[len(arr)-1]


print(house_robber(houses))


"""
                              F(i)
                            /     \
    include curr cost F(i-1)      not include F(i-2) + cost[i]

        nums = [2,7,9,3,1]

        F(0) = nums[0]
        F(1) = max(nums[0], nums[1])
        F(2) --> include curr cost or not
            F(2) --> not include F(1)
            F(2) --> include F(0) + nums[2]
        F(3) --> include or not:
            F(3) --> include (F2)
            F(3) --> not include (F1) + nums[3]
        F4 --> include or not:
            F(4) --> not incl F(3)
            F(4) --> include F(2) + nums[4]


"""


def rob(nums):

    memo = {}

    def helper(i):
        if i in memo:
            return memo[i]
        if i == 0:
            result = nums[0]
        elif i == 1:
            result = max(nums[0], nums[1])
        else:
            result = max(helper(i-1), helper(i-2)+nums[i])
        memo[i] = result
        return memo[i]
    return helper(len(nums)-1)


houses = [6, 7, 1, 30, 8, 2, 4]
print(rob(houses))

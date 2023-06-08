# find how many unique way to find to sump up the coins to become equal to the total
"""
Example 1:

Input: [1,2,3], 4

Output: 4

Possible Combinations:

1+1+1+1

1+3

1+1+2

2+2


Example 2:

Input: [2,5,3,6], 10

Output: 5

Possible Combinations:

2+3+5

5+5

2+3+2+3

2+2+6

2+2+2+2+2

"""

# Complete the 'coinSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY coins
#  2. INTEGER total
#


# we need to create two burnch in leftside I subtract last coin form total (total-cin[-1]) and the right side I need to coins.pop() the last coin
# then if the coin become empty or total become 0 return 1, if the total become less than 0 then return 0

#                                         total(5),[coins(1,2,3)]
#                              subtract/                            \pop()
#                           2,[1,2,3]                                  5,[1,2]
#                           /.       \                               /.      \
#                       -1,[1,2,3].  2,[1,2]                   3[1,2].      5[1]
#                                   /.       \.              /      \     /.   \
#                               0,[1,2].   2,[1]          1[1,2]. 3[1].   4[1]. 5[]
#                                         /.   \.        /.  \.   /. \.   /.  \
#                                     1[1]   2,[].  -1[1,2] 1[1] 2[] 3[] 3[1] 4[]
#                                    /. \.                  /. \.        /. \ 
#                                  0[1] 1[]                0[]. 1[].   2[1]  3[]
#                                                                     /.  \ 
#                                                                   1[1]. 2[]
#                                                                  /. \ 
#                                                                 0[]  1[]


def coinSum(total_input, coins_list):
    def find_ways(total, coins):
        if total < 0:
            return 0 
        if len(coins) == 0:
            if total > 0:
                return 0
            return 1 
        left = find_ways(total-coins[-1], coins)
        poped = coins.pop()
        right = find_ways(total, coins)
        # becuase we need to have the complete form of coins in the most left and also write for the next round
        # so we need to push back to the coins list
        coins.append(poped)
        return left + right 
    return find_ways(total_input, coins_list)


print(coinSum(4,[1,2,3]))
print(coinSum(10,[2,5,3,6]))


#time O(n^(m+n))
# space O(m+n), how tall are call stack



#let do this time with dynamic programming memoaization tichniq

def cashedCoinSum(total_input, coins_list):
    cashe = {}
    def helper(total, coins):
        key = str(total) + '_' + str(coins)
        if key in cashe:
            return cashe[key]
        if total < 0:
            return 0
        if len(coins) == 0:
            if total > 0:
                return 0
            return 1
        left = helper(total-coins[-1], coins)
        poped = coins.pop()
        right = helper(total, coins)
        # we need to have the complete form of the coins for the right call as well so we have to put bakc
        # other wise it's going to pop the second last coin as well
        coins.append(poped)
        cashe[key] = left + right 
        return left + right
    return helper(total_input, coins_list)


print(cashedCoinSum(1000, [1,2,3,4,5,6,7,8,9,10,11,12]))



# tabulation coin sum
# total(5),[coins(1,2,3)]
"""
based on previous question we know that if coins become empty and total become zero we return 1
            0   1   2   3   4  5
        -------------------------
[]      |   1   0   0   0   0  0 
[1]     |   1   1   1   1   1  1
[1,2]   |   1   1   2   2   3  3
[1,2,3] |   1   1   2   2   4  4 



1, identify factor (total, coins)
2, create table increamintely increasing factors 
    what is smallest version ?
    what is eventual version ?
3, determine formula
4, create fuction - create first row 
5, fill out rest of the table

"""


def tabulationCoinSum(total_input, coins_input):
    table = [0]*(total_input+1)
    table[0] = 1
    for coin in coins_input:
        for i in range(coin, len(table)):
            # print("thisis each row: -->table: ", table[i], "table[i-coins]", i-coin, "coin -> :", coin)
            table[i] = table[i] + table[i-coin]
    return table[total_input]

print(tabulationCoinSum(10,[2,5,3,6]))


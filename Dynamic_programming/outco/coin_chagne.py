""" 
                (11)
          1/    2|   5\
         10     9        6 ------> this level 6 is minimum
      /  | \   /|\     / |  \
     9   8 5  8 7 4   5  4     1 -----> this level 1 is min
    ~     ~    ~    /|\  /|\    /|\
                  4 3 0 1 2 -1 0 -1 -4

as you can see we need to track min in each level so we can reach to the solution
F(n) = min(F(amount-coins[0]), F(amount-coins[1]), F(amount-coins[2])) + 1  --> I add +1 becuase 
if we move from 0 to 1 then it cast as one coin so you need to add 1 
"""


from collections import deque


def coin_change(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    # track the min amount in each level as like in figure
    min_remain_amount = float('inf')
    for coin in coins:
        remain_amt = coin_change(coins, amount-coin)
        # if we have enough amount just do it
        if remain_amt >= 0:
            min_remain_amount = min(min_remain_amount, remain_amt)
    return -1 if min_remain_amount == float('inf') else min_remain_amount + 1


coins, amount = [1, 2, 5], 11

print(coin_change(coins, amount))


def coin_change_memo(coins, amount):
    def helper(amount, memo):
        if amount == 0:
            return 0
        if amount < 1:
            return -1
        if amount in memo:
            return memo[amount]

        min_way = float('inf')
        for coin in coins:
            remain_amt = helper(amount-coin, memo)
            if remain_amt >= 0:
                min_way = min(min_way, remain_amt)
        memo[amount] = -1 if min_way == float('inf') else min_way + 1
        return memo[amount]
    return helper(amount, {})


coins, amount = [1, 2, 5], 900
print(coin_change_memo(coins, amount))


# or by DFS
"""
                (11)
          1/    2|   5\
         10     9        6 ------> this level 6 is minimum
      /  | \   /|\     / |  \
     9   8 5  8 7 4   5  4     1 -----> this level 1 is min
    ~     ~    ~    /|\  /|\    /|\
                  4 3 0 1 2 -1 0 -1 -4

"""


def coinChangeDFS(coins, amount):
    q = deque([(amount, 0)])
    visited = set()

    while q:

        remain, count = q.popleft()
        if remain == 0:
            return count
        for coin in coins:
            dif = remain - coin
            if dif in visited or dif < 0:
                continue
            q.append((dif, count+1))
            visited.add(dif)
    return -1


coins, amount = [1, 2, 5], 9000
print(coinChangeDFS(coins, amount))


# Tabulation way
def tabulation_coin_change(coins, amount):
    ch = [float('inf')] * (amount + 1)
    ch[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i-coin >= 0:
                ch[i] = min(ch[i], ch[i-coin]) + 1
    return -1 if ch[amount] == float('inf') else ch[amount]


coins, amount = [1, 2, 5], 11
print(tabulation_coin_change(coins, amount))

"""
    Painting problem:
    You're painting the exterior of houses in a neighborhood. Each house has a
    cost. Adjacent houses can't be painted on the same day because the paint
    needs to dry.

    Given an array costs of house painting costs, return the maximum possible
    cost while adhering to the constraint of not painting adjacent houses on the
    same day.

    Example 1:
    Input: costs = [2, 7, 9, 3, 1]
    Output: 12
    Explanation: Paint the first, third, and fifth houses for a total cost of 2 +
    9 + 1 = 12.

    Example 2:
    Input: costs = [10, 5, 1, 20]
    Output: 30
    Explanation: Paint the first and fourth houses for a total cost of 10 + 20
    = 30.

    Example 3:
    Input: costs = [4, 1, 2, 3, 7]
    Output: 13
    Explanation: Paint the first, third, and fifth houses for a total cost of 4 +
    2 + 7 = 13.

    Recursive relationship
    F(n) = Max ( F(n-1), F(n-2) + costs[n] )
    F(0) = costs[0],  F(1) =F(0)+ costs[1]

    more information: -->
    https://docs.google.com/document/d/1JaYYuTtXCSAuCqoZnyfIe8sHGW9iY4-_eSIffENHnKU/edit
    
    
    
    [4, 1, 2, 3, 7]
    F(0) = costs[0]
    F(1) = max(costs[0], costs[1])
    F(2) = here we need to decide if we are going to include ith index it means (2) index
        as well or not 
        if it's not included F2 = F(1)
        if it's included F2 = F(0) + costs[2]
        
    F(3) = if not included  F(3) = F(2)
            if included F(3) = F(1) + costs[3]
            
    F(4) = not included F(4) = F(3)
            included F(4) = F(2) + costs[4)
    
    
                                [4, 1, 2, 3, 7]
                                    F(i)
                                /         \
                            f(i-1)       f(i-2) + costs(i)
                            
                            
                            
"""


def max_point_cost(costs):
    def helper(i):
        if i == 0:
            return costs[0]
        if i == 1:
            return max(costs[0], costs[1])
        return max(helper(i-1), helper(i-2)+costs[i])
    return helper(len(costs)-1)


lst = [4, 1, 2, 3, 7]
print(max_point_cost(lst))


def max_point_cost_memo(costs):
    def helper(i):
        map = {}
        if i in map:
            return map[i]
        if i == 0:
            result = costs[0]
        elif i == 1:
            result = max(costs[0], costs[1])
        else:
            result = max(costs[i-1], costs[i-2] + costs[i])
        map[i] = result
    return helper(len(costs)-1)


print(max_point_cost(lst))


def max_point_cost_with_dp(costs):
    dp = [0] * len(costs)
    dp[0] = costs[0]
    dp[1] = max(costs[1], costs[0])
    for i in range(2, len(costs)):
        dp[i] = max(dp[i-1], dp[i-2] + costs[i])
    return dp[len(costs)-1]


print(max_point_cost_with_dp(lst))

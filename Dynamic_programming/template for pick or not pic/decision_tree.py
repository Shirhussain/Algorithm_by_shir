def decision_tree(nums, index, current_subset):
    # Base Case: If you've processed all elements
    if index == len(nums):
        # Process the current subset (e.g., print or store it)
        print(current_subset)  # Example action
        return

    # Case 1: Do not pick the current element
    decision_tree(nums, index + 1, current_subset)

    # Case 2: Pick the current element
    current_subset.append(nums[index])
    decision_tree(nums, index + 1, current_subset)

    # Backtrack: Remove the element after processing
    current_subset.pop()


# Example usage
nums = [1, 2, 3]
decision_tree(nums, 0, [])


# with dp way to memoize

def decision_tree_dp(nums, index, current_sum, memo):
    # Base Case: If all elements are processed
    if index == len(nums):
        # Example condition to check (e.g., target sum)
        return current_sum == 0

    # If the result is already computed, return it
    if (index, current_sum) in memo:
        return memo[(index, current_sum)]

    # Case 1: Not Pick the current element
    not_pick = decision_tree_dp(nums, index + 1, current_sum, memo)

    # Case 2: Pick the current element
    pick = decision_tree_dp(nums, index + 1, current_sum - nums[index], memo)

    # Store the result in the memo dictionary
    memo[(index, current_sum)] = pick or not_pick

    return memo[(index, current_sum)]


# Example usage
nums = [1, 2, 3]
target_sum = 4
memo = {}
print(decision_tree_dp(nums, 0, target_sum, memo))


# Example usage

def subset_sum(nums, index, target_sum):
    # Base Case: If the target sum is 0, subset exists
    if target_sum == 0:
        return True
    # If no elements left or target becomes negative, no valid subset
    if index == len(nums) or target_sum < 0:
        return False

    # Case 1: Do not pick the current element
    not_pick = subset_sum(nums, index + 1, target_sum)

    # Case 2: Pick the current element
    pick = subset_sum(nums, index + 1, target_sum - nums[index])

    return pick or not_pick


# Example usage
nums = [3, 34, 4, 12, 5, 2]
target_sum = 9
print(subset_sum(nums, 0, target_sum))  # Output: True (subset [4, 5])


def subset_sum_dp(nums, target_sum):
    n = len(nums)
    # Initialize the DP table with False
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

    # Base Case: A subset with sum 0 is always possible (empty subset)
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if nums[i - 1] <= j:  # If current element can be included
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:  # If current element cannot be included
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]


# Example usage
nums = [3, 34, 4, 12, 5, 2]
target_sum = 9
# Output: True (subset [4, 5])
print("this is result: ", subset_sum_dp(nums, target_sum))


def combination_sum(nums, index, target_sum, current_combination, result):
    # Base Case: If the target sum is 0, store the current combination
    if target_sum == 0:
        result.append(list(current_combination))
        return

    # If target becomes negative or no more elements to process
    if target_sum < 0 or index == len(nums):
        return

    # Case 1: Pick the current element (can pick again)
    current_combination.append(nums[index])
    combination_sum(nums, index, target_sum -
                    nums[index], current_combination, result)
    current_combination.pop()  # Backtrack

    # Case 2: Not pick the current element and move to the next element
    combination_sum(nums, index + 1, target_sum, current_combination, result)


# Example usage
nums = [2, 3, 6, 7]
target_sum = 7
result = []
combination_sum(nums, 0, target_sum, [], result)
print(result)  # Output: [[2, 2, 3], [7]]


def combination_sum_dp(nums, target_sum):
    # Initialize the DP table with empty lists
    dp = [[] for _ in range(target_sum + 1)]

    # Base Case: There is one way to get sum 0 (empty combination)
    dp[0] = [[]]

    # Fill the DP table
    for num in nums:
        for j in range(num, target_sum + 1):
            for combination in dp[j - num]:
                dp[j].append(combination + [num])

    return dp[target_sum]


# Example usage
nums = [2, 3, 6, 7]
target_sum = 7
print("combination_sum_dp: ", combination_sum_dp(
    nums, target_sum))  # Output: [[2, 2, 3], [7]]


def generate_subsequences(nums, index, current_subsequence, result):
    # Base Case: If all elements are processed, store the current subsequence
    if index == len(nums):
        result.append(list(current_subsequence))
        return

    # Case 1: Not pick the current element
    generate_subsequences(nums, index + 1, current_subsequence, result)

    # Case 2: Pick the current element
    current_subsequence.append(nums[index])
    generate_subsequences(nums, index + 1, current_subsequence, result)

    # Backtrack
    current_subsequence.pop()


# Example usage
nums = [1, 2, 3]
result = []
generate_subsequences(nums, 0, [], result)
print(result)
# Output: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]


def generate_subsequences_dp(nums):
    n = len(nums)
    dp = [[]]  # Start with an empty subsequence

    # Fill the DP table
    for num in nums:
        dp += [current + [num] for current in dp]

    return dp


# Example usage
nums = [1, 2, 3]
print("generate_subsequences_dp: ", generate_subsequences_dp(nums))
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


def knapsack(weights, values, index, capacity):
    # Base Case: No items left or capacity becomes zero
    if index == len(weights) or capacity == 0:
        return 0

    # Case 1: Not pick the current item
    not_pick = knapsack(weights, values, index + 1, capacity)

    # Case 2: Pick the current item, if it fits in the knapsack
    pick = 0
    if weights[index] <= capacity:
        pick = values[index] + \
            knapsack(weights, values, index + 1, capacity - weights[index])

    return max(pick, not_pick)


# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print(knapsack(weights, values, 0, capacity))  # Output: 220


def knapsack_dp(weights, values, capacity):
    n = len(weights)
    # Initialize the DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:  # If the current item can fit in the knapsack
                dp[i][j] = max(dp[i - 1][j], values[i - 1] +
                               dp[i - 1][j - weights[i - 1]])
            else:  # If the current item cannot fit
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]


# Example usage
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("knapsack_dp: ", knapsack_dp(weights, values, capacity))  # Output: 220


# this is the template for pick or not pick of DP
# dp[i][j]=dp[i−1][j]+dp[i−1][j−nums[k]]


def three_sum_dp(nums):
    n = len(nums)
    target = 0  # We are looking for triplets that sum up to 0

    # Initialize a DP table: dp[i][j] -> True if we can form sum j with i elements
    dp = [[[False] * (target + 1) for _ in range(4)] for _ in range(n + 1)]
    dp[0][0][0] = True  # Base case: we can make sum 0 with 0 elements

    # Fill the DP table
    for i in range(1, n + 1):
        num = nums[i - 1]
        for j in range(4):
            for s in range(target + 1):
                # Don't take the current number
                dp[i][j][s] = dp[i - 1][j][s]
                # Take the current number, if it doesn't exceed the target and j > 0
                if j > 0 and s >= num:
                    dp[i][j][s] = dp[i][j][s] or dp[i - 1][j - 1][s - num]

    # The result is True if we can form a triplet that sums to the target
    return dp[n][3][target]

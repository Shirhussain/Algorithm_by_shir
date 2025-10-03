# Longest Consecutive
# Have the function LongestConsecutive(arr) take the array of positive integers stored
# in arr and return the length of the longest consecutive subsequence (LCS). An LCS is
# a subset of the original list where the numbers are in sorted order, from lowest to highest,
#  and are in a consecutive, increasing order. The sequence does not need to be
#   contiguous and there can be several different subsequences. For example:
#    if arr is [4, 3, 8, 1, 2, 6, 100, 9] then a few consecutive sequences
#    are [1, 2, 3, 4], and [8, 9]. For this input, your program should return 4
#     because that is the length of the longest consecutive subsequence.

def longest_consecutive_arr(arr):
    longest = 0
    for num in arr:
        current = num
        current_strike = 1
        while (current + 1) in arr:
            current = current + 1
            current_strike = current_strike + 1
        longest = max(longest, current_strike)
    return longest


lst = [4, 3, 8, 1, 2, 6, 100, 9]
print(longest_consecutive_arr(lst))

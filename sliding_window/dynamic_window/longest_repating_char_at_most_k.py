""" 
395. Longest Substring with At Least K Repeating Characters
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""


def longest_substring_with_at_least_k_repeating_char(s, k):
    if not s or k > len(s):
        return 0

    # If any character appears less than k times in the entire string,
    # we need to split on that character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Base case: all characters appear at least k times
    all_valid = True
    for count in char_count.values():
        if count < k:
            all_valid = False
            break
    if all_valid:
        return len(s)

    # Divide and conquer
    max_length = 0
    start = 0
    for i in range(len(s)):
        if char_count[s[i]] < k:
            substring = s[start:i]
            if substring:
                max_length = max(max_length,
                                 longest_substring_with_at_least_k_repeating_char(substring, k))
            start = i + 1

    # Check the last substring
    if start < len(s):
        max_length = max(max_length,
                         longest_substring_with_at_least_k_repeating_char(s[start:], k))

    return max_length


print(longest_substring_with_at_least_k_repeating_char("aaabb", 3))
print(longest_substring_with_at_least_k_repeating_char("ababbc", 2))

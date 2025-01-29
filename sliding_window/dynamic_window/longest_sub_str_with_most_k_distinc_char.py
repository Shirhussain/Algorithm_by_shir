""" 
340. Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Example 3:
Input: s = "a", k = 1
Output: 1
Explanation: The substring is "a" with length 1.

Example 4:
Input: s = "abaccc", k = 2
Output: 4
Explanation: The substring is "abac" with length 4.
"""


def longest_substring_with_most_k_distinct_char(s, k):
    left = 0
    right = 0
    char_count = {}
    max_length = 0

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length


print(longest_substring_with_most_k_distinct_char("eceba", 2))
print(longest_substring_with_most_k_distinct_char("aa", 1))
print(longest_substring_with_most_k_distinct_char("a", 1))
print(longest_substring_with_most_k_distinct_char("abaccc", 2))


def longest_substring_with_most_k_distinct_char_2(s, k):
    from collections import Counter
    char_count = Counter()

    # Length of the input string

    n = len(s)

    # Initialize the answer and the start index (j) of the current window

    max_length = start_index = 0

    # Enumerate over the characters of the string with index (i) and character (char)

    for i, char in enumerate(s):

        # Increment the count of the current character

        char_count[char] += 1

        # If the number of distinct characters exceeds k, shrink the window

        while len(char_count) > k:

            # Decrement the count of the character at the start index

            char_count[s[start_index]] -= 1

            # If the count goes to zero, remove the character from the counter

            if char_count[s[start_index]] == 0:

                del char_count[s[start_index]]

            # Move the start index forward

            start_index += 1

        # Update the maximum length found so far

        max_length = max(max_length, i - start_index + 1)

    # Return the maximum length of substring with at most k distinct characters

    return max_length


print(longest_substring_with_most_k_distinct_char_2("eceba", 2))
print(longest_substring_with_most_k_distinct_char_2("aa", 1))
print(longest_substring_with_most_k_distinct_char_2("a", 1))
print(longest_substring_with_most_k_distinct_char_2("abaccc", 2))

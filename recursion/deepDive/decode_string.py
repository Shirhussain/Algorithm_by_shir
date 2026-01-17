"""
Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
""" 
   3[a2[c]]
        \
        [a2[c]]
            \
            a2[c]
                \
                [c]

we continue if face with "["
    then call the recusive function
    if we hit to "]" it's the base case:
        then return the curr sol
    and multiply with the constant value


s = "2[abc]3[cd]ef"

                    2[abc]3[cd]ef
                       \
                       [abc]3[cd]ef
                              \
                              3[[cd]ef
                                  \
                                  [cd]ef
                                     


"""


class Solution:
    def decodeString(self, s: str) -> str:

        def helper(i):
            result = ""
            num = 0

            while i < len(s):
                c = s[i]

                if c.isdigit():
                    num = num * 10 + int(c)
                    i += 1

                elif c.isalpha():
                    result += c
                    i += 1

                elif c == "[":
                    decoded, i = helper(i + 1)
                    result += decoded * num
                    num = 0

                elif c == "]":
                    return result, i + 1

            return result, i

        decoded, _ = helper(0)
        return decoded

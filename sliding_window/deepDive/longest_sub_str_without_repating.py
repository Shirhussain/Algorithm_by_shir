'''
Longest Substring Without Repeating Characters
Given a string s, find a longest substring without repeating characters.

Input: String
Output: String


N = 10^8 and K = 16-bit characters (2^16)
Is case sensitive
Does not matter which longest substring is found if there are multiple.
'''
'''
Examples

Input: abcabcbb =>	Output: abc
Input: bbbbb	 	=>	Output: b
Input: pwwkew		=>	Output: wke or kew

'''

'''
Constraints
N ~ Length of input string
K ~ Number of unique characters in input string

Time Complexity: O(N)
Auxiliary Space Complexity: O(K)+O(N)
s consists of English letters, digits, symbols and spaces.
'''

'''

Monotonic condition: no repeating chars in the window

state:

hashmap of characters we have seen (keys), value is number of occurrences

Diagram:

abcabcbb
l
   r

hash: {a:0, b:1, c:0}

max_l: 0
max_r: 0

sliding_window(input sequence)
  # initialize state related to window
  hash = {}
  initialize left to 0

  max_l
  max_r

  for right in range 0 to length of input

    # update window state for expansion
    "add" input[right] to hash: if first "add", then value is 1, else value is incremented
    
    # while monotonic condition is not met
    while hash[input[right]] value is 2
      # update window state for contraction
      decrement value of input[left] character in hash
      increment left

    difference between the current r and l exceeds the difference between max_r and max_l, then
       (max_l, max_r) = (l, r-1)
       
  return input[max_l:max_r+1]
'''


def lengthOfLongestSubstring(s):
    result = 0
    new_set = set()
    l = 0

    for r in range(len(s)):
        while s[r] in new_set:
            new_set.remove(s[r])
            l += 1

        new_set.add(s[r])
        result = max(result, r-l + 1)
    return result


s = "abcabcbb"

print(lengthOfLongestSubstring(s))


def longest_substr_with_map(s):
    map = {}
    l = 0
    result = 0

    for r in range(len(s)):
        if s[r] in map:
            map[s[r]] += 1
        else:
            map[s[r]] = 1

        while map[s[r]] > 1:
            map[s[r]] -= 1
            l += 1
        result = max(result, r-l + 1)
    return result


print(longest_substr_with_map(s))

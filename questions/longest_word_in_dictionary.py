"""
Given an array of strings words representing an English Dictionary,
return the longest word in words that
can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest
word with the smallest lexicographical order. If there is no answer,
return the empty string.

Note that the word should be built from left to right with each additional
character being added to the end of a previous word. 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary.
However, "apple" is lexicographically smaller than "apply".

"""


def longest(words):
    words.sort()
    st, result = set(), ""
    st.add("")
    for word in words:
        if word[:-1] in st:
            if len(word) > len(result):
                result = word
            st.add(word)
    return result


words = ["ac", "applz", "a", "banana", "app", "appl", "ap", "apply", "apple"]

print(longest(words))

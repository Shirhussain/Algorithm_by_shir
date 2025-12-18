"""
Letter Combinations of a Phone Number
Solved
Medium
Topics
premium lock icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
"""
'''
 for each number
 map it to its characters

        [abc][def]
    
    a.          b.        c
    ad. ae af  bd. be bf  cd ce cf
    adg      
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # digit_letter_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
        # "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # combinations = []

        # dp = list(digit_letter_map[digits[0]])
        # for digit in digits[1:]:

        #     current_digits = list(digit_letter_map[digit])
        #     new_dp = []
        #     for j in current_digits:
        #         for index, val in enumerate(dp):
        #             new_dp.append(val+j)
        #     dp = new_dp

        # return dp
        """
                                2345

                                ""
                            /.   |      \
                           a     b.      c
                       /. | \.   / | \.   / |   \ 
                    d.    e. f  d. e. f. d.  e.  f 
                / | \.   /|\ /\\ /|\ .....
               g. h. i. g hi g hi ghi 
            /|\.  /|\
           j k l. j k l
        """

        digit_letter_map = {"2": "abc", "3": "def", "4": "ghi",
                            "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        result = []

        def dfs(path, i):
            if i == len(digits):
                result.append(path)
                return
            items = digit_letter_map[digits[i]]
            for item in items:
                dfs(path+item, i+1)

        dfs('', 0)
        return result

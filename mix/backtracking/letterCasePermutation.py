""" 
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]



                                    ""
                                a/       A\             0
                               1         1              1
                            b/   B\      b/  B\         2
                        a1b      a1B    A1b   A1B       
                        2|        2|    2|     2|       3
                        a1b2     a1B2   A1b2   A1B2


"""


def letterCasePermutation(s):
    result = []

    def helper(substr, idx):
        if idx == len(s):
            result.append(substr)
            return

        curr_char = s[idx]

        if curr_char.isalpha():
            helper(substr+curr_char.lower(), idx+1)
            helper(substr+curr_char.upper(), idx+1)
        else:
            # if it's a number
            helper(substr+curr_char, idx+1)

    helper("", 0)

    return result


print(letterCasePermutation("a1b2"))


def letterCasePermutation_swapCase(s):
    result = []

    def backtrack(substr="", i=0):
        if len(substr) == len(s):
            result.append(substr)
        else:
            if s[i].isalpha():
                backtrack(substr+s[i].swapcase(), i+1)
            backtrack(substr+s[i], i+1)

    backtrack()
    return result


print(letterCasePermutation_swapCase("a1b2"))

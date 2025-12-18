"""
 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open prantecies if open is < n
        # only add close prantecies if close is < close
        # valid if open == close == n

        stack = []
        result = []

        def backtracking(openN, closeN):
            if openN == closeN == n:
                result.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtracking(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backtracking(openN, closeN+1)
                stack.pop()
        backtracking(0, 0)
        return result


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        """

                                ""
                            open(.  close)

you have to build two branch one for open and one for close and just continue 
up and append to each not that open"(" and clsoe ")"

                         n = 2
                        ""
                    /        \
                  (            )
                /. \          / \
            ((      ().     )(.  ))
            / \.    / \      / \     /.  \
          ((( ((). ()( ()). )(( )()  ))(. )))
     /. \    /. \    .....
((((.  ((() (()( (())


then we can check the valdity of the pranteses
        """
        result = []

        def dfs(path, i):
            if i == n*2:
                if self.isValid(path):
                    result.append(path)
                return
            dfs(path+"(", i+1)
            dfs(path+")", i+1)

        dfs("", 0)
        return result

    # I barrow this from  https://leetcode.com/problems/valid-parentheses/

    def isValid(self, s: str) -> bool:
        # pairs = {")": "(", "]": "[", "}": "{"}
        # stack = []
        # for char in s:
        #     if char in pairs:
        #         if stack and stack[-1] == pairs[char]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(char)
        # return True if not stack else False

        # or

        # result = {"(": ")", "[": "]", "{": "}"}
        # stack = []
        # for c in s:
        #     if c in result:
        #         stack.append(c)
        #     else:
        #         if not stack or result[stack[-1]] != c:
        #             return False
        #         stack.pop()
        # return not stack

        stack = []

        for c in s:
            # '(', ')', '{', '}', '[' and ']'
            if c in "({[":
                stack.append(c)
            if not stack:
                return False
            elif c == ")":
                if stack.pop() != "(":
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    return False
        if stack:
            return False
        return True


print(Solution2().generateParenthesis(3))
print(Solution2().generateParenthesis(1))

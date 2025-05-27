"""
Answer these questions:
- What is the base case?
    pow(x,0) = 1
- What are the subproblems?
    pow(x,4) = pow(x,2)* pow(x,2)
    pow(x,5) = pow(x,2)* pow(x,2) * x
    
    General case:
    pow(x,n) = 
                Subproblem 1: pow(x,n//2) *  pow(x,n//2) if n is even
                Subproblem 2: pow(x,n//2) *  pow(x,n//2) * x if n is odd

- What is the combinator?
    OR


"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)

        r = self.myPow(x, n//2)
        if n % 2 == 0:
            return r * r
        else:
            return r * r * x


sol = Solution()
print(sol.myPow(2, 10))

""" 
a rabbit can hop 1, 2, or 3 steps at a time.
given a number of steps, how many ways can the rabbit hop to the top?

                  0
                 / | 
                1  2 
               /| / \ 
              2 3 3  4
            /| / \ / \
           3 4 4 5 5  6
    
"""


class Solution:
    def __init__(self, n):
        self.n = n

    def rabbit_hop(self):

        def backtrack(node):
            if node == self.n:
                return 1
            if node > self.n:
                return 0

            return backtrack(node + 1) + backtrack(node + 2)

        return backtrack(0)

    def print_all_paths(self):
        result = []

        def backtrack(node, path):
            # here the removing is done by our recursive call stack for free
            if node == self.n:
                result.append(path)
                return
            if node > self.n:
                return

            backtrack(node + 1, path + [1])
            backtrack(node + 2, path + [2])

        backtrack(0, [])

        return result


s = Solution(4)
print(s.print_all_paths())
print(s.rabbit_hop())

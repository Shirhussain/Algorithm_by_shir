"""
if we have grid travel of (2,3) --> which only you can go down or right 
find the amount of way to go there. 

                                (2,3)
                            /        \
                        (1,3)         (2,2)
                        /    \         /     \ 
                    (0,3)    (1,2)    (1,2)     (2,1)
                            /  \        / \        /    \
                        (0,2) (1,1) (0,2)(1,1)   (1,1)  (1,0)
                        

those which become zero it's return 0 way to go and 
those which ended with '1' is return 1 way to go


"""


def grid_travel(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1

    return grid_travel(m-1, n) + grid_travel(m, n-1)


print(grid_travel(2, 3))
print(grid_travel(3, 3))


def grid_traveler_memo(m, n, memo=None):
    if memo is None:
        memo = {}
    key = f"{m},{n}"
    if key in memo:
        return memo[key]

    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    memo[key] = grid_traveler_memo(
        m-1, n, memo) + grid_traveler_memo(m, n-1, memo)
    return memo[key]


print(grid_traveler_memo(18, 18))

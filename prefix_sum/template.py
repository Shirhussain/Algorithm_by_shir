# And the hashmap prefix-sum template:
""" 


seen = {0: 1}
prefix = 0
for x in nums:
    prefix += x
    if prefix - k in seen:
        ...
    seen[prefix] = seen.get(prefix, 0) + 1




# 2D Prefix Sum Template

m, n = len(grid), len(grid[0])
pre = [[0]*(n+1) for _ in range(m+1)]

for i in range(m):
    for j in range(n):
        pre[i+1][j+1] = (
            grid[i][j]
            + pre[i][j+1]
            + pre[i+1][j]
            - pre[i][j]
        )

"""
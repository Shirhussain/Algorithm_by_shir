# rabbit can go one step or 2 step a time how to reach destination

def rabbit_hope(n):
    rabbit = [0] * n  # ways the rabbit can go
    rabbit[0] = 0
    rabbit[1] = 1
    rabbit[2] = 2

    for i in range(3, n):
        rabbit[i] = rabbit[n-1] + rabbit[n-2]
        return rabbit[i]


print(rabbit_hope(5))

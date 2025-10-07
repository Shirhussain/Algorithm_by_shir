# experacing number as a sum of other in how many ways is possible.
# number factor of sum of (1,3,4)
# the number of way to find "f" as a sum of (1,3,4)
# {1,4},{1,1,3},{1,1,1,1,1}---> there is all six ways to find

def number_factor(num):
    if num in (0, 1, 2):
        return 1
    elif num == 3:
        return 2
    else:
        sub1 = number_factor(num-1)
        sub2 = number_factor(num-3)
        sub3 = number_factor(num-4)
        return sub1 + sub2 + sub3


print(number_factor(5))

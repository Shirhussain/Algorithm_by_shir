# step1: divid the number by 2

# Division | Quotient | reminder
# 13/2     | 6        | 1
# 6/2      | 3        | 0
# 3/2      | 1        | 1
# 1/2      | 0        | 1

# result = 1101

def decimal_to_binary(x):
    assert int(x) == x, "Parameter must be Integer"
    if x ==0:
        return 0
    else:
        return x%2 + 10*decimal_to_binary(int(x/2))

print(decimal_to_binary(13))
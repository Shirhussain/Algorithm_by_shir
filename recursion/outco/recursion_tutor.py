# 1. instantiate scope variables
# 2. return result
# 3. a) create helper method
#    b) invoke helper method
# 4. base case
# 5. recursive case

def factorial(n):
    # 1. instantiate scope variables
    result = 1
    # 3a. helper method
    def multiply_int(count):
        nonlocal result  #<-- define result as a nonlocal
        # 4. base case
        if(count > n):
            return
        # 5. recursive case
        result = result * count
        multiply_int(count + 1)
    # 3b. invoke helper method with initial input parameters
    multiply_int(1)
    # 2. return result
    return result
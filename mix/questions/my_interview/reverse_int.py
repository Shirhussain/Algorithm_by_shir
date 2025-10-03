# Reversing an integer without using reverse functions or lists or strings

number = 123456789
result = 0 

while number > 0:
    result = result * 10 + number % 10 
    number //= 10

print(result)
# reverse integer , ie: 0, 1, 2, 3

number = 34534534

reverse_number = 0

while number != 0:
    remain_number = number % 10 
    reverse_number = reverse_number * 10 + remain_number
    number //= 10

print(reverse_number)

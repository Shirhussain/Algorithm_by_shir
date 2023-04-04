# Change string to list datatype
# Remove last digit (check digit)
# Reverse remaining digits
# Double digits at even indices
# Subtract 9 if over 9
# Add the check digit back to the list
# Sum all digits
# If the sum is divisible by 10 then it is valid; otherwise, Invalid

numbers = "378282246310005"

def validate_credit_card(nums):
    card_number = [int(i) for i in numbers]
    check_digit = card_number.pop(-1)
    card_number.reverse()
    
    card_number = [num*2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]
    card_number = [ num-9 if num > 9 else num for num in card_number]
    card_number.append(check_digit)
    result = sum(card_number)
    return result % 10 == 0

print(validate_credit_card(numbers))
def count_bits(x):
    number_of_bits = 0
    while x:
        number_of_bits += x & 1
        x >>= 1
    return number_of_bits


print(count_bits(1000))


# Function calculates the decimal equivalent
# to given binary number

def binaryToDecimal(binary):

    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)


# Driver code
if __name__ == '__main__':
    binaryToDecimal(11000)


def decimal_to_binary(num):
    return bin(num).replace('0b', '')


print(decimal_to_binary(25))
print(decimal_to_binary(30))

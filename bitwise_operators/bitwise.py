# this is a tutorial for bitwise https://www.youtube.com/watch?v=PyfKCvHALj8
def count_bits(x):
    number_of_bits = 0
    while x:
        number_of_bits += x & 1
        x >>= 1
    return number_of_bits


print(count_bits(1000))

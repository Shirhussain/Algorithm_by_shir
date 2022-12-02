class Solution:
    def reverseBits(self, n: int) -> int:
        my_string = str(bin(n))[::-1][:-2]
        if len(my_string) < 32:
            my_string = my_string + '0' * (32 - len(my_string))
        return int(my_string, 2)

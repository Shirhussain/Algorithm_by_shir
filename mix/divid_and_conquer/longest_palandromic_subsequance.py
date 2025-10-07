# The longest palandromic subsequance
# problem statment
# S is a givin string
# find the longest palandromic subsequence
# subsequence: is a sequance which is driving from another sequance by deleting some elements.
# without changing the order of the sequences

# palandromic: means should be read able from both side the same i.e MADAM

# example
# S = "ELRMENMET"
# output = 5
# answer = EMEME


def longest_palandromic_sequences(s, start_index, end_index):
    if start_index > end_index:
        return 0
    elif start_index == end_index:
        # this statment means it reach to the middle of the sequence
        return 1
    elif s[start_index] == s[end_index]:
        # it means they both matched so we need to add 2 at the beginning,
        # because it' comming form right to the left then I'm going to subtract 1==(-1)
        return 2 + longest_palandromic_sequences(s, start_index+1, end_index-1)
    else:
        option1 = longest_palandromic_sequences(s, start_index, end_index-1)
        option2 = longest_palandromic_sequences(s, start_index+1, end_index)
        return max(option1, option2)


print(longest_palandromic_sequences("ELRMENMET", 0, 8))

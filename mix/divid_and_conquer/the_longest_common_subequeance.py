# Longest common Subsequence
# S1 and S2 are given string
# find the length of longest sub sequance which is common in both string
# subsequance: a sequance that can be driven from another sequance by deleting some elements
# without changing the order of them.

# example:
# s1 = elephant
# s2 = erepat
#longest = eepat


def find_longest_subsequence(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        # here '1' means that character is matched
        return 1 + find_longest_subsequence(s1, s2, index1 + 1, index2+1)
    else:
        option1 = find_longest_subsequence(s1, s2, index1+1, index2)
        option2 = find_longest_subsequence(s1, s2, index1, index2+1)
        return max(option1, option2)


print(find_longest_subsequence("elephant", "erepat", 0, 0))

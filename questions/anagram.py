from collections import Counter
string1 = "salesman"
string2 = "nameless"

string3 = "danger"
string4 = "gender"


def is_anagram(s1, s2):
    dic_map1 = {}
    dic_map2 = {}
    for char in s1:
        if char in dic_map1:
            dic_map1[char] = 1 + dic_map1.get(char, 0)
    for char in s2:
        if char in dic_map2:
            dic_map2[char] = 1 + dic_map2.get(char, 0)
    for key in dic_map2:
        if key not in dic_map1 and dic_map1[key] != dic_map2[key]:
            return False
    return True


print(is_anagram(string1, string2))
print(is_anagram(string3, string4))


string1 = "salesman"
string2 = "nameless"


def are_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    return Counter(string1) == Counter(string2)


print(are_anagram(string3, string4))


def anagram(s1, s2):
    print(s1, s2)
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


print(anagram(string1, string2))


'''
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Example: s = mom

The list of anagrammatic pairs is [m,m], [mo, om], so output is 2.

Example: s = abba, output is 4: [a,a],[ab,ba],[abb,bba],[b,b]

Example: s = abcd, output is 0

Example: s = abac, output is 2 --> [a,a], [ab, ba]
             i  j
             l=1: a, a +1             i[a] = 1, j[a] = 1
             l=2: ab, ac              i[a]-1, i[b]=1, i[c]=0  j[a]=1 j[b]=0 j[c]=1
            
             l=1: a, b
             l=2: ab, ba  +1
             l=3: aba, bac

Example: s = kkkk, output is 10 [[0,1],[1,2], [0,1],[2,3], ...]
                                   k     k       k    k 

Constraint: 2 <= |s| <= 100

abba


def 

'''


print("#####\n")


def sherlock_and_anagrams(s):
    def count_anagrams(current_index, arr):
        current_element = arr[current_index]
        arr_rest = arr[current_index + 1:]
        counter = 0

        for i in range(len(arr_rest)):
            if len(current_element) == len(arr_rest[i]) and is_anagram(current_element, arr_rest[i]):
                counter += 1

        return counter

    def get_all_substrings(input_str):
        substrings = []
        for i in range(len(input_str)):
            for j in range(i + 1, len(input_str) + 1):
                substrings.append(input_str[i:j])
        return substrings

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)

    duplicates_count = len([v for i, v in enumerate(s) if s.index(v) != i])

    if not duplicates_count:
        return 0

    anagrams_count = 0
    substrings_arr = get_all_substrings(s)

    for i in range(len(substrings_arr)):
        anagrams_count += count_anagrams(i, substrings_arr)

    return anagrams_count


# Example usage:
s = "abba"
result = sherlock_and_anagrams(s)
print(result)

print(sherlock_and_anagrams("mom"))

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

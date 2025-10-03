""" 
Ransom Note


Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


"""


from collections import Counter


def can_construct(ransom_note, magazine):
    for c in ransom_note:
        if c not in magazine:
            return False
        # remove the first occurrence of the character from the magazine
        magazine = magazine.replace(c, '', 1)
    return True


print(can_construct("a", "b"))
print(can_construct("aa", "ab"))
print(can_construct("aa", "aab"))


def can_construct_2(ransom_note, magazine):
    count = {}
    for c in magazine:
        count[c] = count.get(c, 0) + 1
    for c in ransom_note:
        if count.get(c, 0) == 0:
            return False
        count[c] -= 1
    return True


print(can_construct_2("a", "b"))
print(can_construct_2("aa", "ab"))
print(can_construct_2("aa", "aab"))


def can_construct_3(ransom_note, magazine):
    return all(ransom_note.count(c) <= magazine.count(c) for c in set(ransom_note))


print(can_construct_3("a", "b"))
print(can_construct_3("aa", "ab"))
print(can_construct_3("aa", "aab"))


def can_construct_4(ransom_note, magazine):
    count = Counter(magazine)

    for c in ransom_note:
        if count[c] == 0:
            return False
        count[c] -= 1
    return True


print(can_construct_4("a", "b"))
print(can_construct_4("aa", "ab"))
print(can_construct_4("aa", "aab"))

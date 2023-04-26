# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter 
def can_construct(ransom_note, magazine):
    _magz = Counter(magazine) # char: number
    
    for c in ransom_note:
        if _magz[c] == 0:
            return False 
        _magz[c] -= 1
    return True


print(can_construct("aa", "aab"))
    
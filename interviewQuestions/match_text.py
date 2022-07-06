#  Write a Program to match a string that has the letter ‘a’ followed by 4 to 8 'b’s.
import re

def match(text):
    pattern = "ab{4,8}"
    if re.search(pattern, text):
        return "match found"
    else:
        return "match not found"

print(match("abc"))
print(match("aabbbbc"))



# def is_palindrome(s):
#     result = []
#     for char in s.lower():
#         if char.isalnum():
#             result.append(char)
#     return True if result == result[::-1] else False
    
        
s = "A man, a plan, a canal: Panama"
# print(is_palindrome(s))

def is_palindrome(s):
    l, r = 0, len(s) - 1

    # Move the pointers towards the middle of the string
    while l < r:
        # Ignore non-alphanumeric characters
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1

        # Check if the characters at the pointers are equal, ignoring case
        if s[l].lower() != s[r].lower():
            return False

        # Move the pointers to the next characters
        l += 1
        r -= 1

    # If the pointers have crossed, the string is a palindrome
    return True

print(is_palindrome(s))
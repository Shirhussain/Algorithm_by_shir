# Program to print ASCII Value of a character

import string 

print(ord("a")) 
data = map(lambda x: ord(x), string.ascii_letters)
print(list(data))
# help(string)

# ascii_lowercase 
# ascii_uppercase 
# asscii_letters 


# or:
text = input("Enter yur string to see the asci  cahr: ")
for i in text:
    print(ord(i))

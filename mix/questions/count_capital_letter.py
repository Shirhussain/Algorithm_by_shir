# Write Python logic to count the number of capital letters in a file.
with open("someRandomWord.txt", "r") as myFile:
    count = 0 
    for i in myFile.read():
        if i.isupper():
            count += 1
    print(count)        
    
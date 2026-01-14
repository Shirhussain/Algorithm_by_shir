import os
def hasEvenByteSize(full_path):
    # return true if the file has size
    
    file_size = os.path.getsize(full_path)
    print("file size: ", file_size)
    return file_size % 2 == 0

curr_path = "/Users/shirhussaindanishyar/Data/Code/algorithm-learning/recursion/deepDive/recursive_book_of_recursion"

print(hasEvenByteSize(curr_path))


def hasEveryVowel(full_path):
    "return if it has 'a,e,i,o,u'"
    name = os.path.basename(full_path)
    return ('a' in name) and ('e' in name) and ('i' in name) and ('o' in name) and ('u' in name)

print(hasEveryVowel(curr_path))

def walk(folder, mach_func):
    """Calls the match function with every file in the folder and its
    subfolders. Returns a list of files that the match function
    returned True for."""
    matchedFiles = []
    folder = os.path.abspath(folder)
    
    for name in os.listdir(folder):
        file_path = os.path.join(folder, name)
        if os.path.isfile(file_path):
            if mach_func(file_path):
                matchedFiles.append(file_path)
        elif os.path.isdir(file_path):
            matchedFiles.extend(walk(file_path, mach_func))
            
    return matchedFiles

print(walk(".", hasEvenByteSize))
print(walk("../", hasEveryVowel))


def callFunction(func):
    func()
    func()
    

def sayHi():
    print("Hi")
    
def say_good_by():
    print("by by")

callFunction(say_good_by)
callFunction(sayHi)


def subSequence(string):
    result = []
    
    def helper(i, temp_list):
        if i == len(string):
            # join list into string
            result.append("".join(temp_list))
            return
        
        # pick the current character
        helper(i + 1, temp_list+ [string[i]])
        
        # do not pick the current character
        helper(i + 1, temp_list)
    
    helper(0, [])
    return result

print("result of ABCD subsequences:", subSequence("ABCD"))


def permutations(string):
    result = []
    chars = list(string)
    
    def helper(i):
        if i == len(chars):
            result.append("".join(chars))
            return
        
        for j in range(i, len(chars)):
            chars[i], chars[j] = chars[j], chars[i] # swap
            helper(i+1)
            chars[i], chars[j] = chars[j], chars[i] # undo swap
    helper(0)
    return result

print("permutations: ", permutations("ABC"))


def permutation_2(string):
    result = []
    sol = []
    
    def backtrack():
        if len(sol) == len(string):
            result.append("".join(sol))
            return 
        
        for char in string:
            if char not in sol:
                sol.append(char)
                backtrack()
                sol.pop()
    backtrack()
    return result

print("permutation backtrack second way: ", permutation_2("ABC"))
                


def getPerms(chars, indent=0):
    print('.' * indent + 'Start of getPerms("' + chars + '")')
    if len(chars) == 1:
        # BASE CASE
        print('.' * indent + 'When chars = "' + chars + '" base case returns', chars)
        return [chars]
   
    # RECURSIVE CASE
    permutations = []
    head = chars[0]
    tail = chars[1:]
        
    tailPermutations = getPerms(tail, indent + 1)
    for tailPerm in tailPermutations:
        print('.' * indent + 'When chars =', chars, 'putting head', head, 'in all places in',
        tailPerm)
        for i in range(len(tailPerm) + 1):
            newPerm = tailPerm[0:i] + head + tailPerm[i:]
            print('.' * indent + 'New permutation:', newPerm)
            
    permutations.append(newPerm)
    print('.' * indent + 'When chars =', chars, 'results are', permutations)
    return permutations

print('Permutations of "ABCD":')
print('Results:', ','.join(getPerms('ABCD')))




# opening the lock of a cycle 

def open_cycle_lock(string):
    for a in string:
        for b in string:
            for c in string:
                for d in string:
                    print(a, b, c, d)

# open_cycle_lock("ABCD")



def getPermsWithRep(chars, permLength=None, prefix=''):
    indent = '.' * len(prefix)
    print(indent + 'Start, args=("' + chars + '", ' + str(permLength) + ', "' + prefix + '")')
    if permLength is None:
        permLength = len(chars)
    # BASE CASE
    if (permLength == 0):
        print(indent + 'Base case reached, returning', [prefix])
        return [prefix]
    
    # RECURSIVE CASE
    # Create a new prefix by adding each character to the current prefix.
    results = []
    print(indent + 'Adding each char to prefix "' + prefix + '".')
    for char in chars:
        newPrefix = prefix + char
        # Decrease permLength by onez because we added one character to the prefix.
        results.extend(getPermsWithRep (chars, permLength - 1, newPrefix))
    print(indent + 'Returning', results)
    return results
print('All permutations with repetition of JPB123:')
print(getPermsWithRep('JPB123', 4))
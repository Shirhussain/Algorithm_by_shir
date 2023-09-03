""" 
    count constract (abcdef, [ab, abc, cd, def, abcd])
    
                                    abcdef
                                ab/   abc|  abcd\
                            cdef        def      ef 
                            cd|          def|    
                             ef            "" 
    
    if we remain with "" we return one `1` otherwise we return 0 
"""


def count_construct(target, word_break):
    if target == "":
        return 1

    count = 0
    for word in word_break:
        if target.startswith(word):
            suffix = target[len(word):]
            rest_count = count_construct(suffix, word_break)
            count += rest_count
    return count


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))

# time O(m*n^m ) Space = O(m^2)


def count_construct_memo(target, word_break, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    total_count = 0
    for word in word_break:
        if target.startswith(word):
            suffix = target[len(word):]
            rest_count = count_construct_memo(suffix, word_break, memo)
            total_count += rest_count
    memo[target] = total_count
    return total_count


print(count_construct_memo('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct_memo("eeeeeeeeeeeeeeeeeeeeeeeeeeeee", [
      "e", "ee", "eee", "ef"]))

# Time O(n*m^2) Space O(m^2)

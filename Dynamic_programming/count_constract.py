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

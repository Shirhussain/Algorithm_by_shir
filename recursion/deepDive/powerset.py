# Input 1: 

# "abc"

# Output 1: 

# [ '', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c' ]


# Reason 1: 

# These are all the combinations of "abc"


# Input 2: 

# ''

# Output 2: 

# ['']

# Reason 2: 

# The only combination that can be made from an empty string is an empty string



# helper Method recursion
"""
1, create state variable(s)
2, return state variable(s)
3, instantiate and invoke helper method
4, base case(s)
5, recursive case 

"""

def powerset(word):
    # [ '', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c' ]
    # in this recursive every level (" ")---> don't add and "add" ---> "abc..." 
    # each level one character
    #                                 ""
    #                             /.      \
    #                           ""        "a"
    #.                       /.    \.       /   \
    #                       ""     "b".    "a".    "ab"
    #                     /.\.    /. \.   /. \.     /. \
    #                   ""  "c". "b"  "bc" "a" "ac" "ab" "abc"
    result = []
    
    def helper(build, depth):
        if depth == len(word):
            result.append(build)
            return
        
        # use "don't add", "add tichniq"
        helper(build, depth+1) # don't add 
        helper(build + word[depth], depth+1) #
        
    helper("", 0)
    return result

print(powerset("abc"))
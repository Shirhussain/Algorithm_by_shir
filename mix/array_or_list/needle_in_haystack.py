""" 
function int[]/list grep(string haystack, string needle)
haystack = "aaabcdddbadddabcdefghi"
           "zyxw"
needle = "abc"

[2,14]

"aaaaa"
"aaa"
[0,1,2]

""
[]

needle = ""
[]

Time: O(h*n) -> O(h)
Space: O(1)


aaabcdddbadddabcdefghi
 ^
abc
 ^

"""


def grep(needle, haystack):
    result = []

    for i in range(len(haystack)-len(needle)):
        while j < len(needle):
            if haystack[i+j] != needle[j]:
                break
            j += 1

        if j == len(needle):
            result.append(i)
    return result


print(grep("abc", "aaabcdddbadddabcdefghi"))

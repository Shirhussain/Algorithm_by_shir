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
        j = 0
        print("i:", i, "and num[i]: ", haystack[i])
        for j in range(j, len(needle)):
            print("j: ", j, "and needle[j]: ", needle[j])
            # if haystack[i+j] != needle[j]:
            #     break

        if j == len(needle):
            result.append(j)
    return result


print(grep("abc", "aaabcdddbadddabcdefghi"))

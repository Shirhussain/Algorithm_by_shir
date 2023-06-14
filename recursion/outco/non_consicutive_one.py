"""
Non-Consecutive Ones

Given a positive integer n, return an array of all the binary strings of length n that DO NOT contain consecutive 1s.

Input: n (Integer)
Output: [Str] (Array of Strings)
Example
Input: 2
Output: ["00", "01", "10"]

Input: 3
Output: ["000", "001", "010", "100", "101"]

Input: 0
Output: ['']

Input: 1
Output: ["0", "1"]

Time Complexity: O(2^N)
Space Complexity: O(2^N)

1. Understand
2. Diagram
3. Pseudocode
4. Code


1. Reduce
2. Build
---------------------
Reduce method:

                             (n)
                          /0       \1
                        (n-1)     (n-1) 
                        

                             (0)

                             
Build method:                ([], n)

---------------------
Diagram - concrete values and the state of the program

result = ["000", ]           
n = 3

                             ("")                3 i
                        /              \
                     ("0")            ("1")      2 i
                /           \         /      
            ("00")        ("01")  ("10")         1 i
          /     \        /           /\
    ("000")   ("001") ("010")  ("100") ("101")   0 i


---------------------
Pseudocode - generalized patterns and instructions

define nonconsecutive_ones(n):
  result = []

  define helper(build_string):
    # base case(s)
    if length of build string is n:
      add build_string to result
      return
  
    # recursive case(s)
    helper(build_string + "0")
    if build_string is empty the last char isn't 1:
      helper(build_string + "1")
    

function nonconsecutive_ones(n) {
  
}

"""

# def nonconsecutive_ones(n):
#   result = []

#   def helper(build_string):
#     # base case(s)
#     if len(build_string) == n:
#       result.append(build_string)
#       return
  
#     # recursive case(s)
#     helper(build_string + "0")
#     if not build_string or build_string[-1] == "0":
#       helper(build_string + "1")

#   helper("")
#   return result

def helper(build_string, result, n):
  print(build_string, result, n)
  if len(build_string) == n:
    result.append(build_string)
    return

  # recursive case(s)
  helper(build_string + "0", result, n)
  if not build_string or build_string[-1] == "0":
    helper(build_string + "1", result, n)


def ones(n):
  result = []
  helper("", result, n)
  return result

print(ones(3))



def generate_binary_strings(n):
    results = []
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)  # Convert to binary and pad with leading zeros
        results.append(binary)
    return results

n = 3
binary_strings = generate_binary_strings(n)
print(binary_strings)

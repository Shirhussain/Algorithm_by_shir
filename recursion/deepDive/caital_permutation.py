"""
1) Can we get another example of diagramming for a recursive problem?

231 - Capital Permutations
Given a string str of lowercase alphabetical characters, return the set of all permutations of those characters in upper AND lowercase.


Input: str (String)
Output: [Str] (Array of Strings)
Example
Input: "abc"
Output: ["ABC", "ABc", "AbC", "aBC", "Abc", "aBc", "abC", "abc"]


Advanced:

Input: "A1d3"
Output: ["A1D3", "a1D3", "A1d3", "a1d3"]


                                ("abc")

                                 012
                                 abc
 
                                 ("")                          0 a
                              /        \
                          ("A")        ("a")                   1 b
                        /     \          /      \
             ("AB")        ("Ab")      ("aB")       ("ab")     2  c
          /      \         /   \       /     \      /     \
     ("ABC")   ("ABc") ("AbC") ("Abc")("aBC")("aBc")("abC")("abc")
                  


Tail Recursion
 * a type of recursion where the recursive call is the last thing to happen in the function -> there is essentially no need to return the function at all

  0    1    2    3    4
['a', 'b', 'c', 'd', 'e', ...]


(4)
-------
CALL STACK


print(arr, 0) -> print(arr, 1) -> print(arr, 2) -> print(arr, 3)

LISP

"""




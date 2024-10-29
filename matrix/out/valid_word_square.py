'''
422. Valid Word Square

Given an array of strings words, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns). 

Example 1: Input: words = ["abcd",
                           "bnrt",
                           "crmy",
                           "dtye"] 
Output: true Explanation: The 1st row and 1st column both read "abcd". The 2nd row and 2nd column both read "bnrt". The 3rd row and 3rd column both read "crmy". The 4th row and 4th column both read "dtye". Therefore, it is a valid word square. 

Example 2:


Input: words = ["abcd",
                "bnrt",
                "crm",
                "dt"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crm".
The 4th row and 4th column both read "dt".
Therefore, it is a valid word square.

Example 3:
Input: words = ["ball","area","read","lady"]
Output: false
Explanation:
The 3rd row reads "read" while the 3rd column reads "lead".
Therefore, it is NOT a valid word square.


Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 500 words[i] consists of only lowercase English letters.

https://leetcode.com/problems/valid-word-square/
'''

'''
["abc",
 "de"
 "f"]
     [ "abcd",
        "bnrt",
        "crm",
        "dt"]
            1
       0,0 0,1
   1   1,0

'''
'''
Pseudocode

for r from 0 to length of words-1
  if number of elements in row r != number of elements in column at r 
    return false
  for each index of row r
    if words[index,r] != words[r,index] return false

return true

'''

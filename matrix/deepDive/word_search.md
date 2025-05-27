'''
Given a matrix of characters a-z and a word, return a boolean as to whether the word can be found
within the matrix. Words can be built from adjacent letters: up, down, left, right, or diagonal.
However, the same matrix element cannot be used multiple times in the same word.

Input: Matrix of characters from a-z, String word
Output: Boolean as to whether word can be found in matrix
'''
'''
Example:

        a b c d
        e f g h
        i j k l
        m n o p

word: lop
output: true

word: pop
output: false

Constraints:
Square NxN matrix, 1 <= N <= 1,000
Word w length is 1 == |w| <= 3
Matrix and word are lowercase letters only
Word is not necessarily a word that will be found in a dictionary.
We are allowed to modify the matrix

What is the time complexity of a backtracking algorithm portion of the solution for this problem?

'''
'''
Diagram:

a b c d
e f g o
i j k l
m n h p

word: lop

                        0,0, 0 -> false
                        0,1, 0 -> false
                          ....
                        2,3, 0 --> false
              1,3, 1  --> false
      0,2, 2  0,3, 2 ...
      false   false   false


--> false

'''
'''
pseudocode

def word_search(matrix, word):

def dfs(i,j, index):
if (i,j) is outside the matrix
return false
if index is past the end of word
return true
if matrix(i,j) is not word[index]
return false # if matrix(i,j) is not a lowercase letter # return false

    mark matrxi(i,j) as visited: store capital version of letter in matrix(i,j),
    for each neighbor of (i,j) (8 of them in general)
      if dfs(neighbor, index+1)
        unmark matrix(i,j) as visited
        return true
    unmark matrix(i,j) as visited: store lower case version of letter in matrix(i,j)
    return false

for each m, n starting point in the matrix
if dfs(m,n, 0)
return true
return false

'''

'''
Runtime: O(1,000 x 1,000 x 8^3) ~ O(2^9 \* 10^6)

'''

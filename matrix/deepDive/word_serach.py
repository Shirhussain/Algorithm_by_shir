'''
Given a matrix of characters a-z and a word, return a boolean as to whether the word can be found 
within the matrix. Words can be built from adjacent letters: up, down, left, right, or diagonal. 
However, the same matrix element cannot be used multiple times in the same word.

Input: Matrix of characters from a-z, String word
Output: Boolean as to whether word can be found in matrix
'''
'''
1. Understanding
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
Square NxN matrix, 1 <= N <= 100 = 10^2
Word w length is 1 == |w| <= 5
Matrix and word are lowercase letters only
Word is not necessarily a word that will be found in a dictionary.
We are allowed to modify the matrix

'''

'''
Diagram

                        a b c d
                        e f g h
                        i j k L
                        m n O P

                        
                                (2,3), 0

                            up to 8 children

                            up to 8^2 grandchildren

                            up to 8^3 great-grandchildre

      1:                        (3,2), 1  -> true
      
      2:                        (3,3), 2 -> true
      
'''

'''
Pseudocode

def word_search(matrix, word)

  # Return true if word is found in matrix beginning at location.
  # Probably recursive...
  def IsFound((i,j), k)
    if k is last letter in word
      return true
    for each neighbor of (i,j) that is in the matrix and that matches word[k+1]
      upcase neighbor
      if IsFound(neighbor, k+1)
        return true
      downcase neighbor
    return false

Time for IsFound: O(8^5) = O((2^3)^5) = O(2^15) = 32K

    
  nested loop over matrix
    if current character is the first character of word
      upcase the current character
      if IsFound(current_position, 0)
        return true
      downcase the current character
  return false


Overall time: O(10^2*10^2 * 32K) = 10^4 * 3.2*10^4 = 3.2 * 10^8

'''


















""" 


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
      return false
    # if matrix(i,j) is not a lowercase letter
    #  return false
  
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
Runtime: O(1,000 x 1,000 x 8^3) ~ O(2^9 * 10^6)

'''
"""

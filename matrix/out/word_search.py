'''

Given a matrix of characters a-z and a word, return a boolean as to whether the word can be found within the matrix. Words can only be built from adjacent letters (up, down, left, right), but not diagonals. Same elements cannot be used multiple times in the same word.

Input: Matrix of characters from a-z, String word
Output: Boolean as to whether word can be found in matrix

'''
'''
Input: board = 
[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]], 
word = "ABCCED"
Output: true

word = "SEE"
Output: true

word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase English letters.

'''
'''
Diagram

[["A","B","C","E"],
 ["S","F","C","S"],
 ["A","D","E","E"]], 

 word = "ABCCED"

                         A,0
                  S,1              B,1
                  X         a    F              C.2
                            X    X      b       C          E
                                        X   c F S     E
                                            X X X   c D E
                                                    X !
                
                                        
'''

'''
define word_search(matrix, word):

 def helper(start, index):

    # success base case
    if index is past the end of word:
      return true

    # failure base case
    if matrix[start] is not word[index]
      return false

    change case of letter at matrix[start]
    for each neighbor (go up/down/left/right from down)
      if helper(neighbor, index+1)
        return true
    change case of letter at matrix[start]
    return false

  for each position in array
    if helper(position, 0)
      return true
    return false
  

'''
'''
Time: O(4^15) = 2^30 ~ 10^9

'''

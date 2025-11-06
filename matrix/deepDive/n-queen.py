# https://leetcode.com/problems/n-queens/

'''
Diagram

                                []
                   Q...     .Q..
         

   Q...    Q...        Q...      Q...
   Q...    .Q..        ..Q.      ...Q

    XX      XX      

                 Q...
                 ..Q.
                 Q...

                 xx

Runtime: O(4^4) 

In general: O(n^n) ~ 9^9

'''
'''
def valid(board): # returns true iff valid
  if length of board is 1 then return true
  find index of queen on the last row of board
  col1 = index-1
  col2 = index
  col3 = index+1
  for each row above last row
    if Q at any of [row, colX] (Note: if colX is off the board, ignore it)
      return false
    col1 -= 1
    col3 += 1
  return true
  

def n_queens(n):

  create empty answer_list

  def dfs(board): # board is list of strings
    if board is not valid (queen attacking another queen)
      return
    if we are a leaf (length of board is n)
      add copy of board to answer_list
      return
    for each row_string, e.g., "Q...", .Q.., ..Q., ...Q
      append row_string to board
      dfs(board)
      pop last string from board
    
  create empty_board, e.g., []
  dfs(empty_board, 0)
  
  return answer_list


'''

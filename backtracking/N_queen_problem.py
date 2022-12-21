# place 4 queen on 4x4 chase board, in such a manner that no two queens can attack each other

# not the same column
# not the same row
#not diagonal

# 1- start in left most column
# 2- if all queen are paaced
# return true
# 3) try all rows in the current column
#       Do the following for every tried row.
#       a) if the queen can be placed safely in this row, then mark this row
#          [row,column] as par of the solution and recursively check if placing queen
#           here lead to teh solution.
#       b) if placing the queen in [row, column] lead to teh solution then return true
#       c) if placing the queen doesn't lead to teh solution then unmark this [row, column]
#       backtacking and go to the step (a) to try other rows.

# 4) if all row has been tried and nothing worked then return false to trigger back tracking.

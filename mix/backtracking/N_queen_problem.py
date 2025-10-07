# place 4 queen on 4x4 chase board, in such a manner that no two queens can attack each other

# not the same column
# not the same row
# not diagonal

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

class NQueues(object):
    def __init__(self, n):
        self.n = n
        self.chase_table = [[0 for i in range(n)] for j in range(n)]

    def print_chase_table(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chase_table[i][j] == 1:
                    print(" Q ", end=" ")
                else:
                    print(" - ", end=" ")
            print("\n")

    def is_place_safe(self, row_index, column_index):
        # check horizontally if there is any in the row
        for i in range(self.n):
            if self.chase_table[row_index][i] == 1:
                return False
        # then check diagonally
        # top left to right bottom
        j = column_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chase_table[i][j] == 1:
                return False
            j = j - 1
        # the same just from top right to bottom left diagonally
        j = column_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chase_table[i][j] == 1:
                return False
            j = j - 1
        return True

        #  we don't need to check vertically because we place one qunuen in each column

    # amount of qunuen is equal to column index so i use column index

    def solve(self, column_index):
        if column_index == self.n:
            return True

        for row_index in range(self.n):
            # check for secon queen to finde a convinian place
            if self.is_place_safe(row_index, column_index):
                self.chase_table[row_index][column_index] = 1
            # this  means we palce all sucessfully
                if self.solve(column_index + 1):
                    return True
                self.chase_table[row_index][column_index] = 0
        return False

    def solve_N_Queun(self):
        if self.solve(0):
            self.print_chase_table()
        else:
            print("there is no solution for the problem")


queens = NQueues(4)
queens.solve_N_Queun()

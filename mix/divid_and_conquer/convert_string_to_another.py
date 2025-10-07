# S1 and S2 are given string
# convert S2 to S1 using delete , insert, or replace operations
# find minimum count of edit operations

# exmple:

# S1: table       Delete
# S2: Tgable                -------> f(2,3)

# S1: Table        Insert
# S2: Tble                  -------> f(2,3)


# S1: Table Replace
# S2: Tcble                  -------> f(3,3)

def find_minimum_operation(s1, s2, index1, index2):
    if index1 == len(s1):
        # delete the rest of s2
        return len(s2)-index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return find_minimum_operation(s1, s2, index1+1, index2+1)
    else:
        delete_op = 1+find_minimum_operation(s1, s2, index1, index2+1)
        insert_op = 1+find_minimum_operation(s1, s2, index1+1, index2)
        replace_op = 1+find_minimum_operation(s1, s2, index1+1, index2+1)
        return min(delete_op, insert_op, replace_op)


# 0 means start from this index
print(find_minimum_operation("table", "tbrltt", 0, 0))
print(find_minimum_operation("table", "tbrlt", 0, 0))
print(find_minimum_operation("table", "tabrltt", 0, 0))
print(find_minimum_operation("table", "tbrltte", 0, 0))
print(find_minimum_operation("table", "tabeltt", 0, 0))

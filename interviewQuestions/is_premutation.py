# premuaation and combination, for combination ordring is not important but for premuataion is
#formula  P(n,r) = n!/(n-r)!
first_lst = [7,8,9,0]
second_lst = [9,7,8,0]

lst1=["a","b","c"]
lst2 = ["c","a","b"]
#work just for integer
def is_premutation(list1,list2):
    if len(list1) != len(lst2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

print(is_premutation(lst1, lst2))

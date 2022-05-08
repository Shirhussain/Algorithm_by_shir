lst = [1,3,4,6,8,7,5,10]


#best on sumation of sequeance formalla which is  n(n+1)/2
# this one only work for one number but not a list of numbers

# def find_missing(list, n):
#     sum1 = 10*(10+1)/2
#     sum2 = sum(list)
#     print(sum1-sum2)

# find_missing(lst, 10)




# mising = [ele for ele in range(max(lst)+1) if ele not in lst]

# print(mising)



#sedonc way is with the set
missing_set = list(set(range(max(lst)+1)) - set(lst))
print(missing_set)
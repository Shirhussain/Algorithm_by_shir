
# Python program to check if there is Pythagorean
# triplet in given array
 
# Returns true if there is Pythagorean
# triplet in ar[0..n-1]

# this is Naive way but i do it

array = [3, 1, 4, 6, 5]
len_arry = len(array)

def isTriple(arr, len_num):
    j = 0
    for i in range(len_num-2):
        for k in range(j+1, len_num):
            for j in range(i+1, len_num-1):
                x = arr[i]*arr[i]
                y = arr[j]*arr[j]
                z = arr[k]*arr[k]
                if (x==y+z or y ==x+z or z == y+x): return 1
    return 0

if(isTriple(array, len_arry)):
    print("yes")
else:
    print("no")




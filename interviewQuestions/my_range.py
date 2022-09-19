# Python program for reversal algorithm of array rotation

# Function to reverse arr[] from index start to end
# def rverseArray(start, step, end):
# 	while (start < end):
# 		temp = arr[start]
# 		arr[start] = arr[end]
# 		arr[end] = temp
# 		start += 1
# 		end = end-1


def my_range(end, start=0, step=1):
    new_list = []
    print(start)
    while start < end:
        start += step
        print(start)
        if start + step  >= end:
            break
        
    
# my_range(200, 5, 20)
# my_range(20)
my_range(100, 10, 5)


    
    

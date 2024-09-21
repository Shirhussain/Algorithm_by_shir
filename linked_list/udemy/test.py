my_list = [1,2,3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,]

def find_jam(lst):
    even = []
    for i in my_list:
        if i%2 == 0:
            even.append(i)
    return even

print(find_jam(my_list))
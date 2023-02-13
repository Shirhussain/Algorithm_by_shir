#Python program to print all Prime numbers in an Interval
#this is my solution
def prime_in_interval(x,y):
    for i in range(x,y):
        if i%2!=0:
            print(i)

prime_in_interval(10,20)

#geeks for geeks solution
# Python program to print all
# prime number in an interval

def prime(x, y):
	prime_list = []
	for i in range(x, y):
		if i == 0 or i == 1:
			continue
		else:
			for j in range(2, int(i/2)+1):
				if i % j == 0:
					break
			else:
				prime_list.append(i)
	return prime_list

# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
	print("There are no prime numbers in this range")
else:
	print("The prime numbers in this range are: ", lst)

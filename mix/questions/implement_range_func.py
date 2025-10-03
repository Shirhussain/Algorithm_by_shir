def my_range(end, start=0, step=1):
    while start < end:
        start += step
        print(start)
    
my_range(10, 5, 2)

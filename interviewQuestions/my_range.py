# def my_range(end, start=0, step=1):
#     print(start)
#     while start < end:
#         start += step
#         yield start
#         if start + step >= end:
#             break


# my_range(200, 5, 20)
# my_range(20)
# my_range(100, 10, 5)


# my_range(100)


# def custom_range(stop):
#     i = 0
#     while i < stop:
#         yield i
#         i += 1


# for i in custom_range(10):
#     print(i)


# assinment:
# framework to build a libarary

# typeing: i have to read


def myRange(start, step=None, stop=None):
    if step == None and stop == None:
        start, step, stop = 0, 1, start
        while start < stop:
            yield start
            start += step
    elif stop == None:
        start, step, stop = start, 1, step
        while start < stop:
            yield start
            start += step
    while start < stop:
        yield start
        start += step


# for i in myRange(1, 2, 10):
#     print(i)


# for i in rrange(4, 2, 20):
#     print(i)


def custome_range(*args):
    if len(args) == 1:
        start, step, stop = 0, 1, args[0]
        while start < stop:
            yield start
            start += step
    elif len(args) == 2:
        start, step, stop = args[0], 1, args[1]
        while start < stop:
            yield start
            start += step
    else:
        start, step, stop = args[0], args[1], args[2]
        while start < stop:
            yield start
            start += step


for i in custome_range(1, 10, 100, 4):
    print(i)

# for i in custome_range(3, 30):
#     print(i)

# for i in custome_range(3, 5, 64):
#     print(i)

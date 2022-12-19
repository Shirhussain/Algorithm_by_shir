my_list = [
    ('a', 3, "f", 11),
    ('b', 10, "f", 11),
    ('c', 20, "f", 11),
    ('a', 40, "f", 11),
    ('a', 50, "f", 11),
    ('c', 11)
]

# output = {
#     "a": [3,40,50],
#     "b": [10],
#     "c": [20, 11]
# }

# my way
out_put = {}
for item in my_list:

    if item[0] in out_put:
        out_put[item[0]].append(item[1])
    else:
        out_put[item[0]] = [item[1]]

print(out_put)

# hakimi way
for key, value, *rest in my_list:
    if key in out_put:
        out_put[key].append(value)
    else:
        out_put[key] = [value]

print(out_put)

def capitalize_first(lst):
    new_list = []
    for word in lst:
        result = word.title()
        new_list.append(result)
    return new_list

name = ["shir", "hussain", "danishyar", "amir", "rana", "sidiqa" ]

cpf = capitalize_first(name)
print(cpf)


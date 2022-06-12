def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])


name = ["shir", "hussain", "danishyar", "amir", "rana", "sidiqa"]

cpw = capitalizeWords(name)
print(cpw)
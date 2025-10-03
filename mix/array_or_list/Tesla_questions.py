# 1. Find the kth largest element in an unsorted list. Note that it is the Kth largest element in the sorted order, not the Kth distant element.
# For example, given [3,2,1,5,6,4] and k = 2, return 5.
# Note: You may assume k is always valid, 1 ≤ k ≤ list's length.


arr = [3, 2, 1, 5, 6, 4]
# k = 2


def find_the_kth_largest_element(arr,  k):
    new_arr = sorted(arr)
    if k == 0:
        return new_arr[-1]
    return new_arr[-k]


print(find_the_kth_largest_element(arr, 2))

assert find_the_kth_largest_element(arr=[3, 2, 1, 5, 6, 4], k=2) == 5
assert find_the_kth_largest_element(
    arr=[-9, -5, -12, 1, 5, 9, 100, 2, 0], k=0) == 100
assert find_the_kth_largest_element(
    arr=[-9, -5, -12, 1, 5, 9, 2, 12, 13, 0], k=8) == -5


def k_th_large(arr, k):
    while k > 1:
        max_value = max(arr)
        arr.remove(max_value)
        k -= 1
    return max(arr)


print(k_th_large(arr, 2))

assert k_th_large(arr=[3, 2, 1, 5, 6, 4], k=2) == 5
assert k_th_large(arr=[-9, -5, -12, 1, 5, 9, 100, 2, 0], k=0) == 100
assert k_th_large(arr=[-9, -5, -12, 1, 5, 9, 2, 12, 13, 0], k=8) == -5


def find_m_large(arr, m):
    arr.sort()
    new_index = len(arr) - m
    return arr[new_index]


arr = [3, 2, 1, 5, 6, 4]
print(find_m_large(arr, 2))


assert find_m_large(arr=[3, 2, 1, 5, 6, 4], m=2) == 5
assert find_m_large(arr=[-9, -5, -12, 1, 5, 9, 100, 2, 0], m=2) == 9


# 2. You are given a list of N numbers. Create a single list comprehension in Python to create a new list that contains only those values which have even numbers from elements of the list at even indices.
# For instance if list[4] has an even value it should be included in the new output list because it has an even index but if list[5] has an even value it should not be included in the list because it is not at an even index.

# my solution

def even_idx_items(lst):
    new_list = []
    for idx, item in enumerate(lst):
        if idx % 2 == 0 and item % 2 == 0:
            new_list.append(item)
    return new_list


arr = [5, 4, 6, 1, 0, 2, 7, 9, 1]
new_arr = [0, 13, 27, 5, 2, 4, -2, 5, 6]
print(even_idx_items(new_arr))


def even_idx_items(lst):
    out_put = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            out_put.append(lst[i])
    return out_put


# Test
assert (even_idx_items([5, 4, 6, 1, 0, 2, 7, 9, 1])) == [6, 0]
assert (even_idx_items([0, 13, 27, 5, 2, 4, -2, 5, 6])) == [0, 2, -2, 6]


#######################################################################################################
"""
3. Count the vehicle's color from the list of vehicle configuration and return the top 3 most common ones and their frequency.
If there is a tie in top 3 most common color, include the ones that are tied.
"""

# my solution


def count_configurations(vehicles: list) -> dict:
    only_colors = {}
    out_put = {}
    for car in vehicles:
        for key, value in car.items():
            if key == "color":
                if key in only_colors and value in out_put:
                    only_colors[key].append(value)
                    out_put[value] += 1
                else:
                    only_colors[key] = [value]
                    out_put[value] = 1
    out_put.popitem()
    # or
    # result = dict(list(out_put.items())[:-1])
    return out_put


# others
def count_configurations(vehicles: list) -> dict:
    # Count colors
    countColors = {}
    for vehicle in vehicles:
        if vehicle["color"] in countColors:
            countColors[vehicle["color"]] += 1
        else:
            countColors[vehicle["color"]] = 1

    print(countColors)
    # Find 3rd largest element
    result = {}

    while len(result.keys()) < 3:
        maxValue = max(countColors.values())
        # print(maxValue)
        listKeywords = []

        # Add
        for keyword in countColors.keys():
            # We have the most common color
            if countColors[keyword] == maxValue:
                # Add to dict
                result[keyword] = countColors[keyword]
                listKeywords.append(keyword)

        for key in listKeywords:
            # Delete from countColors
            countColors.pop(key)
    print("result", result)
    # Return the top 3 most common color
    # [1,2,3,4,4,4,4]
    return result


vehicles = [
    {"model": "S", "drive": "AWD Dual Motor", "color": "red"},
    {"model": "Y", "drive": "AWD Dual Motor", "color": "deep_blue"},
    {"model": "3", "drive": "RWD", "color": "red"},
    {"model": "X", "drive": "AWD Tri Motor", "color": "red"},
    {"model": "SX", "drive": "AWD Tri Motor", "color": "silver"},
    {"model": "SX", "drive": "AWD Tri Motor", "color": "deep_blue"},
    {"model": "Y", "drive": "AWD Dual Motor", "color": "silver"},
    {"model": "SX", "drive": "AWD Tri Motor", "color": "deep_blue"},
    {"model": "3", "drive": "AWD Dual Motor", "color": "black"},
    {"model": "S", "drive": "AWD Dual Motor", "color": "red"},
]

print(count_configurations(vehicles))


# Test
assert (
    count_configurations(
        [
            {"model": "S", "drive": "AWD Dual Motor", "color": "red"},
            {"model": "Y", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "3", "drive": "RWD", "color": "red"},
            {"model": "X", "drive": "AWD Tri Motor", "color": "red"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "silver"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "deep_blue"},
            {"model": "Y", "drive": "AWD Dual Motor", "color": "silver"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "deep_blue"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "black"},
            {"model": "S", "drive": "AWD Dual Motor", "color": "red"},
        ]
    )
    == {"red": 4, "deep_blue": 3, "silver": 2}
)
assert (
    count_configurations(
        [
            {"model": "Y", "drive": "AWD Dual Motor", "color": "red"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "black"},
            {"model": "S", "drive": "AWD Dual Motor", "color": "red"},
            {"model": "X", "drive": "AWD Tri Motor", "color": "silver"},
            {"model": "S", "drive": "AWD Dual Motor", "color": "black"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "silver"},
            {"model": "X", "drive": "AWD Dual Motor", "color": "white"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "S", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "red"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "silver"},
            {"model": "X", "drive": "AWD Tri Motor", "color": "red"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "black"},
        ]
    )
    == {"deep_blue": 5, "red": 4, "black": 3, "silver": 3}
)
assert (
    count_configurations(
        [
            {"model": "Y", "drive": "AWD Dual Motor", "color": "red"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "red"},
            {"model": "SX", "drive": "AWD Tri Motor", "color": "black"},
            {"model": "S", "drive": "AWD Dual Motor", "color": "black"},
            {"model": "X", "drive": "AWD Tri Motor", "color": "silver"},
            {"model": "S", "drive": "AWD Dual Motor", "color": "silver"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "white"},
            {"model": "X", "drive": "AWD Dual Motor", "color": "white"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "deep_blue"},
            {"model": "3", "drive": "AWD Dual Motor", "color": "blue"},
        ]
    )
    == {"red": 2, "black": 2, "white": 2, "silver": 2, "deep_blue": 2}
)

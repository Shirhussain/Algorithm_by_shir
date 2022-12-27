# Given N numbers of houses along with the street with some amount of money
# Adjacent houses can't be stolen
# find the maximum amount that cna be stolen

def house_robber_top_down(houses, current_index, temp_dict):
    if current_index >= len(houses):
        return 0
    else:
        if current_index not in temp_dict:
            # here increasing index by to to skep one house
            steal_first_house = houses[current_index] + \
                house_robber_top_down(houses, current_index + 2, temp_dict)
            skipped_first_house = house_robber_top_down(
                houses, current_index+1, temp_dict)
            temp_dict[current_index] = max(
                steal_first_house, skipped_first_house)
        return temp_dict[current_index]


houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber_top_down(houses, 0, {}))


def houses_robber_bottom_up(houses, current_index):
    # i'm putting +2 because of the last index
    temp_arr = [0]*(len(houses)+2)
    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i]+temp_arr[i+2], temp_arr[i+1])
    return temp_arr[0]


new_houses = [6, 7, 1, 30, 8, 2, 4]
print(houses_robber_bottom_up(new_houses, 0))

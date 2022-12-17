# House roubber problem
# Given N number of houses along the street with the some amount of money with diffrent vlaue
# Adjecent houses can't be stolen because they have an alert system which polic will notice
# Find thee max amount can be stolen.


def max_value_house_robber(houses, current_index):
    if current_index >= len(houses):
        return 0
    else:
        # for stealing we have to skip one hose and go to the next house
        steal_first_house = houses[current_index] + \
            max_value_house_robber(houses, current_index+2)
        skip_first_house = max_value_house_robber(houses, current_index+1)
        return max(steal_first_house, skip_first_house)


houses = [6, 7, 1, 30, 8, 2, 4]
print(max_value_house_robber(houses, 0))

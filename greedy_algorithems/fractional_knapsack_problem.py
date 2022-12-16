# if we have a empty box how we can put it the best possible way

# calculate the density or ratio for each item.
# sort item based on the ratio
# take item with the highest ratio seqantaialy until wait allows
# and the next item as much as (fractional) as we can

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight


def knapsack_problem(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            total_value += i.value
        else:
            un_used_weight = capacity - used_capacity
            value = i.ratio * un_used_weight
            used_capacity += un_used_weight
            total_value += value

        if used_capacity == capacity:
            break
    print("Total value obtained : " + str(total_value))


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
my_list = [item1, item2, item3]

knapsack_problem(my_list, 50)

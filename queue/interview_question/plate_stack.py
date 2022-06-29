# if you ahve many plate on top of eachother then taht might be fall so you need to stack beside taht 
# === === === === 
# === === === === 
# === === === === 
# === === === === 
# === === === === 
#  like if you have mony plate on top of this will fall.

from calendar import c


class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        
    def __str__(self):
        return self.stacks
    
    def push(self, item):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])
        
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return None if len(self.stacks) == 0 else self.stacks[-1].pop()
    
    # poping form each category of the plate
    def pop_at(self, stack_num):
        if len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop()
        else:
            return None

custome = PlateStack(3)
custome.push(1)
custome.push(2)
custome.push(3)
custome.push(4)
custome.push(5)
# print(custome.pop())
# print(custome.pop())

# print(custome.pop_at(0))    
print(custome.pop_at(1))    
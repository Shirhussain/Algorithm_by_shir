# describe how you could use a single python list to implement three stack.

# for stack 1 [0],[1],[2] ----------> [0, n/3]
# from stack 2 [3],[4],[6] --------> [n/3, 2n/3]
# for stack 3 [7],[8],[9] --------> [2n/3, n]


class MultiStack:
    def __init__(self, stack_size):
        self.number_of_stack = 3
        # take the number of stack multiply with number of stack size
        self.custList = [0] * (stack_size * self.number_of_stack)
        self.sizes = [0] * self.number_of_stack
        self.stack_size = stack_size
        
    def isFull(self, stack_num):
        return self.sizes[stack_num] == self.stack_size

    def isEmpty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def indexOfTop(self, stack_num):
        offset = stack_num * self.stack_size
        return offset * self.sizes[stack_num] - 1
    
    def push(self, item, stack_num):
        if self.isFull(stack_num):
            return "the stack is full"
        self.sizes[stack_num] += 1
        self.custList[self.indexOfTop(stack_num)] = item
    
    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            return "the stack is empty"
        value = self.custList[self.indexOfTop(stack_num)]
        self.custList[self.indexOfTop(stack_num)] = 0
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.isEmpty(stack_num):
            return "the stack is empty"
        return self.custList[self.indexOfTop(stack_num)]
    

custome_stack = MultiStack(6)
print(custome_stack.isFull(0))
print(custome_stack.isEmpty(1))
custome_stack.push(10, 0)
custome_stack.push(11, 0)
custome_stack.push(12, 1)
custome_stack.push(13, 1)
custome_stack.push(14, 2)
custome_stack.pop(1)
print(custome_stack.peek(1))
class KthLargestNumber:
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k
        
    def add(self, num):
        self.nums.append(num)
        return sorted(self.nums)[-self.k] 
    
def main():
    kth = KthLargestNumber([3, 1, 5, 12, 2, 11], 4)
    print(f"4th largest number is: {str(kth.add(6))}")
    print(f"4th largest number is: {str(kth.add(13))}")
    print(f"4th largest number is: {str(kth.add(4))}")

main()


from heapq import heappop, heappush

class KLarge(object):
    minHeap = []
    def __init__(self, nums, k):
        self.nums = nums
        self.k = k 
        for num in self.nums:
            self.add(num)
            
        
    def add(self, num):
        heappush(self.minHeap, num)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
    
def new_main():
    my_k = KLarge([3, 1, 5, 12, 2, 11], 4)
    print(my_k.add(6))
    print(my_k.add(13))
    print(my_k.add(4))
    

new_main()
            


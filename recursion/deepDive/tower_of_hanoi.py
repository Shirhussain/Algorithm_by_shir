def hanoi(N):

    def move(num, start, finish, temp):
        if num == 1:
            print("move", start, "to", finish)
        else:
            move(num-1, start, temp, finish)
            move(1, start, finish, temp)
            move(num-1, temp, finish, start)

    move(N, 'A', 'C', 'B')


hanoi(4)

'''
def permutations(nums):

  result = []
  def helper(partial_result, nums):

    if len(nums) == 0:
      result.append(partial_result)
      return
    
    for num in nums:
      # make a copy of nums that excludes num
      copy = []
      for number in nums:
        if number != num:
          copy.append(number)
      helper(partial_result + [num], copy)
  
  helper([], nums)
  return result

print(len(permutations([1,2,3,4,5,6])))

'''

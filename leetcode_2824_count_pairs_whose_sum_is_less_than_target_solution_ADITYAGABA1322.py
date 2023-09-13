# SOLUTION from user ADITYAGABA1322 on leetcode.com

def countPairs(nums: list[int], target: int) -> int:
    nums.sort() # sort the vector nums
    count = 0 # variable to store the count
    left = 0 # variable to store the left
    right = len(nums)-1 # variable to store the right
    while(left < right): # loop until left is less than right
        if(nums[left] + nums[right] < target): # if nums[left] + nums[right] is less than target
            count += right-left # update the count
            left += 1 # increment the left
        else: # else
            right -= 1 # decrement the right
    return count # return the count

print(countPairs([-1,1,2,3,1], 2)) # => 3
print(countPairs([-6,2,5,-2,-7,-1,3], -2)) # => 10
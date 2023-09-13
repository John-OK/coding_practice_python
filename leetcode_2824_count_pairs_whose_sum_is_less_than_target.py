def countPairs(nums: list[int], target: int) -> int:
    numberOfPairs = 0

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] < target:
                numberOfPairs += 1
    
    return numberOfPairs

print(countPairs([-1,1,2,3,1], 2)) # => 3
print(countPairs([-6,2,5,-2,-7,-1,3], -2)) # => 10
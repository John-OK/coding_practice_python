def numIdenticalPairs(nums: list[int]) -> int:
    goodPairs = 0
    numElements = len(nums)

    for i in range(numElements - 1):
        for j in range(i + 1, numElements):
            if nums[i] == nums[j]:
                goodPairs += 1

    return goodPairs

print(numIdenticalPairs([1,2,3,1,1,3])) # => 4
print(numIdenticalPairs([1,1,1,1])) # => 6
print(numIdenticalPairs([1,2,3])) # => 0
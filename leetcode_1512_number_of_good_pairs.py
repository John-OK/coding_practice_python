def numIdenticalPairs(nums: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n**2), 46 ms, beats 26.93%
    # goodPairs = 0
    # numElements = len(nums)
    #
    # for i in range(numElements - 1):
    #     for j in range(i + 1, numElements):
    #         if nums[i] == nums[j]:
    #             goodPairs += 1
    #
    # return goodPairs

    
    # SECOND ATTEMPT: time complexity: O(n), 33 ms, beats 94.23%
    # goodPairs = 0
    # count = {}
    #
    # for num in nums:
    #     if num in count:
    #         count[num] += 1
    #     else:
    #         count[num] = 0
    #
    # for value in count.values():
    #     if value > 0:
    #         goodPairs += (value**2 + value) / 2
    #
    # return int(goodPairs)


    # THIRD ATTEMPT: time complexity: O(n), 35 ms, beats 87.90%; uses hashmap but algo updates answer while iterating through array, not by iterating through hashmap
    goodPairs = 0
    count = {}

    for num in nums:
        if num in count:
            goodPairs += count[num]
            count[num] += 1
        else:
            count[num] = 1

    return goodPairs


print(numIdenticalPairs([1,2,3,1,1,3])) # => 4
print(numIdenticalPairs([1,1,1,1])) # => 6
print(numIdenticalPairs([1,2,3])) # => 0
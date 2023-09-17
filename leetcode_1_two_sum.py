def twoSum(nums: list[int], target: int) -> list[int]:
    # FIRST TRY: nested loop => O(n**2)
    # for i, num in enumerate(nums):

    #     if i == len(nums) - 1:
    #         return []

    #     for j in range(i+1, len(nums)):
    #         if num + nums[j] == target:
    #             return [i, j]

    hashmap = {}

    for i in range(len(nums)):
        num = nums[i]
        difference = target - num
        if difference in hashmap:
            return [hashmap[difference], i]
        else:
            hashmap[num] = i

print(twoSum([2,7,11,15], 9)) # => [0, 1]
print(twoSum([3,2,4], 6)) # => [1, 2]
print(twoSum([3,3], 6)) # => [0, 1]
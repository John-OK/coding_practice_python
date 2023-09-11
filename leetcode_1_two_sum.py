# TODO: solve without nested loop

def twoSum(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):

        if i == len(nums) - 1:
            return []

        for j in range(i+1, len(nums)):
            if num + nums[j] == target:
                return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))
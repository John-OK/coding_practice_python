def removeDuplicates(nums: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n log n) due to .sort(), 72 ms, beats 98.01%
    left = 0
    right = 1
    k = 1

    while right < len(nums) and left < len(nums):
        if nums[left] != nums[right]:
            left = right
            right = left + 1
            k += 1
        elif nums[left] == nums[right]:
            nums[right] = 999
            right += 1

    nums.sort()

    return k

print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
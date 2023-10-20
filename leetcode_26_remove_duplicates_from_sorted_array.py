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


# Solution from kshatriyas on leetcode that uses one of the pointers to keep
# track of the number of unique elements by replacing non-unique elements with
# unique ones. In the end, all unique elements are next to each other and j has
# the value of the number of unique elements.

    # j = 1
    # for i in range(1, len(nums)):
    #     if nums[i] != nums[i - 1]:
    #         nums[j] = nums[i]
    #         j += 1
    # return j

print(removeDuplicates([1, 1, 2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
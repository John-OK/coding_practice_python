def sortColors(nums: list[int]) -> None:
    # FIRST ATTEMPT: time complexity: O(n**2), 45 ms, beats 44.10%
    left = 0
    right = 1
    have_switched = True

    while have_switched:
        have_switched = False
        left = 0
        right = 1
        while right < len(nums):
            if nums[left] > nums[right]:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1
                have_switched = True
            else:
                left += 1
                right += 1

print(sortColors([2,0,2,1,1,0])) # => [0, 0, 1, 1, 2, 2]
print(sortColors([2,0,1])) # => [0, 1, 2]

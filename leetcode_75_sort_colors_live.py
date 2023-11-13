def sortColors(nums: list[int]) -> None:
    # FIRST ATTEMPT: time complexity: O(n**2), 45 ms, beats 44.10%
    # left = 0
    # right = 1
    # have_switched = True

    # while have_switched:
    #     have_switched = False
    #     left = 0
    #     right = 1
    #     while right < len(nums):
    #         if nums[left] > nums[right]:
    #             nums[right], nums[left] = nums[left], nums[right]
    #             left += 1
    #             right += 1
    #             have_switched = True
    #         else:
    #             left += 1
    #             right += 1
    # return nums



    # SECOND ATTEMPT (hashmap): time complexity: O(n), 31 ms, beats 97.19%
    # from collections import defaultdict
    # freq_map = defaultdict(list)

    # for num in nums:
    #     freq_map[num].append(num)

    # i = 0
    # for num in range(3):
    #     freq = freq_map[num]
    #     nums[i:i + len(freq)] = freq_map[num]
    #     i += len(freq)

    # return nums


    # THIRD ATTEMPT (partitioning): time complexity: O(n), 38 ms, beats 76.99%
    low = 0
    high = len(nums) - 1
    current = 0

    while current <= high:
        if nums[current] == 0:
            nums[low], nums[current] = nums[current], nums[low]
            low += 1
            current += 1
        elif nums[current] == 2:
            nums[high], nums[current] = nums[current], nums[high]
            high -= 1
            current -= 1
        current += 1

    return nums

print(sortColors([2,0,2,1,1,0])) # => [0, 0, 1, 1, 2, 2]
print(sortColors([2,0,1])) # => [0, 1, 2]
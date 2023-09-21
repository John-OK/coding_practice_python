def majorityElement(nums: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n), 160 ms, beats 30.15%
    # n = len(nums)
    # num_frequency = {}
    #
    # for num in nums:
    #     if num in num_frequency:
    #         num_frequency[num] += 1
    #     else:
    #         num_frequency[num] = 1
    #
    # return [key for key, value in num_frequency.items() if value > n/2][0]


    # SECOND ATTEMPT: slightly better time; time complexity: O(n), 154 ms, beats 50.19%
    # num_frequency = {}
    #
    # for num in nums:
    #     if num not in num_frequency:
    #         num_frequency[num] = nums.count(num)
    #
    # return max(num_frequency, key=num_frequency.get)


    # THIRD ATTEMPT: time complexity: O(n log n), 137 ms, beats 97.87%, but seems gimmicky and very specific to this exact situation (i.e., not applicable to general, real-world coding problems)
    # nums.sort()
    #
    # return nums[int(len(nums)/2)]


    # FOURTH ATTEMPT: using Boyer-Moore's Voting Algorithm: time complexity: O(n), 153 ms, beats 53.28% Not the best time complexity, but good to know this algo
    current_majority = 0
    count = 0

    for num in nums:
        if count == 0:
            current_majority = num
        count += (1 if num == current_majority else -1)

    return current_majority

print(majorityElement([3,2,3])) # => 3
print(majorityElement([2,2,1,1,1,2,2])) # => 2
print(majorityElement([3,3,4])) # => 3
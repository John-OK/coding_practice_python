def majorityElement(nums: list[int]) -> int:
    n = len(nums)
    num_frequency = {}

    for num in nums:
        if num in num_frequency:
            num_frequency[num] += 1
        else:
            num_frequency[num] = 1

    return [key for key, value in num_frequency.items() if value > n/2][0]

print(majorityElement([3,2,3])) # => 3
print(majorityElement([2,2,1,1,1,2,2])) # => 2
print(majorityElement([3,3,4])) # => 3
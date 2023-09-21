def runningSum(nums: list[int]) -> list[int]:
    # FIRST ATTEMPT: time complexity: O(n)
    # sum_list: list[int] = []
    # for index, num in enumerate(nums):
    #     if sum_list:
    #         sum_list.append(num + sum_list[index-1])
    #     else:
    #         sum_list.append(num)
    # return sum_list


    # SECOND ATTEMPT: time complexity: O(n), basically the same algorithm but modifies the original list to save space. Avoid when possible as modifying the inputs can have unexpected side effects.
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

print(runningSum([1, 2, 3, 4])) # => [1,3,6,10]
print(runningSum([1,1,1,1,1])) # => [1,2,3,4,5]
print(runningSum([3,1,2,10,1])) # => [3,4,6,16,17]
from collections import defaultdict

def maxSum(nums: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n**2) because max() is O(n), 101 ms, beats 97.65%
    max_digit_nums = defaultdict(list)
    max_sum = -1

    for num in nums:
        max_digit = int(max(str(num)))
        max_digit_nums[max_digit].append(num)
        
    for k, v in max_digit_nums.items():
        if len(v) > 1:
            max_index = v.index(max(v))
            temp_sum = v.pop(max_index)
            temp_sum += max(v)
            
            if temp_sum > max_sum:
                max_sum = temp_sum

    return max_sum


    # SECOND ATTEMPT: time complexity: O(n**2) because max() is O(n), 112 ms, beats 81.44%
    # max_digit_nums = defaultdict(list)
    # max_sum = -1

    # for num in nums:
    #     max_digit = int(max([*str(num)]))
    #     max_digit_nums[max_digit].append(num)
        
    # for k, v in max_digit_nums.items():
    #     if len(v) > 1:
    #         v.sort(reverse=True)
    #         temp_sum = sum(v[:2])
            
    #         if temp_sum > max_sum:
    #             max_sum = temp_sum

    # return max_sum

print(maxSum([51,71,17,24,42])) # => 88
print(maxSum([1,2,3,4])) # => -1
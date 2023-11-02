from collections import defaultdict

def maxSum(nums: list[int]) -> int:
    max_digit_nums = defaultdict(list)
    max_sum = -1

    for num in nums:
        max_digit = int(max([*str(num)]))
        max_digit_nums[max_digit].append(num)
        
    for k, v in max_digit_nums.items():
        if len(v) > 1:
            max_index = v.index(max(v))
            sum = v.pop(max_index)
            sum += max(v)
            
            if sum > max_sum:
                max_sum = sum


    return max_sum

print(maxSum([51,71,17,24,42])) # => 88
print(maxSum([1,2,3,4])) # => -1
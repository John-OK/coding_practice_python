# SOLUTION from user Kyrylo-Ktl on leetcode.com

def countPairs(nums: list[int], target: int) -> int:
    return sum(
        nums[i] + nums[j] < target
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
    )

print(countPairs([-1,1,2,3,1], 2)) # => 3
print(countPairs([-6,2,5,-2,-7,-1,3], -2)) # => 10
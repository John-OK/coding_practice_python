def maxArea(height: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n), 564 ms, beats 92.13%
    left = 0
    right = len(height) - 1
    maxWater = min(height[left], height[right]) * (right - left)

    while left < right:        
        if height[left] <= height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1

        waterAmount = min(height[left], height[right]) * (right - left)
        if waterAmount > maxWater:
            maxWater = waterAmount

    return maxWater

print(maxArea([1,8,6,2,5,4,8,3,7])) # => 49
print(maxArea([1,1])) # => 1
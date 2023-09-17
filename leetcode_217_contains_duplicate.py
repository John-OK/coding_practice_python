"""
loop through each element except last element
    nest loop through each element beginning at index 1 to see if matches first element
"""

# def containsDuplicate(nums: list[int]) -> bool:
#     for i in range(len(nums) - 1):
#         for j in range (i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 return True

#     return False

def containsDuplicate(nums: list[int]) -> bool:
    hashmap = {}

    for num in nums:
        if num in hashmap:
            return True
        else:
            hashmap[num] = True

    return False

print(containsDuplicate([1,2,3,1])) # => True
print(containsDuplicate([1,2,3,4])) # => False
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # => True
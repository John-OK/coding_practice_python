"""
pseudo code:
- loop through list and create dict with int as key and index as value
    - if list's int exists in dict and 
    (list's int index) - (key's value) <= to k, then return true,
        else, replace key's value with new index
        (because the difference of any newer index - old index will be larger,
        so it can be discarded)
"""

# FIRST ATTEMPT: time complexity: O(n), 492 ms, beats 99.17%
def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    duplicate_indices = {}

    for i, num in enumerate(nums):
        if num in duplicate_indices and i - duplicate_indices[num] <= k:
            return True
        else:
            duplicate_indices[num] = i

    return False

print(containsNearbyDuplicate([1,2,3,1], 3)) # True
print(containsNearbyDuplicate([1,0,1,1], 1)) # True
print(containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
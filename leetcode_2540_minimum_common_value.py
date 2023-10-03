def getCommon(nums1: list[int], nums2: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n), 378 ms, beats 93.13%
    num1_elements = {}

    for num in nums1:
        if num not in num1_elements:
            num1_elements[num] = 1

    for num in nums2:
        if num in num1_elements:
            return num

    return -1

print(getCommon([1,2,3], [2,4]))
print(getCommon([1,2,3,6], [2,3,4,5]))
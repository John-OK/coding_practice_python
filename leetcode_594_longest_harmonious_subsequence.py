def findLHS(nums: list[int]) -> int:
    # FIRST ATTEMPT: time complexity: O(n**2), TIME EXCEEDED
    # answer = 0

    # for left in range(len(nums) - 1):
    #     answer_greater = 0
    #     answer_lesser = 0
    #     right = left + 1
    #     has_harmony = False

    #     while right < len(nums):
    #         if nums[right] - nums[left] == 1:
    #             answer_greater += 1
    #             has_harmony = True
    #         elif nums[right] - nums[left] == -1:
    #             answer_lesser += 1
    #             has_harmony = True
    #         elif nums[right] == nums[left]:
    #             answer_greater += 1
    #             answer_lesser += 1
    #         right += 1

    #     if has_harmony:
    #         answer = max(answer, answer_greater, answer_lesser)

    # if answer > 0:
    #     answer += 1
    # return answer


    # SECOND ATTEMPT: time complexity: O(), ms, beats %
    from collections import Counter
    freq_table = Counter(nums)
    longest_subsequence = 0

    for num, freq in freq_table.items():
        if num - 1 in freq_table:
            longest_subsequence = max(longest_subsequence, freq + freq_table[num - 1])

    return longest_subsequence


print(findLHS([1,3,2,2,5,2,3,7])) # => 5
print(findLHS([1,2,3,4])) # => 2
print(findLHS([1,1,1,1])) # => 0
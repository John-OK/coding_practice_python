def topKFrequent(nums: list[int], k: int) -> list[int]:
    from collections import Counter

    # FIRST ATTEMPT: time complexity: O(n), 83 ms, beats 86.22%
    most_freq_nums = []
    num_freqs = Counter(nums)
    freqs = [[] for i in range(len(nums) + 1)] # array indexed by possible frequencies (index 0 will never be used)

    # put numbers into freq-indexed array, "freqs"
    # e.g., [1, 1, 1, 2, 2, 3] => [[], [3], [2], [1], [], [], []]
    for num, count in num_freqs.items():
        freqs[count].append(num)

    # populate "most_freq_nums" array starting with the most frequent nums
    # (i.e., largest index) until it has "k" nums

    # for i in range(len(freqs) - 1, 0, -1):
    #     for num in freqs[i]:
    #         most_freq_nums.append(num)
    #         if len(most_freq_nums) == k:
    #             return most_freq_nums
    i = len(freqs) - 1
    while len(most_freq_nums) < k:
        for num in freqs[i]:
            most_freq_nums.append(num)
        i -= 1

    return most_freq_nums


print(topKFrequent([1,1,1,2,2,3], 2)) # => [1,2]
print(topKFrequent([1], 1)) # => [1]
print(topKFrequent([1, 2], 2)) # => [1, 2]
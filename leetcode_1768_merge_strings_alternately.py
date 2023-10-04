def mergeAlternately(word1: str, word2: str) -> str:
    # FIRST ATTEMPT: time complexity: O(n), 31 ms, beats 92.32%
    pointer_1 = 0
    pointer_2 = 0
    merged_string = ""

    while pointer_1 < len(word1) or pointer_2 < len(word2):
        if pointer_1 < len(word1):
            merged_string += word1[pointer_1]
            pointer_1 += 1

        if pointer_2 < len(word2):
            merged_string += word2[pointer_2]
            pointer_2 += 1

    return merged_string

print(mergeAlternately("abc", "pqr")) # => apbqcr
print(mergeAlternately("ab", "pqrs")) # => apbqrs
print(mergeAlternately("abcd", "pq")) # => apbqcd
def findRepeatedDnaSequences(s: str) -> list[str]:

    # FIRST ATTEMPT: time complexity: O(n), 49 ms, beats 92.99%
    sequence_table = {}
    repeat_table = {}

    # for i in range(len(s) - 9):
    #     sequence = s[i:i + 10]
    #     if sequence in sequence_table:
    #         sequence_table[sequence] += 1
    #         repeat_table[sequence] = 1
    #     else:
    #         sequence_table[sequence] = 1

    # return list(repeat_table)

    # REFACTOR TO SIMPLIFY
    for i in range(len(s) - 9):
        sequence = s[i:i + 10]
        if sequence in sequence_table:
            repeat_table[sequence] = 1
        sequence_table[sequence] = 1

    return list(repeat_table)

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # => ["AAAAACCCCC","CCCCCAAAAA"]
print(findRepeatedDnaSequences("AAAAAAAAAAAAA")) # => ["AAAAAAAAAA"]

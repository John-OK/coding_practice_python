def findRepeatedDnaSequences(s: str) -> list[str]:
    sequence_table = {}
    repeat_table = {}

    for i in range(len(s) - 9):
        sequence = s[i:i + 10]
        if sequence in sequence_table:
            sequence_table[sequence] += 1
            repeat_table[sequence] = 1
        else:
            sequence_table[sequence] = 1

    return list(repeat_table)

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) # => ["AAAAACCCCC","CCCCCAAAAA"]
print(findRepeatedDnaSequences("AAAAAAAAAAAAA")) # => ["AAAAAAAAAA"]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    PSEUDO CODE:
    -create a hashtable to store each string
    -loop through list
        -for each string,
            -save the string as a sorted list in the hashtable
            with the value being the string
    -return anagram group list with hashtable values
    """

    # FIRST ATTEMPT: time complexity: O(n log n) due to sorted(), 93 ms, beats 82.93%
    hashTable = {}

    for word in strs:
        word_chars = "".join(sorted(word))
        if word_chars not in hashTable:
            hashTable[word_chars] = [word]
        else:
            hashTable[word_chars].append(word)

    return [v for k, v in hashTable.items()]

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # => [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""])) # => [[""]]
print(groupAnagrams(["a"])) # => [["a"]]
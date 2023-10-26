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


    #SECOND ATTEMPT: time complexity: O(n * m) where m = number of input strings, and n = avg length of those strings; strings, 101 ms, beats 52.89%
    # from collections import defaultdict

    # char_freqs = defaultdict(list) # defaultdict handles cases where key:value does not yet exist in dict 

    # for word in strs: # "m" in time complexity
    #     count = [0] * 26 # list of count of chars a to z (all initially set to 0)

    #     for char in word: "n" in time complexity
    #         count[ord(char) - ord("a")] += 1 # ord() gets the ASCII value of char; subtract by ord("a") to get index of char ("a" - "a" = 0; "b" - "a" = 1; ...; "z" - "a" = 25)

    #     char_freqs[tuple(count)].append(word) # tuple becuase keys must be immutable

    # return char_freqs.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # => [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""])) # => [[""]]
print(groupAnagrams(["a"])) # => [["a"]]
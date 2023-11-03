from collections import defaultdict

def reverseVowels(s: str) -> str:

    # FIRST ATTEMPT: time complexity: O(n), 45 ms, beats 94.40%
    # vowel_indices_map = defaultdict(str)
    # vowels = "aeiouAEIOU"
    # answer = []

    # for i, char in enumerate(s):
    #     if char.lower() in vowels:
    #         vowel_indices_map[i] = char

    # vowel_indices_list = list(vowel_indices_map.keys())
    # vowel_list = list(vowel_indices_map.values())
    # reversed_vowel_list = vowel_list[::-1]

    # for i, char in enumerate(reversed_vowel_list):
    #     vowel_indices_map[vowel_indices_list[i]] = char

    # for i, char in enumerate(s):
    #     if char in vowels:
    #         answer.append(vowel_indices_map[i])
    #     else:
    #         answer.append(char) 

    # return answer


    # SECOND ATTEMPT (simplified code, but worse time complexity): time complexity: O(n), 204 ms, beats 5.01%
    vowels = "aeiouAEIOU"
    vowel_indices = []
    vowel_chars_reversed = []
    reversed_vowels = list(s)
    
    for i, char in enumerate(s):
        if char in vowels:
            vowel_indices.append(i)
            vowel_chars_reversed.insert(0, char)

    for i, vowel_index in enumerate(vowel_indices):
        reversed_vowels[vowel_index] = vowel_chars_reversed[i]

    return "".join(reversed_vowels)
    
    

# THIRD ATTEMPT (using 2 pointers): time complexity: O(n), 45 ms, beats 94.40%



print(reverseVowels("hello")) # => "holle"
print(reverseVowels("leetcode")) # => "leotcede"
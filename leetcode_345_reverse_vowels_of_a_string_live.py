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
    # vowels = "aeiouAEIOU"
    # vowel_indices = []
    # vowel_chars_reversed = []
    # reversed_vowels = list(s)
    
    # for i, char in enumerate(s):
    #     if char in vowels:
    #         vowel_indices.append(i)
    #         vowel_chars_reversed.insert(0, char)

    # for i, vowel_index in enumerate(vowel_indices):
    #     reversed_vowels[vowel_index] = vowel_chars_reversed[i]

    # return "".join(reversed_vowels)
    
    

    # THIRD ATTEMPT (using 2 pointers): time complexity: O(n), 42 ms, beats 97.49%
    vowels = "aeiouAEIOU"
    s_list = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        if s_list[left] not in vowels:
            left += 1
        else:
            if s_list[right] not in vowels:
                right -= 1
            else:
                right_char = s_list[right]
                s_list[right] = s_list[left]
                s_list[left] = right_char
                
                left += 1
                right -= 1
    
    return "".join(s_list)

print(reverseVowels("hello")) # => "holle"
print(reverseVowels("leetcode")) # => "leotcede"
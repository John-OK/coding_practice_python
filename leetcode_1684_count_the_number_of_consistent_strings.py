def countConsistentStrings(allowed: str, words: list[str]) -> int:
    # FIRST ATTEMPT: time complexity: O(n**2), 221 ms, beats 87.04%
    number_of_consistent_strings = 0
    allowed_chars = {char: True for char in allowed}

    for word in words:
        valid = True
        if valid == False:
            continue
        for char in word:
            if char not in allowed_chars:
                valid = False
                break
        if valid == True:
            number_of_consistent_strings += 1
    
    return number_of_consistent_strings


    # SECOND ATTEMPT using dictionary comprehension: time complexity: O(n**2)?, 283 ms, beats 29.18%
    # I heard that dictionary & list comprehensions were faster than for loops, but it seems that they are just faster to write.
    # number_of_consistent_strings = 0
    # allowed_chars = {x: True for x in allowed}

    # for word in words:
    #     current_characters = {char: 1 if char in allowed_chars else 0 for char in word}
    #     has_invalid_char = 0 in current_characters.values()
    #     if has_invalid_char == False:
    #         number_of_consistent_strings += 1
    
    # return number_of_consistent_strings

print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
print(countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
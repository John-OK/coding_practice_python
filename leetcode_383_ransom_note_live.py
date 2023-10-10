# LIVE INTERVIEW PRACTICE WITH DAN. 2023-10-09

def canConstruct(ransomNote: str, magazine: str) -> bool:

    # FIRST ATTEMPT: time complexity: O(n), 67 ms, beats 44.78%
    # magazine_chars = {}

    # for char in magazine:
    #     if char in magazine_chars:
    #         magazine_chars[char] += 1
    #     else:
    #         magazine_chars[char] = 1

    # for char in ransomNote:
    #     if char not in magazine_chars:
    #         return False
    #     if char in magazine_chars:
    #         if magazine_chars[char] == 0:
    #             return False
    #         else:
    #             magazine_chars[char] -= 1

    # return True


    # SECOND ATTEMPT WITH "Counter()": time complexity: O(n), 53 ms, beats 78.76%
    # Note: Counter() is optimized construction of the frequency count using the for loop in attempt 1, so it is faster.
    # Its use an optimized C function, is what makes it faster. Otherwise, the logic is pretty much the same between the two attempts.
        from collections import Counter
        magazine_chars = Counter(magazine)
        note_chars = Counter(ransomNote)

        for char in note_chars:
            if char not in magazine_chars or note_chars[char] > magazine_chars[char]:
                return False

        return True
    

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
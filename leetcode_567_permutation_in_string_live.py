def checkInclusion(s1: str, s2: str) -> bool:
    from collections import Counter

    length = len(s1)
    letter_freq = Counter(s1)

    for i, char in enumerate(s2):
        if char in letter_freq:
            substring = s2[i:i + length]
            substring_freq = Counter(substring)
            same_freq = False

            if substring_freq == letter_freq:
                return True

    return False

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))
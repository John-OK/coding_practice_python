# LIVE INTERVIEW PRACTICE WITH DAN

def canConstruct(ransomNote: str, magazine: str) -> bool:
    note_chars = {}

    for char in magazine:
        if char in note_chars:
            note_chars[char] += 1
        else:
            note_chars[char] = 1

    for char in ransomNote:
        if char not in note_chars:
            return False
        if char in note_chars:
            if note_chars[char] == 0:
                return False
            else:
                note_chars[char] -= 1

    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
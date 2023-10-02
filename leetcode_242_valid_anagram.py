def isAnagram(s: str, t: str) -> bool:
    # FIRST ATTEMPT: time complexity: O(n)
    letter_count = {}

    if len(s) != len(t):
        return False

    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for letter in letter_count:
        if t.count(letter) != letter_count[letter]:
            return False

    return True

print(isAnagram('anagram', 'nagaram'))
print(isAnagram('rat', 'car'))
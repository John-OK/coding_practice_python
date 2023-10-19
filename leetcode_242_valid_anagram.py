from collections import Counter
def isAnagram(s: str, t: str) -> bool:
    # FIRST ATTEMPT: time complexity: O(n), 51 ms, beats 72.75%
    # Could do in one line: return Counter(s) == Counter(t)
    count_s, count_t = Counter(s), Counter(t)

    if len(s) != len(t):
        return False

    for letter in count_s:
        if count_s[letter] != count_t[letter]:
            return False

    return True

print(isAnagram('anagram', 'nagaram')) # => True
print(isAnagram('rat', 'car')) # => False
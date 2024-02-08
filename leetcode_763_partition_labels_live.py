 
def partitionLabels(s: str) -> list[int]:
    left, inner, right = 0, 0, 0
    char_index = {}
    parts = []

    for i in range(len(s)):
        char = s[i]
        if char in char_index:
            char_index[char] = i
        else:
            char_index[char] = i

    while right < len(s):
        right = char_index[s[left]]
        inner = left + 1

        while right > inner:
            if char_index[s[inner]] > right:
                right = char_index[s[inner]]
            inner += 1

        parts.append(right - left + 1)
        right += 1
        left = right    

    return parts

print(partitionLabels("ababcbacadefegdehijhklij")) # => [9,7,8]
print(partitionLabels("eccbbbbdec")) # => [10]
print(partitionLabels("qiejxqfnqceocmy")) # => [13,1,1]

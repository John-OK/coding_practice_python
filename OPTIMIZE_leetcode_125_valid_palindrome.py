def isPalindrome(s: str) -> bool:
    """
    PSEUDO CODE:
    - lowercase and remove non-alphanumerics
    - pointers to left and right ends of string
    - check if pointer values equal: if not, return False; if so, move pointers towards each other
        - repeat until pointer indices equal or cross
    - return True
    """
    # FIRST ATTEMPT: time complexity: O(n), 60 ms, beats 19.02%
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        if not s[left].isalnum():
            left += 1

        if not s[right].isalnum():
            right -= 1
    
    return True



print(isPalindrome("A man, a plan, a canal: Panama")) # => True
print(isPalindrome("race a car")) # => False
print(isPalindrome(" ")) # => True
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
    # left = 0
    # right = len(s) - 1

    # while left < right:
    #     if s[left].isalnum() and s[right].isalnum():
    #         if s[left].lower() != s[right].lower():
    #             return False
    #         else:
    #             left += 1
    #             right -= 1

    #     if not s[left].isalnum():
    #         left += 1

    #     if not s[right].isalnum():
    #         right -= 1
    
    # return True


    # SECOND ATTEMPT: time complexity: O(n), 44 ms, beats 84.14%
    # Only slightly better than first attempt.
    # NOTE: although there are nested loops, time complexity is still O(n)
    # because the inner loops are not looping through the whole string again,
    # but helping to progress the pointers towards the center
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while right > left and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1
    
    return True



print(isPalindrome("A man, a plan, a canal: Panama")) # => True
print(isPalindrome("race a car")) # => False
print(isPalindrome(" ")) # => True
print(isPalindrome("a")) # => True
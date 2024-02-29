def dividePlayers(skill: list[int]) -> int:

    # FIRST ATTEMPT: time complexity: O(n log n) for sorting, 386 ms, beats 94.262%
    # if len(skill) % 2 != 0:
    #     return -1

    # skill.sort()
    # left = 0
    # right = len(skill) - 1
    # teams_are_equal = True
    # outter_team_level = skill[0] + skill[-1]
    # products_sum = 0

    # while left < right and teams_are_equal == True:
    #     teams_are_equal = False        
    #     team_level = skill[left] + skill[right]
        
    #     if team_level == outter_team_level:
    #         teams_are_equal = True
    #         products_sum += skill[left] * skill[right]
    #     else:
    #         return -1

    #     left += 1
    #     right -= 1

    # return products_sum

    # SECOND ATTEMPT: time complexity: O(n) (but getting worse times on leetcode), 409 ms, beats 48.33%
    
    # Odd number of players means one team will not be of size 2
    if len(skill) % 2 != 0:
        return -1

    from collections import defaultdict

    num_players = len(skill)
    avg_team_skill = sum(skill)/(num_players/2)
    skill_freq = defaultdict(int)
    twice_sum_products = 0

    for level in skill:
        skill_freq[level] += 1

    for level in skill:
        teammate_level = avg_team_skill - level
        if skill_freq[level] != skill_freq[teammate_level]:
            return -1

        twice_sum_products += level * teammate_level
    
    return int(twice_sum_products / 2)


print(dividePlayers([3,2,5,1,3,4])) # 22
print(dividePlayers([3,4])) # 12
print(dividePlayers([1,1,2,3])) # -1
print(dividePlayers([2,1,5,2])) # -1
print(dividePlayers([1,1,1,2,3,3,3,7,7,8,8,8,9,9])) # -1
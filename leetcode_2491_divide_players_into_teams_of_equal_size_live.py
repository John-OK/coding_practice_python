def dividePlayers(skill: list[int]) -> int:

    # FIRST ATTEMPT: time complexity: O(n*log(n)) for sorting, 396 ms, beats 80.82%
    if len(skill) % 2 != 0:
        return -1

    skill.sort()
    left = 0
    right = len(skill) - 1
    teams_are_equal = True
    outter_team_level = skill[0] + skill[-1]
    products_sum = 0

    while left < right and teams_are_equal == True:
        teams_are_equal = False        
        team_level = skill[left] + skill[right]
        
        if team_level == outter_team_level:
            teams_are_equal = True
            products_sum += skill[left] * skill[right]
        else:
            return -1

        left += 1
        right -= 1

    return products_sum


print(dividePlayers([3,2,5,1,3,4])) # 22
print(dividePlayers([3,4])) # 12
print(dividePlayers([1,1,2,3])) # -1
print(dividePlayers([2,1,5,2])) # -1
print(dividePlayers([1,1,1,2,3,3,3,7,7,8,8,8,9,9])) # -1
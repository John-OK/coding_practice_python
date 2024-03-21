def numFriendRequests(ages: list[int]) -> int:
    from collections import Counter

    age_freq = Counter(ages)
    num_requests = 0

    for focus_age, focus_count in age_freq.items():
        for eval_age, eval_count in age_freq.items():
            if eval_age > 0.5 * focus_age + 7 and focus_age >= eval_age:
                num_requests += eval_count * focus_count
                if eval_age == focus_age:
                    num_requests -= focus_count
            
    return num_requests

print(numFriendRequests([16,16])) # => 2
print(numFriendRequests([16,17,18])) # => 2
print(numFriendRequests([20,30,100,110,120])) # => 3
print(numFriendRequests([101,56,69,48,30])) # => 4
print(numFriendRequests([8,85,24,85,69])) # => 4
print(numFriendRequests([98,60,24,89,84,51,61,96,108,87,68,29,14,11,13,50,13,104,57,8,57,111,92,87,9,59,65,116,56,39,55,11,21,105,57,36,48,93,20,94,35,68,64,41,37,11,50,47,8,9]))
    # => 439

def groupThePeople(groupSizes: list[int]) -> list[list[int]]:

    # FIRST ATTEMPT: time complexity: O(n), 65 ms, beats 73.11%
    size_indices = {}
    answer = []

    for i, size in enumerate(groupSizes):
        if size not in size_indices:
            size_indices[size] = [i]
        else:
            size_indices[size].append(i)

    for group_size, indices in size_indices.items():
        group = []

        for i in indices:
            group.append(i)

            if len(group) == group_size:
                answer.append(group)
                group = []

    return answer

print(groupThePeople([3,3,3,3,3,1,3])) # => [[0, 1, 2], [3, 4, 6], [5]]
print(groupThePeople([2,1,3,3,3,2])) # => [[0, 5], [1], [2, 3, 4]]
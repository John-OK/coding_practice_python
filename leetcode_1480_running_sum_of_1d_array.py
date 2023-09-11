def runningSum(nums: list[int]) -> list[int]:
    sum_list: list[int] = []
    for index, num in enumerate(nums):
        if sum_list:
            sum_list.append(num + sum_list[index-1])
        else:
            sum_list.append(num)
    return sum_list

print(runningSum([1, 2, 3, 4]))
def addUp(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total

print(addUp(4)) # => 10
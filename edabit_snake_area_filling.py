def snakefill(n):
    number_squares = n ** 2
    times_can_eat = 0
    i = 1
    while i <= number_squares:
        times_can_eat += 1
        i *= 2
    return times_can_eat - 1

print(snakefill(3)) # >> 3
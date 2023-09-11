def series_resistance(lst):
    total_resistance = sum(lst)
    ohm = 'ohm'
    if (total_resistance > 1):
        ohm = "ohms"
    return f'{total_resistance} {ohm}'

print(series_resistance([1,2,3.5]))
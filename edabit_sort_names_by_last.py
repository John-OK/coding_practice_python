def last_name_lensort(names):
    last_name_lengths = {}
    sorted_names = []

    for name in names:
        length_of_last_name = len(name.split(" ")[1])
        if length_of_last_name in last_name_lengths:
            last_name_lengths[length_of_last_name].append(name)
        else :
            last_name_lengths[length_of_last_name] = [name]
        

    sorted_lengths = sorted(last_name_lengths)

    for length in sorted_lengths:
        name_list = last_name_lengths[length]
        sorted_names += sorted(name_list, key=lambda name: name.split(" ")[1])    

    return sorted_names

        
print(last_name_lensort(["Jennifer Figueroa","Heather Mcgee","Amanda Schwartz","Nicole Yoder","Melissa Hoffman"]))
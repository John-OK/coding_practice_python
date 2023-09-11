def track_robot(steps):
    position = [0, 0] # [east, north] moving east and north increase values, while west and south decrease values
    order_of_heading_values = [[1, 0], [0, -1], [-1, 0], [0, 1]] # represent values that will be added to position if moving east, south, west, north
    heading_values_index = 0 # since east is the beginning direction, index starts at 0 and will increment with '>' and decrement with '<'

    for step in steps:
        if (step == '>'):
            heading_values_index = (heading_values_index + 1) % 4 # increment the index; % will cause it to loop back to index 0 after index 3
        elif (step == '<'):
            heading_values_index = (heading_values_index - 1) % 4 # decrement the index; % will cause it to loop back to index 3 after index 0
        else:
            values_to_add = order_of_heading_values[heading_values_index]
            position[0] += values_to_add[0]
            position[1] += values_to_add[1]
    
    return position

print(track_robot("..<.<.")) # >> [ 1, 1 ]
print(track_robot("<>>>><><<<><>>>><><<<><>>><>")) # >> [ 0, 0 ]
print(track_robot(".<..<...<....<.....<......")) # >> [ 3, 4 ]
print(track_robot(">>..")) # >> [ -2, 0 ]
print(track_robot("..<<..>>..<<..>>..")) # >> [ 2, 0 ]
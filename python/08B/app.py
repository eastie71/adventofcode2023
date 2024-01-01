"""
Question BA) Calculate the number of steps for all starting locations that end in "A" to travel to node ending in "Z". All locations must be at a node ending in "Z" to finish. 
The map data first line gives you direction of travel steps (left or right)
The remaining map data is map instructions (or nodes) for either LEFT or RIGHT. 
Sample Map instructions (test.txt):
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Above there are 2 starting nodes ending in "A" ("11A" and "22A"). Trace each of this nodes at the same time, until BOTH nodes end up at nodes ending in "Z". 
In this case, they finish at "11Z" and "22Z" and this example takes 6 steps.
"""
# Need LCM (lowest common multiple) function
import math

class Route:
    LEFT = 0
    RIGHT = 1
    
# Map Instructions of the form:
# map_instructions = {"AAA": ["BBB","BBB"], "BBB": ["AAA", "ZZZ"]}
    
def get_total_number_of_steps(map_data):
    map_instructions = {}
    directions = map_data[0].strip()
    print(f"Directions are: {directions}")

    # Skip line 1, it is blank. Start at line 2
    for line_no in range(2, len(map_data)):
        # print(f"Map data line: {map_data[line_no]}")
        lookup_name = map_data[line_no].split('=')[0].strip()
        left_location = map_data[line_no].split('(')[1].split(',')[0]
        right_location = map_data[line_no].split(',')[1].strip().split(')')[0]
        map_instructions[lookup_name] = [left_location, right_location]

    print(f"Map instructions: {map_instructions}")

    current_locations = []
    # Find each of the first locations ending in "A"
    for line_no in range(2, len(map_data)):
        if map_data[line_no].find("A =") != -1:
            current_locations.append(map_data[line_no].split('=')[0].strip())
    print(f"Starting locations = {current_locations}")
    
    position = 0
    location_step_counts = []
    ending_locations = []
    for i in range(0, len(current_locations)):
        location_step_counts.append(0)
        while current_locations[i][2] != 'Z':
            # print(f"Traversing location = {current_locations[i]}")
            if directions[position] == 'L':
                current_locations[i] = map_instructions[current_locations[i]][Route.LEFT]
            else: # directions[position] == 'R'
                current_locations[i] = map_instructions[current_locations[i]][Route.RIGHT]
            # print(f"NEW location = {current_locations[i]}")
            position += 1
            if position >= len(directions):
                position = 0
            location_step_counts[i] += 1
        ending_locations.append(current_locations[i])

    print(f"Ending locations = {ending_locations}")
    print(f"Location step counts = {location_step_counts}")

    print(f"Lowest Common Multiple = {math.lcm(*location_step_counts)}")
    return math.lcm(*location_step_counts)

with open("Q8input.txt", "r") as file:
#with open("test.txt", "r") as file:
    map_data = [line.strip() for line in file.readlines()]

print(f"2023 - Question 8B: Total number of steps for all nodes ending in \"A\" to travel to finish with all nodes ending in \"Z\" = {get_total_number_of_steps(map_data)}")

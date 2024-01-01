"""
Question 8A) Calculate the number of steps to travel from AAA to ZZZ. 
The map data first line gives you direction of travel steps (left or right) that is repeated until you reach ZZZ.
The remaining map data is map instructions for either LEFT or RIGHT. 
Sample Map instructions (test.txt):
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Above we start at map instruction AAA and follow the map directions (LLR), we continue this until we reach ZZZ. This example takes 6 steps.
"""
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

    current_location = "AAA"
    position = 0
    step_count = 0
    while current_location != "ZZZ":
        if directions[position] == 'L':
            current_location = map_instructions[current_location][Route.LEFT]
        else: # directions[position] == 'R'
            current_location = map_instructions[current_location][Route.RIGHT]
        position += 1
        if position >= len(directions):
            position = 0
        step_count += 1    

    return step_count

with open("Q8input.txt", "r") as file:
#with open("test.txt", "r") as file:
    map_data = [line.strip() for line in file.readlines()]

print(f"2023 - Question 8A: Total number of steps to travel from AAA to ZZZ = {get_total_number_of_steps(map_data)}")

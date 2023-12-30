"""
Question 3B) Sum all the gear ratios in the engine schematic.
A gear is any "*" symbol that has EXACTLY 2 adjacent part numbers. To calculate the gear ratio you multiply these two numbers.
Sample Engine Schematic (test.txt):
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
Above, the gear ratios are 467 and 35, and 755 and 598. Sum of the product of these ratios = 467835.
"""
gear_symbol = "*"

gear_ratios = {}

"""
Example of gear ratio results.
Key is the position of the gear symbol ('*') in the map eg "1-1" is row 1, col 1
Values are a list of numbers that are adjacent to the gear symbol.
gear_ratio_results = {
    "1-1": [1,2],
    "3-4": [2],
    "11-22": [32,44,556],
    "22-25": [256, 2]
}
"""

"""
Here is some test data:    
add_gear_part_number("1", 1, 1)
add_gear_part_number("2", 1, 1)
add_gear_part_number("32", 11, 22)
add_gear_part_number("44", 11, 22)
add_gear_part_number("556", 11, 22)
add_gear_part_number("10", 22, 33)
add_gear_part_number("20", 22, 33)
for gear in gear_ratios:
    if len(gear_ratios[gear]) == 2:
        print(f"gear: {gear}, with ratio = {gear_ratios[gear][0]}, {gear_ratios[gear][1]}")
"""

def add_gear_part_number(part_number, row, col):
    gear_key = str(row) + '-' + str(col)
    if gear_key in gear_ratios:
        gear_ratios[gear_key].append(int(part_number))
    else:
        gear_ratios[gear_key] = [int(part_number)]

def add_adjacent_row_gear_part_number(row, part_number, part_len, start_pos, row_number):
    if row == None:
        return
    real_start_pos = start_pos if start_pos == 0 else start_pos-1
    real_end_pos = start_pos + part_len if (start_pos + part_len) == len(row) else start_pos + part_len + 1
    for col_number in range(real_start_pos, real_end_pos):
        if gear_symbol.find(row[col_number]) != -1:
            add_gear_part_number(part_number, row_number, col_number)

def add_part_number_for_gear_ratios(part_number, start_pos, row_number, current_row, above_row, below_row):
    part_len = len(part_number)
    #left
    if start_pos > 0 and gear_symbol.find(current_row[start_pos-1]) != -1:
        col_number = start_pos - 1
        add_gear_part_number(part_number, row_number, col_number)

    #right
    if (start_pos + part_len) < len(current_row) and gear_symbol.find(current_row[start_pos + part_len]) != -1:
        col_number = start_pos + part_len
        add_gear_part_number(part_number, row_number, col_number)

    #above or below
    add_adjacent_row_gear_part_number(above_row, part_number, part_len, start_pos, row_number-1)
    add_adjacent_row_gear_part_number(below_row, part_number, part_len, start_pos, row_number+1)

def sum_valid_gear_ratios():
    sum = 0
    for gear in gear_ratios:
        if len(gear_ratios[gear]) == 2:
            sum += (gear_ratios[gear][0] * gear_ratios[gear][1])
    return sum

def get_gear_ratio_sum(schematic_lines):
    schematic_len = len(schematic_lines)
    for current_row in range(0, schematic_len):
        current_line = schematic_lines[current_row]
        part_number = ""
        for current_col in range(0, len(current_line)):
            if current_line[current_col].isdigit():
                part_number += current_line[current_col]
            elif len(part_number) > 0:
                # check if part number is valid
                add_part_number_for_gear_ratios(part_number, current_col - len(part_number), current_row, current_line,
                                     None if current_row == 0 else schematic_lines[current_row-1], 
                                     None if current_row == schematic_len-1 else schematic_lines[current_row+1])
                part_number = ""
        if len(part_number) > 0: 
            add_part_number_for_gear_ratios(part_number, len(current_line) - len(part_number), current_row, current_line,
                                     None if current_row == 0 else schematic_lines[current_row-1], 
                                     None if current_row == schematic_len-1 else schematic_lines[current_row+1])
    print(f"gear ratios are: {gear_ratios}\n")
    return sum_valid_gear_ratios()

with open("Q3input.txt", "r") as file:
#with open("test.txt", "r") as file:
    schematic_lines = [line.strip() for line in file.readlines()]

print(f"2023 - Question 3B: Total sum of all gear ratios = {get_gear_ratio_sum(schematic_lines)}")

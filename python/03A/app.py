"""
Question 3A) Sum all the part numbers in the engine schematic.
The valid part numbers to sum are any numbers with an adjacent symbol (including diaganally). A '.' is NOT a valid symbol
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
Above, the valid part numbers are 467, 35, 633, 617, 592, 755, 664 and 598. Sum of these = 4361.
"""

symbols = "~@#$%^&*()_-+=/"

def row_has_adjacent_symbols(start_pos, part_len, row):
    if row == None:
        return False
    real_start_pos = start_pos if start_pos == 0 else start_pos-1
    real_end_pos = start_pos + part_len if (start_pos + part_len) == len(row) else start_pos + part_len + 1
    for pos in range(real_start_pos, real_end_pos):
        if symbols.find(row[pos]) != -1:
            return True
    return False

def valid_part_number(part_number, start_pos, current_row, above_row, below_row):
    part_len = len(part_number)
    #left
    if start_pos > 0 and symbols.find(current_row[start_pos-1]) != -1:
        return True
    #right
    elif (start_pos + part_len) < len(current_row) and symbols.find(current_row[start_pos + part_len]) != -1:
        return True
    #above or below
    if row_has_adjacent_symbols(start_pos, part_len, above_row) or row_has_adjacent_symbols(start_pos, part_len, below_row):
        return True
    return False


def get_valid_part_number_sum(schematic_lines):
    valid_part_numbers = []
    schematic_len = len(schematic_lines)
    for current_row in range(0, schematic_len):
        current_line = schematic_lines[current_row]
        part_number = ""
        for current_col in range(0, len(current_line)):
            if current_line[current_col].isdigit():
                part_number += current_line[current_col]
            elif len(part_number) > 0:
                # check if part number is valid
                if valid_part_number(part_number, current_col - len(part_number), current_line,
                                     None if current_row == 0 else schematic_lines[current_row-1], 
                                     None if current_row == schematic_len-1 else schematic_lines[current_row+1]):
                    valid_part_numbers.append(int(part_number))
                part_number = ""
        if len(part_number) > 0 and valid_part_number(part_number, len(current_line) - len(part_number), current_line,
                                     None if current_row == 0 else schematic_lines[current_row-1], 
                                     None if current_row == schematic_len-1 else schematic_lines[current_row+1]):
            valid_part_numbers.append(int(part_number))
    print(f"part numbers are: {valid_part_numbers}")
    return sum(valid_part_numbers)

with open("Q3input.txt", "r") as file:
# with open("test.txt", "r") as file:
    schematic_lines = [line.strip() for line in file.readlines()]

print(f"Total sum of valid part numbers = {get_valid_part_number_sum(schematic_lines)}")

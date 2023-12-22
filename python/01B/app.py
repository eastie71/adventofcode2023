"""
Question 1B) Calculate the sum of the calibration values.
For each line, the calibration value can be found by combining the first "string" digit (eg. "one","two",etc) and the last "string" digit (in that order) to form a single two-digit number.
"""
# For the folliwing 4 lines, values are 29, 83, 13, 24, 42, 14, and 76. Sum = 281
test_entries = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

# "zero" is not possible
num_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# Get the first number in a string (where the number could be string ("one","two","three", etc) or integer form (1,2,3..))
# return number as a string
def get_first_num(value):
    first_pos = len(value)
    first_num = None
    # first look for number strings in the value
    for i in range(0,9):
        pos = value.find(num_strings[i])
        if pos != -1 and pos < first_pos:
            first_num = str(i + 1)
            first_pos = pos
    pos = 0        
    # now look for any numbers in the value
    for element in value:
        if element.isnumeric() and pos < first_pos:
            first_num = element
            first_pos = pos
            break
        pos += 1
        if pos >= first_pos:
            break
    if first_num == None:
        print(f"ERROR: Couldn't find first number in value: {value}")
    return first_num

# Get the second number (the last number) in a string (where the number could be string ("one","two","three", etc) or integer form (1,2,3..))
# return number as a string
def get_second_num(value):
    last_pos = 0
    second_num = None
    # first look for number strings in the value
    for i in range(0,9):
        # rfind finds the last position of string in string
        pos = value.rfind(num_strings[i])
        if pos != -1 and pos > last_pos:
            second_num = str(i + 1)
            last_pos = pos
    pos = 0        
    # now look for any numbers in the value
    for i in reversed(range(len(value))):
        if value[i].isnumeric() and i >= last_pos:
            second_num = value[i]
            break
        if i <= last_pos:
            break

    if second_num == None:
        print(f"ERROR: Couldn't find second number in value: {value}")
    return second_num


def get_calibration_sum(values):
    sum = 0
    for line in values:
        first_num = get_first_num(line)
        second_num = get_second_num(line)
        if (first_num == None or second_num == None):
            print(f"ERROR: cannot find calibration value with line = {line} !!")
            break
        else:
            value = int(first_num + second_num)
            sum += value
            print(f"Value = {value}")           
    return sum

with open("Q1input.txt", "r") as file:
    entries = [line.strip() for line in file.readlines()]

print(f"Total sum of calibration values = {get_calibration_sum(entries)}")

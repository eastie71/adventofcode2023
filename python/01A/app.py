"""
Question 1A) Calculate the sum of the calibration values.
For each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
"""
# For the folliwing 4 lines, values are 12, 38, 15, and 77. Sum = 142
test_entries = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def get_calibration_sum(values):
    sum = 0
    for line in values:
        found_first = False
        first_num = None
        second_num = None
        for element in line:
            if element.isnumeric():
                if found_first == False:
                    first_num = second_num = element
                    found_first = True
                else:
                    second_num = element
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

print(f"2023 - Question 1A: Total sum of calibration values = {get_calibration_sum(entries)}")

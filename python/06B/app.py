"""
Question 6B) Calculate the number of ways you can beat the current record in ONE race.
To beat the record, you must travel further than the distance of the current record in the time allowed.
To travel you hold down a button for a certain number of milliseconds, and that determines the distince you will travel per millisecond.
eg. hold down button for 4 milliseconds means you will travel 4 millimetres per millisecond.
Sample Time and Distance record (test.txt):
Time:      7  15   30
Distance:  9  40  200
For the above, there is actually only ONE record - ignore the spaces b/w the numbers the time is 71530, and the distance is 940200.
This record can be beaten b/w 14 and 71516 milliseconds. Hence a total of 71503 ways.
"""
# My approach for this solution is to calculate the first possible time to win (starting from 1) and 
# then calculate the last possible way to win (starting from the max time), and then assume all values in b/w are winners!

def convert_number_strings_to_number(numbers):
    number_string = ""
    for num_str in numbers:
        number_string += num_str
    return int(number_string)

def get_product_of_num_ways_to_win(input_lines):
    record_time = convert_number_strings_to_number([time for time in input_lines[0].split(':')[1].strip().split(' ') if time.isnumeric()])
    record_distance = convert_number_strings_to_number([distance for distance in input_lines[1].split(':')[1].strip().split(' ') if distance.isnumeric()])
    print(f"record time = {record_time}, record distance = {record_distance}")

    # From start (1) find the first win
    for speed in range(1, record_time):
        distance = speed * (record_time - speed)
        if distance > record_distance:
            first_win = speed
            break

    # From end (max time) - counting backwards (-1 increment), find last win
    for speed in range(record_time, 1, -1):
        distance = speed * (record_time - speed)
        if distance > record_distance:
            last_win = speed
            break

    print(f"first win = {first_win}, last win = {last_win}")

    # Assume all are wins in b/w first and last win
    return last_win - first_win + 1

with open("Q6input.txt", "r") as file:
#with open("test.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

print(f"The total number of ways to beat the record = {get_product_of_num_ways_to_win(input_lines)}")

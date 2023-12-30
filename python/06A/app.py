"""
Question 6A) Calculate the number of ways you can beat the current record in each race, then calculate the product of the count of the number of ways.
To beat the record, you must travel further than the distance of the current record in the time allowed.
To travel you hold down a button for a certain number of milliseconds, and that determines the distince you will travel per millisecond.
eg. hold down button for 4 milliseconds means you will travel 4 millimetres per millisecond.
Sample Time and Distance records (test.txt):
Time:      7  15   30
Distance:  9  40  200
For the above, for the 1st record of distance of 9 - you can beat this record by hold button for 2 milliseconds and travel 10 millimetres,
and 3 time 12 distance, 4 time 12 distance and 5 time 10 distance. ie. 4 different ways.
For the 2nd record, there are 8 ways to win
For the 3rd record, there are 9 ways to win.
Hence the answer is (4 x 8 x 9) = 288
"""

def get_product_of_num_ways_to_win(input_lines):
    total = 1
    times = [int(time) for time in input_lines[0].split(':')[1].strip().split(' ') if time.isnumeric()]
    distances = [int(distance) for distance in input_lines[1].split(':')[1].strip().split(' ') if distance.isnumeric()]
    print(f"times = {times}, distances = {distances}")
    winning_counts = []
    for record in range(0, len(times)):
        win_count = 0
        for speed in range(1, times[record]):
            distance = speed * (times[record] - speed)
            if distance > distances[record]:
                win_count += 1
        winning_counts.append(win_count)
    print(f"winning counts = {winning_counts}")
    for count in winning_counts:
        total *= count
    return total

with open("Q6input.txt", "r") as file:
#with open("test.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

print(f"2023 - Question 6A: Product of number of ways to beat each record = {get_product_of_num_ways_to_win(input_lines)}")

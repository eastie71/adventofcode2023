"""
Question 5A) Calculate the loweest location number that corresponds to any of the intial seed numbers.
Starting with an intial list of seed numbers, run through a series of source-->destination maps to eventualy arrive at a final set of location numbers.
Then, find the lowest number from the final set of location numbers.
Sample Seed Input and sets of source-->destination map rules (test.txt):
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
For the above, the final set of location numbers are 82,43,86,35 - so lowest is 35.
"""
# Of the form: [{"from": 98, "to": 99, "offset": -48}, {"from": 50, "to": 97, "offset": 2}]
source_dest_map = []

class Mapping:
    DEST_START_NUM = 0
    SOURCE_START_NUM = 1
    COUNT = 2

def build_source_to_dest_map(map_nums):
    source_map = {}
    source_map["from"] = int(map_nums[Mapping.SOURCE_START_NUM])
    source_map["to"] = source_map["from"] + int(map_nums[Mapping.COUNT]) - 1
    source_map["offset"] = int(map_nums[Mapping.DEST_START_NUM]) - source_map["from"]
    source_dest_map.append(source_map)
    print(f"Source --> Dest Map = {source_dest_map}")

def apply_source_and_get_new_source(inputs):
    results = []
    for input in inputs:
        result = -1
        for map in source_dest_map:
            if map["from"] <= input and map["to"] >= input:
                result = input + map['offset']
        if result == -1:
            result = input
        results.append(result)
    source_dest_map.clear()
    return results

def get_lowest_location_number(input_lines):
    lowest = -1
    source_inputs = [int(numstr) for numstr in input_lines[0].split(':')[1].strip().split(' ')]
    print(f"Starting source inputs = {source_inputs}")
    first_source = True
    for i in range(1, len(input_lines)):
        if input_lines[i].strip() == "":
            continue
        if not input_lines[i][0].isdigit() and not first_source:
            # apply source inputs to map and get new source inputs
            source_inputs = apply_source_and_get_new_source(source_inputs)
            print(f"new source inputs = {source_inputs}")
        elif input_lines[i][0].isdigit():
            first_source = False
            map_nums = input_lines[i].split(' ')
            # print(f"map nums = {map_nums}")
            build_source_to_dest_map(map_nums)
    source_inputs = apply_source_and_get_new_source(source_inputs)
    print(f"FINAL source inputs = {source_inputs}")
    # Find the lowest from the final destination numbers
    for i in range(0, len(source_inputs)):
        if lowest == -1 or lowest > source_inputs[i]:
            lowest = source_inputs[i]
    return lowest

with open("Q5input.txt", "r") as file:
#with open("test.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

print(f"Lowest location number = {get_lowest_location_number(input_lines)}")

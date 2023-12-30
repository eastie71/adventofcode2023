"""
Question 5B) Calculate the loweest location number that corresponds to any of the intial seed numbers.
Starting with an intial list of seed numbers; these seed numbers appear in pairs. The first number is the starting number, and the second number is the length of the range  
Run through a series of source-->destination maps to eventualy arrive at a final set of location numbers.
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
For the above, there are 27 seed numbers; 79 --> 92, and 55 --> 67
the lowest location number is obtained from seed number 82. With result of 84,84,77,45,46 and 46. Lowest location (last result) = 46.
"""
import sys
# Of the form: [ [{"from": 98, "to": 99, "offset": -48}, {"from": 50, "to": 97, "offset": 2}], [{"from": 15, "to": 55, "offset": -4}, {"from": 108, "to": 177, "offset": 25}] ]
source_dest_map_list = []

class Mapping:
    DEST_START_NUM = 0
    SOURCE_START_NUM = 1
    COUNT = 2

def build_source_to_dest_map(map_nums, source_dest_map):
    source_map = {}
    source_map["from"] = int(map_nums[Mapping.SOURCE_START_NUM])
    source_map["to"] = source_map["from"] + int(map_nums[Mapping.COUNT]) - 1
    source_map["offset"] = int(map_nums[Mapping.DEST_START_NUM]) - source_map["from"]
    source_dest_map.append(source_map)
    # print(f"Source --> Dest Map = {source_dest_map}")
    return source_dest_map

def get_initial_source_ranges(source_inputs):
    source_ranges = []
    for i in range(0, len(source_inputs)):
        if i % 2 != 0:
            source_ranges.append({"from": source_inputs[i-1], "to": source_inputs[i-1] + source_inputs[i] - 1})
    return source_ranges

def calc_new_source_ranges_from_map(sources, source_dest_map):
    new_source_ranges = []
    for source in sources:
        mapped_source_ranges = []
        current_source = source

        i = 0
        while i < len(source_dest_map):
            map = source_dest_map[i]
            new_source_range = {}
            if current_source["from"] >= map["from"] and current_source["from"] <= map["to"]:
                new_source_range["from"] = current_source["from"] + map["offset"]
                if source["to"] <= map["to"]:
                    new_source_range["to"] = current_source["to"] + map["offset"]
                    current_source = {}
                else:
                    new_source_range["to"] = map["to"] + map["offset"]
                    current_source["from"] = map["to"] + 1
                    # run through source-dest maps again - set i = -1, (+1 at end of loop)
                    i = -1
                mapped_source_ranges.append(new_source_range)
                if not current_source:
                    break
            i += 1

        if current_source:
            mapped_source_ranges.append(current_source)
        
        new_source_ranges += mapped_source_ranges
    print(f"NEW source ranges: {new_source_ranges}")
    return new_source_ranges


def get_lowest_location_number(input_lines):
    lowest = -1
    source_ranges = get_initial_source_ranges([int(numstr) for numstr in input_lines[0].split(':')[1].strip().split(' ')])
    print(f"Starting source inputs = {source_ranges}")

    first_map = True
    source_dest_map = []
    for i in range(1, len(input_lines)):
        if input_lines[i].strip() == "":
            continue
        if not input_lines[i][0].isdigit() and not first_map:
            source_dest_map_list.append(source_dest_map)
            source_dest_map = []
        elif input_lines[i][0].isdigit():
            first_map = False
            map_nums = input_lines[i].split(' ')
            # print(f"map nums = {map_nums}")
            source_dest_map = build_source_to_dest_map(map_nums, source_dest_map)
    source_dest_map_list.append(source_dest_map)  

    print(f"Source dest map list = {source_dest_map_list}")

    for source_dest_map in source_dest_map_list:
        source_ranges = calc_new_source_ranges_from_map(source_ranges, source_dest_map)

    lowest = sys.maxsize
    for source_range in source_ranges:
        if source_range["from"] < lowest:
            lowest = source_range["from"]
    return lowest

with open("Q5input.txt", "r") as file:
#with open("test.txt", "r") as file:
    input_lines = [line.strip() for line in file.readlines()]

print(f"Lowest location number = {get_lowest_location_number(input_lines)}")

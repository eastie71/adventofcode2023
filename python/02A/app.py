"""
Question 2A) Calculate the sum of line IDs for games with valid number of cubes.
Game is invalid if: red cubes > 12 or green cubes > 13 or blue cubes > 14.
Sample Game line:
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
"""

max_colour_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_game_valid(game):
    for colour in max_colour_cubes:
        cubes = game.split(':')[1]
        # look for all instances of colour in "cubes" string
        pos = cubes.find(colour)
        while pos != -1:
            # based on the position of the colour name in the string - grab the string before it, 
            # and split this based on a space (' ') and then grab the LAST element of the list (-1) to get the count of that colour. eg. 10 red
            count = int(cubes[:pos-1].split(' ')[-1])
            print(f">> Colour: {colour}, Count: {count}")
            if count > max_colour_cubes[colour]:
                print(">> INVALID GAME!")
                return False
            if len(cubes[pos:]) <= len(colour):
                break
            # grab the right side of the string after the colour just found and look for the colour again
            cubes = cubes[pos+len(colour):]
            pos = cubes.find(colour)
    print(">> VALID GAME!")
    return True

def get_valid_game_id_sum(entries):
    sum = 0
    for game in entries:
        id = int(game.split(' ')[1].split(':')[0])
        print(f"game id: {id}")
        if is_game_valid(game):
            sum += id
    return sum

# For the test input the VALID game IDs (line number) are 1, 2 and 5 and hence the sum = 8
with open("Q2input.txt", "r") as file:
#with open("test.txt", "r") as file:
    entries = [line.strip() for line in file.readlines()]

print(f"Total sum of valid game IDs = {get_valid_game_id_sum(entries)}")

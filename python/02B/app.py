"""
Question 2B) For each game, calculate the max count for each colour, multiply each count by each other and then sum this for all games.
Sample Game line:
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
So, Max 4 blue, 3 green, 1 red. Hence 4 x 3 x 1 = 12 (for game 2)
"""

def get_game_value(game):
    max_colour_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    value = 1
    save_game = game
    for colour in max_colour_cubes:
        game = save_game
        pos = game.find(colour)
        while pos != -1:
            # based on the position of the colour name in the string - grab the string before it, 
            # and split this based on a space (' ') and then grab the LAST element of the list (-1) to get the count of that colour. eg. 10 red
            count = int(game[:pos-1].split(' ')[-1])
            if count > max_colour_cubes[colour]:
                max_colour_cubes[colour] = count
            if len(game[pos:]) <= len(colour):
                break
            # grab the right side of the string after the colour just found and look for the colour again
            game = game[pos+len(colour):]
            pos = game.find(colour)
        if max_colour_cubes[colour] == 0:
            print(f">> ERROR: Colour: {colour} no count found!")
            value = 0
            break
        value *= max_colour_cubes[colour]
    print(f">> Value = {value}")        
    return value

def get_games_sum(entries):
    sum = 0
    for game in entries:
        id = int(game.split(' ')[1].split(':')[0])
        print(f"game id: {id}")
        sum += get_game_value(game.split(':')[1])
    return sum

# For the test input the 5 game values are 48, 12, 1560, 630, and 36. And sum = 2286.  
with open("Q2input.txt", "r") as file:
# with open("test.txt", "r") as file:
    entries = [line.strip() for line in file.readlines()]

print(f"Total sum of game values = {get_games_sum(entries)}")

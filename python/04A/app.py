"""
Question 4A) Sum all the winning number points from the scratchcards.
Points are calculated for all the winning numbers from card. Starting at 1 point and then doubling for each winning number on the card.
Sum all the points from all the cards for the final result.
Sample Scratchcards and Entries (test.txt):
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
Above, the points for each card are 8, 2, 2, 1, and 0. Sum of these = 13.
"""
def get_winning_points_sum(cards):
    sum = 0
    for card in cards:
        winning_numbers = [num for num in card.split(':')[1].split('|')[0].strip().split(' ') if num.isnumeric()]
        entry_numbers = [num for num in card.split('|')[1].strip().split(' ') if num.isnumeric()]
        print(f"Winning numbers = {winning_numbers}, Entries = {entry_numbers}")
        card_points = 0
        for entry in entry_numbers:
            if entry in winning_numbers:
                if card_points > 0: 
                    card_points *= 2
                else:
                    card_points = 1
        sum += card_points
    return sum

with open("Q4input.txt", "r") as file:
# with open("test.txt", "r") as file:
    scratchcards = [line.strip() for line in file.readlines()]

print(f"Total sum of points from the scratchcards = {get_winning_points_sum(scratchcards)}")

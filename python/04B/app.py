"""
Question 4B) Calculate the total numbers of scratchcards you end up with.
The number of winning numbers on a particular determines the number of extra (duplicate) scratchcards you win (gain).
Eg. in example below. Card 1 has 4 winning numbers, hence you gain another copy of cards 2,3,4,5 
Sample Scratchcards and Entries (test.txt):
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
For the above, the number of cards of each card number at the end is 1,2,4,8,14,1. Sum of these = 30.
"""
card_counts = {}

def add_card_count(num, count):
    if num not in card_counts:
        card_counts[num] = 0
    card_counts[num] += count

def get_total_count_of_scratchcards(cards):
    sum = 0
    for card in cards:
        card_number = int(card.split(':')[0].split(' ')[-1])
        winning_numbers = [num for num in card.split(':')[1].split('|')[0].strip().split(' ') if num.isnumeric()]
        entry_numbers = [num for num in card.split('|')[1].strip().split(' ') if num.isnumeric()]
        add_card_count(card_number,1)
        num_of_winning_cards = 0
        for entry in entry_numbers:
            if entry in winning_numbers:
                num_of_winning_cards += 1
        print(f"Card Number: {card_number}, Winning Card Count = {num_of_winning_cards}, Winning numbers = {winning_numbers}, Entries = {entry_numbers}")
        for i in range(card_number+1, card_number+num_of_winning_cards+1):
            add_card_count(i, card_counts[card_number])
    for card in card_counts:
        sum += card_counts[card]
        print(f"Card: {card}, has count = {card_counts[card]}")
    return sum

with open("Q4input.txt", "r") as file:
# with open("test.txt", "r") as file:
    scratchcards = [line.strip() for line in file.readlines()]

print(f"Total number of scratchcards = {get_total_count_of_scratchcards(scratchcards)}")

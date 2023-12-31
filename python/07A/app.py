"""
Question 7A) Calculate the total winnings for the Camel Card hands. 
To calculate the total winnings you need to rank each HAND from lowest ranked hand (1) to highest ranked hand (2) - then multiply each HANDS rank by
its corresponding BID, and the SUM of all these amounts is the Total winnings.
Sample Camel Cards list (test.txt):
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
The hands are ranked similar to poker hands. Card ranked A --> 2, Best hand is 5 of a kind eg. AAAAA
There are NO suits. So rank is 5, 4, 3 of a kind. 2 pair, 1 pair. If rank is same - then compare each card from left to right.
Eg. Hands KK677 and KTJJT are both 2 pair. Comparing each card left to right, the 2nd cards are 'K' and 'T' - therefore KK677 is the better hand.
Ranking each of these hands and multiplying by the bid = (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5) = 6440.
"""
import functools

card_ranks = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

def get_hand_score(hand):
    # assume hand is 5 cards
    card_counts = {}
    for current_card_pos in range(0, len(hand)):
        if hand[current_card_pos] in card_counts:
            card_counts[hand[current_card_pos]] += 1
        else:
            card_counts[hand[current_card_pos]] = 1
    # print(f"Card counts for Hand: {hand} is: {card_counts}")

    score = 0
    for card in card_counts:
        if card_counts[card] == 2:
            score += 1
        elif card_counts[card] == 3:
            score += 3
        elif card_counts[card] == 4:
            score = 5
        elif card_counts[card] == 5:
            score = 6
    # print(f"Score for hand: {hand} is {score}")
    return score

def hand_compare(hand1, hand2):
    result = get_hand_score(hand1["hand"]) - get_hand_score(hand2["hand"])
    if result != 0:
        return result
    for current_card_pos in range(0, len(hand1["hand"])):
        card_diff = card_ranks[hand1["hand"][current_card_pos]] - card_ranks[hand2["hand"][current_card_pos]]
        if card_diff != 0:
            return card_diff
        
def bidSort(hand):
    return(hand["bid"])

def get_camel_card_total_winnings(camel_card_hands):
    card_hands = []
    for camel_card_hand in camel_card_hands:
        card_hand = {}
        card_hand["hand"] = camel_card_hand.split(' ')[0]
        card_hand["bid"] = int(camel_card_hand.split(' ')[1])
        card_hands.append(card_hand)
    print(f"Card hands = {card_hands}")
    # https://learnpython.com/blog/python-custom-sort-function/
    card_hands = sorted(card_hands, key=functools.cmp_to_key(hand_compare))
    print(f"Bid Sorted Card hands = {card_hands}")
    total = 0
    for ranking in range(0, len(card_hands)):
        total += ((ranking+1) * card_hands[ranking]["bid"])

    return total

with open("Q7input.txt", "r") as file:
#with open("test.txt", "r") as file:
    camel_card_hands = [line.strip() for line in file.readlines()]

print(f"2023 - Question 7A: Total Winnings for Camel Card Hands = {get_camel_card_total_winnings(camel_card_hands)}")

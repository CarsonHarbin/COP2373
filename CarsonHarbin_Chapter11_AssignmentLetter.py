"""
Carson Harbin
Programming Exercise 11
This program prompts the user to play a card game giving them a list of 5 cards,
the player can then choose which of the 5 to change by entering the cards' corresponding numbers,
the program then replaces those cards and shows the user's final hand.
"""

import random

#Define the Deck class
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [f'{rank} of {suit}' for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


#Deal a poker hand of 5 cards
def deal_hand(deck, hand_size=5):
    return [deck.deal_card() for _ in range(hand_size)]


#Handle the draw phase
def draw_new_cards(deck, hand, indices_to_replace):
    for i in indices_to_replace:
        if 0 <= i < len(hand):
            hand[i] = deck.deal_card()
    return hand


#Main game loop
def main():
    deck = Deck()
    hand = deal_hand(deck)

    print("Your initial hand:")
    for idx, card in enumerate(hand, start=1):
        print(f"{idx}: {card}")

    #Get user input
    replace_input = input("\nEnter the card numbers you want to replace (1, 2, 3, 4, or 5): ")
    try:
        indices = [int(x.strip()) - 1 for x in replace_input.split(',') if x.strip().isdigit()]
        hand = draw_new_cards(deck, hand, indices)
    except Exception as e:
        print("Invalid input. No cards were replaced.")

    print("\nYour final hand:")
    for idx, card in enumerate(hand, start=1):
        print(f"{idx}: {card}")


if __name__ == "__main__":
    main()

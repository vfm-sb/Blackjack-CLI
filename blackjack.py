"""A Console Based Blackjack Game"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "VFM | SB"
__status__ = "Development"

from random import shuffle # Built-in Methods
from os import system


# Global Variables
CARD_SUIT = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
    "A": 11
}
SUITS = {
    "clubs": "♣︎",
    "diamonds": "♦",
    "hearts": "♥",
    "spades": "♠"
}

def deck_of_cards(decks: int = 1) -> list[list[str, str]]:
    """Generates and Returns Desired Number of Card Decks
    > One Deck Contains 4 Card Suits
    Argument:
        decks (int): Number of Card Decks [default=1]
    Returns:
        playing_cards (list[list[str, str]]): List of Cards Decks
    """
    playing_cards = []
    for symbol in SUITS.values():
        for card in CARD_SUIT:
            playing_cards.append([card, symbol])
    if decks > 1:
        _playing_cards = playing_cards.copy()
        for _ in range(decks - 1):
            playing_cards.extend(_playing_cards)
    return playing_cards

def shuffle_cards(playing_cards: list[str], shuffles: int = 1) -> None:
    """Shuffles Given Card Decks in Desired Times
    Arguments:
        playing_cards (list[str]): A List of Game Cards
        shuffles (int): Number of Shuffles for Randomness
    Returns:
        None
    """
    for _ in range(shuffles):
        shuffle(playing_cards)

def deal_card(playing_cards: list[str]) -> str:
    """Retrives and then Removes Last Card of the Playing Cards
    Returns:
        playing_cards[-1] (str)
    """
    return playing_cards.pop(-1)

def card_value(card: list[str]) -> int:
    """Retrieves and Returns The Card's Value from the CARD_SUIT"""
    return CARD_SUIT[card[0]]

def calculate_hand(hand: list[list]) -> int:
    """Calculates and Returns Given Hand's Total"""
    sum_of_hand = 0
    aces_count = 0
    for card in hand:
        if card[0] == "A":
            aces_count += 1
            continue
        sum_of_hand += card_value(card)
    if aces_count > 0:
        # while soft hand, an Ace counts as 11,
        # otherwise, in a hard hand, an Ace's value is 1
        while sum_of_hand + 11 + (aces_count - 1) <= 21:
            sum_of_hand += 11
            aces_count -= 1
        sum_of_hand += aces_count
    return sum_of_hand

def busted(hand: list[str]) -> bool:
    """Checks If The Hand Exceeds 21 or Not
    Returns:
        True (bool), if hand is over 21
        False (bool), if hand is 21 or less
    """
    return True if calculate_hand(hand) > 21 else False

def repr_card(card: list[str]) -> str:
    """Represents (Returns) a Card of the Deck"""
    return card[0] + card[1]

def repr_hand(hand: list[list], has_facedown_card: bool = False) -> str:
    """Represents (Returns) The Hand of the Participant
    > If Participant is the Dealer, The First Card will be Hidden!
    """
    hand_copy = []
    for card in hand:
        hand_copy.append(repr_card(card))
    if has_facedown_card:
        hand_copy[0] = "*"
    return ", ".join(hand_copy)

def blackjack():
    """Blackjack Game Function"""
    playing_cards = deck_of_cards()
    shuffle_cards(playing_cards)
    # deal initial hands
    player_hand = []
    dealer_hand = []
    # deal initial hands
    for _ in range(2):
        player_hand.append(deal_card(playing_cards))
        dealer_hand.append(deal_card(playing_cards))
    # while not busted() or "stand", ask player to "hit" or "stand"
    while True:
        # display initial hands
        print("Your Hand is:\n", repr_hand(player_hand))
        print("Dealer's Hand is:\n", repr_hand(dealer_hand, has_facedown_card=True))
        # ask player next move
        print("\nWhat's Your Next Move?", end=" ")
        player_choice = input('"hit" or "stand"?\n')
        if player_choice == "hit":
            new_card = deal_card(playing_cards)
            print(f"New Card is {repr_card(new_card)}")
            player_hand.append(new_card)
        elif player_choice == "stand":
            break
        # if player's hand is over 21, end of game
        if busted(player_hand):
            print("Busted! Your Hand is Over 21. You Lost!")
            print("\nFinal Hands:")
            print("Your Hand was:\n", repr_hand(player_hand))
            print("Dealer's Hand was:\n", repr_hand(dealer_hand))
            return
        print()
    print()
    # display dealer's full hand
    print("Dealer's Open Hand is:\n", repr_hand(dealer_hand))
    # dealer's play: dealer must hit if hand is less 17
    while calculate_hand(dealer_hand) < 17:
        new_card = deal_card(playing_cards)
        print(f"New Card is {repr_card(new_card)}")
        dealer_hand.append(new_card)
        # if dealer's hand is over 21, end of game
        if busted(dealer_hand):
            print("Busted! Dealer's Hand is Over 21. You Won!")
            print("\nFinal Hands:")
            print("Your Hand was:\n", repr_hand(player_hand))
            print("Dealer's Hand was:\n", repr_hand(dealer_hand))
            return
    # display final hands
    print()
    print("Final Hands:")
    print("Your Final Hand was:\n", repr_hand(player_hand))
    print("Dealer's Final Hand was:\n", repr_hand(dealer_hand))
    print()
    if calculate_hand(player_hand) > calculate_hand(dealer_hand):
        print("Your Hand is Higher, You Won!")
    elif calculate_hand(dealer_hand) > calculate_hand(player_hand):
        print("Dealer's Hand is Higher, You Lost!")
    else:
        print("Both Hands are the Same! It's a Tie.")
    return


def main():
    while True:
        system("clear")
        with open("blackjack_logo.txt", "r", encoding="utf-8") as blackjack_logo:
            print(blackjack_logo.read())
        blackjack()
        print()
        if input("Do Want to Play Again? (yes or no)?\n") == "no":
            break


main()


# Testing
# if __name__ == "__main__":
#     def deck_of_cards_printer(deck_of_cards: list) -> None:
#         for index, card_container in enumerate(deck_of_cards, start=1):
#             if index == len(deck_of_cards):
#                 print(card_container[0]+card_container[1])
#             elif index % 13 == 0:
#                 print(card_container[0]+card_container[1], end=",\n")
#             else:
#                 print(card_container[0]+card_container[1], end=", ")
#     deck_of_cards = deck_of_cards(decks=2)
#     deck_of_cards_printer(deck_of_cards)
#     shuffle_cards(deck_of_cards)
#     print("\nShuffled Cards:")
#     deck_of_cards_printer(deck_of_cards)

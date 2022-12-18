"""A Console Based Blackjack Game"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "2.0.4"
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


# Functions
def deck_of_cards(decks: int = 1) -> list:
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

def shuffle_cards(playing_cards: list, shuffles: int = 1) -> None:
    """Shuffles Given Card Decks in Desired Times
    Arguments:
        playing_cards (list[str]): A List of Game Cards
        shuffles (int): Number of Shuffles for Randomness
    Returns:
        None
    """
    for _ in range(shuffles):
        shuffle(playing_cards)

def deal_card(playing_cards: list) -> list[str, str]:
    """Retrives and then Removes Last Card of the Playing Cards
    Returns:
        playing_cards[-1] (str)
    """
    return playing_cards.pop(-1)

def card_value(card: list[str, str]) -> int:
    """Retrieves and Returns The Card's Value from the CARD_SUIT"""
    return CARD_SUIT[card[0]]

def calculate_hand(hand: list) -> int:
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

def busted(hand: list) -> bool:
    """Checks If The Hand Exceeds 21 or Not
    Returns:
        True (bool), if hand is over 21
        False (bool), if hand is 21 or less
    """
    return True if calculate_hand(hand) > 21 else False

def make_card(card: list[str, str]) -> list[str]:
    """Generates CLI Template of a Card"""
    card_model = []
    card_model.append("┌───────────┐") # Top
    card_model.append("│           │") # Face: [3] or [2],[3], and [-3] or [-2],[-3]
    card_model.append("│           │") # Suit: [3] and [3]
    card_model.append("│           │") # Empty
    card_model.append("│           │") # Suit: [7]
    card_model.append("│           │") # Empty
    card_model.append("│           │") # Suit: [3] and [3]
    card_model.append("│           │") # Face: [3] or [2],[3], and [-3] or [-2],[-3]
    card_model.append("└───────────┘")
    # inject card face
    if card[0] != "10":
        card_model[1] = f"│  {card[0]}     {card[0]}  │"
        card_model[-2] = f"│  {card[0]}     {card[0]}  │"
    else:
        card_model[1] = f"│ {card[0]}     {card[0]} │"
        card_model[-2] = f"│ {card[0]}     {card[0]} │"
    # inject suit symbol
    card_model[2] = f"│  {card[1]}     {card[1]}  │"
    card_model[4] = f"│     {card[1]}     │"
    card_model[-3] = f"│  {card[1]}     {card[1]}  │"
    return card_model

def display_card(card: list[str, str]) -> str:
    """Calls make_card() for Template Card Formation, Joins Pieces,
    and Returns Formed Card as String"""
    return "\n".join(make_card(card))

def display_hand(hand: list, has_facedown_card: bool = False) -> str:
    """Displays Hand"""
    hand_copy = hand.copy()
    if has_facedown_card:
        hand_copy[0] = ["*", "*"]
    return '\n'.join(map('   '.join, zip(*(make_card(card) for card in hand_copy))))

def blackjack() -> None:
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
        print("Your Hand is:\n", display_hand(player_hand), sep="")
        print("Dealer's Hand is:\n", display_hand(dealer_hand, has_facedown_card=True), sep="")
        # ask player next move
        print("\nWhat's Your Next Move?", end=" ")
        player_choice = input('"hit" or "stand"?\n')
        if player_choice == "hit":
            new_card = deal_card(playing_cards)
            print("New Card is:")
            print(display_card(new_card))
            player_hand.append(new_card)
        elif player_choice == "stand":
            break
        # if player's hand is over 21, end of game
        if busted(player_hand):
            print("Busted! Your Hand is Over 21. You Lost!")
            print("\nFinal Hands:")
            print("Your Hand was:\n", display_hand(player_hand), sep="")
            print("Dealer's Hand was:\n", display_hand(dealer_hand), sep="")
            return
        print()
    print()
    # display dealer's full hand
    print("Dealer's Open Hand is:\n", display_hand(dealer_hand))
    # dealer's play: dealer must hit if hand is less 17
    while calculate_hand(dealer_hand) < 17:
        new_card = deal_card(playing_cards)
        print("New Card is:")
        print(display_card(new_card))
        dealer_hand.append(new_card)
        # if dealer's hand is over 21, end of game
        if busted(dealer_hand):
            print("Busted! Dealer's Hand is Over 21. You Won!")
            print("\nFinal Hands:")
            print("Your Hand was:\n", display_hand(player_hand), sep="")
            print("Dealer's Hand was:\n", display_hand(dealer_hand), sep="")
            return
    # display final hands
    print()
    print("Final Hands:")
    print("Your Final Hand was:\n", display_hand(player_hand), sep="")
    print("Dealer's Final Hand was:\n", display_hand(dealer_hand), sep="")
    print()
    if calculate_hand(player_hand) > calculate_hand(dealer_hand):
        print("Your Hand is Higher, You Won!")
    elif calculate_hand(dealer_hand) > calculate_hand(player_hand):
        print("Dealer's Hand is Higher, You Lost!")
    else:
        print("Both Hands are the Same! It's a Tie.")
    return


def main():
    """Main Function"""
    while True:
        system("clear")
        with open("blackjack_logo.txt", "r", encoding="utf-8") as blackjack_logo:
            print(blackjack_logo.read())
        blackjack()
        print()
        if input("Do Want to Play Again? (yes or no)?\n") == "no":
            break


main()

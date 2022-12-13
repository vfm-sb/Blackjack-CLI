"""A Console Based Blackjack Game"""

__author__ = "VFM | SB"
__email__ = "vfm_sb@proton.me"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "VFM | SB"
__status__ = "Development"

from random import shuffle # Built-in Methods


# Global Variables
CARD_SUIT = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
    "A": 11
}

def deck_of_cards(decks: int = 1) -> list:
    playing_cards = []
    for _ in range(decks * 4):
        playing_cards.extend(CARD_SUIT.keys())
    return playing_cards

def shuffle_cards(deck_of_cards: list, shuffles: int = 1) -> None:
    for _ in range(shuffles):
        shuffle(deck_of_cards)

def deal_card(deck_of_cards: list) -> str:
    return deck_of_cards.pop(-1)

def card_value(card: str) -> int:
    return CARD_SUIT[card]

def calculate_hand(hand: list) -> int:
    sum_of_hand = 0
    for card in hand:
        if card == "A":
            continue
        sum_of_hand += card_value(card)
    if "A" in hand:
        aces_count = hand.count("A")
        while sum_of_hand + 11 + (aces_count - 1) <= 21:
            sum_of_hand += 11
            aces_count -= 1
        sum_of_hand += aces_count
    return sum_of_hand

def busted(hand: list) -> bool:
    return True if calculate_hand(hand) > 21 else False

def display_card(card: str) -> None:
    print(f"New Card is {card}")

def display_hand(hand: list, has_facedown_card: bool = False) -> None:
    hand_copy = hand.copy()
    if has_facedown_card:
        hand_copy[0] = "*"
    print(
        f'{"Dealer" if has_facedown_card else "Your"} Hand: '
        f'{", ".join(hand_copy)}'
    )

def display_endgame(player_hand: list, dealer_hand: list):
    print("Your Hand was: ", end="")
    display_hand(player_hand)
    print("Dealer's Hand was: ", end="")
    display_hand(dealer_hand)

def blackjack():
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
        display_hand(hand=player_hand)
        display_hand(hand=dealer_hand, has_facedown_card=True)
        print()
        # ask player next move
        player_choice = input('"hit" or "stand"?\n')
        if player_choice == "hit":
            card = deal_card(playing_cards)
            display_card(card)
            player_hand.append(card)
        elif player_choice == "stand":
            break
        # if player's hand is over 21, end of game
        if busted(player_hand):
            print("Busted! Your Hand is Over 21.")
            print("You Lost!")
            display_endgame(player_hand, dealer_hand)
            break
    


def main():
    blackjack()


main()


# Testing
if __name__ == "__main__":
    pass
    # playing_cards = deck_of_cards()
    # shuffle_cards(playing_cards)
    # # deal initial hands
    # player_hand = []
    # dealer_hand = []
    # for _ in range(2):
    #     player_hand.append(deal_card(playing_cards))
    #     dealer_hand.append(deal_card(playing_cards))
    # display_hand(player_hand)
    # display_hand(dealer_hand, is_dealer=True)
    # print()
    
    
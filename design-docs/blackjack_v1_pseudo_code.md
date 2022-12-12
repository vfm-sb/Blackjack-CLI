# Blackjack Version 1 - Pseudo Code

set values of a card_set
```python
cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "10": 10, "J": 10, "Q": 10, "K": 10,
    "A": 11
}
```

initialize deck_of_cards
add 4 * cards.keys() to deck_of_cards
deck_of_cards should contain 4 of each card.

shuffle deck_of_cards
    - shuffle_deck()
        - the function should shuffle the deck_of_cards only once.
            - The function should be able to shuffle the deck_of_cards as many times as desired.

deal hands
    - initialize player_hand
    - initialize dealer_hand
    - while player and dealer not have 2 cards each,
        - player_hand.append(deal_card())
        - dealer_hand.append(deal_card())

deal_card() Function for the Version 1:
    - retrieve and remove last item on list and return retrived item.

display cards
    - display both cards of the player:
        - `A, 10`, `7, 2`, `9, Q`...
    - display only one card of the dealer, first card should be hidden:
        - `*, 9`, `*, Q`, `*, A`...

finalizing player_hand
    - while not busted():
        - player's choice: "hit" or "stand"
        - if "hit":
            - display deal_card()
            - player_hand.append(deal_card())
        - elif "stand":
            - break

checking if player is busted()
    - if busted():
        - print("Busted!")
        - print("You Lost!")


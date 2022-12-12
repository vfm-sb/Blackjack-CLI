# Blackjack Algorithm - Version 1

## Core Algorithm

1. Dealing the Cards:
    1. player gets one card
    2. dealer gets one card
    3. then player gets another card
    4. and then dealer gets its second card

- Both cards of the player are displayed.
- One one card of the dealer is shown.
    - The other card is hidden.

* The value of a hand is the sum of the values of the individual cards.
* The value of a card is: 
    * The number on the card (2 through 10),
    * or 10 for a Face Card (Jack, Queen, King),
    * or either 1 or 11 for an Ace

2. The player can choose to "hit" or "stand".
    * If "hit", player receives another card.
    * If "stand", player keeps his/her current hand.

3. At this point, if player choose to "hit";
    * If player's hand exceeds 21, they lose immediately ("Busted")
    * Else, the player will be asked to "hit" or "stand"
        * As long as player's hand is not over 21, player can "hit" or "stand".

4. After the player stands;
    * The dealer reveals their face-down (hidden) card.

5. Based on the value of the Dealer's Hand,
    * The Dealer must "hit" or "stand".
        * The Dealer must "hit" if the hand has a value less than 17,
        * The Dealer must "stand" if the hand has value of 17 or higher.

6. If the Dealer's Hand exceeds 21, the player wins.
7. Otherwise, the winner is determined by comparing the Total Value of the Player's Hand  to the Total Value of the Dealer's hand.
    * The player wins if their hand is higher,
    * The dealer wins if their hand is higher,
    * It is a Tie, if the hands have the same value.

<br>

## Details of the Algorithm

### Deck of Cards

* In the Version 1, It is 52 Cards Only!
* No Clubs, Diamonds, Hearts, or Spades!
* Just 52 Cards.
    * 4 Aces, 4 Kings, 4 Queens, 4 Jacks, and 4 of each Number Cards.

<br>

### Randomizing The Deck of Cards

Shuffle Twice... (at Version 2)

Use `random.shuffle(deck_of_cards)

Create a `shuffle_deck()` Function
- For the Version 1, it should shuffle only once, as the default value.

### Dealing the Cards

#### First Alternative (Complete Randomness)

Even after shuffling the deck of card, pick the cards randomly.

**Steps**:
- Pick a card for the player. (Add it to Player's Hand)
    - Use `random.choice(deck_of_cards)`
    - Use `pop()` to retrieve and remove the card from the list.
        > **Info**: `pop()` mehtod receives an int value which represents index.
        1. Use `random.randint(0, len(deck_of_cards))
        2. Use `random.randrange(len(deck_of_cards))
- Pick a card for the dealer. (Add it to Dealer's Hand)
    - Apply the same steps as above.
- Pick a second card for the player.
    - Apply the same steps as above.
- And finally pick the second card for the dealer.
    - Apply the same steps as above.

#### Second Alternative(Pick the First or Last Card from the Deck)

Just pick first or last cards from the deck of cards.

**Steps**:
- Pick a card for the player.
    - Use `pop(0)` or `pop(-1)` to retrieve and remove the card from the list.
- Then a card for the dealer.
    - Same steps as above.
- Second card for the player.
    - Same steps as above.
- Pick the second card for the dealer.
    - Same steps as above.

### Displaying Cards

* Display both cards of the player:
    * `A, 10`, `7, 2`, `9, Q`...
* Display only one card of the dealer:
    * `9, *`, `Q, *`, `A, *`...

### Asking Player to Choose Next Move

Options: "hit" or "stand"


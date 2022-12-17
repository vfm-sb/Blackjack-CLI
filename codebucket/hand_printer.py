"""Hand Printer"""

def make_card(card: list[str]):
    card_model = []
    card_model.append("┌───────────┐") # Top
    card_model.append("│           │") # Face: [3] or [2],[3], and [-3] or [-2],[-3]
    card_model.append("│  @     @  │") # Suit: [3] and [3]
    card_model.append("│           │") # Empty
    card_model.append("│     @     │") # Suit: [7]
    card_model.append("│           │") # Empty
    card_model.append("│  @     @  │") # Suit: [3] and [3]
    card_model.append("│           │") # Face: [3] or [2],[3], and [-3] or [-2],[-3]
    card_model.append("└───────────┘")
    # replace '#' in card_model[1] and card_model[-1]
    if card[0] != "10":
        pass

def display_hand(hand: list[str]):
    pass

if __name__ == "__main__":
    example_card = ["10", "♥"]
    demo = "\n".join(make_card(example_card))
    print(demo)
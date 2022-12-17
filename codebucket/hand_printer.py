"""Hand Printer"""

def make_card(card: list[str]) -> list:
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

def display_card(card: list[str]) -> None:
    print("\n".join(make_card(card)))

def display_hand(hand: list[str]):
    print('\n'.join(map('   '.join, zip(*(make_card(card) for card in hand)))))

if __name__ == "__main__":
    example_card = ["10", "♥"]
    display_card(example_card)
    another_example = ["K", "♠"]
    display_card(another_example)
    print()
    example_hand = [["5", "♦"], ["10", "♣"], ["K", "♥"]]
    display_hand(example_hand)

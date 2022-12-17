"""Hand Printer"""

def replacer(string, new_string, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(string)):
        raise ValueError("index outside given string")
    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return new_string + string
    if index > len(string):  # add it to the end
        return string + new_string
    # insert the new string between "slices" of the original
    return string[:index] + new_string + string[index + 1:]

def bulk_replacer(string: str, new_string: str, indexes: list[int]):
    for index in indexes:
        string = replacer(string, new_string, index)
    return string

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
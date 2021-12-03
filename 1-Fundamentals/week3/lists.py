import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    user_input = input("Enter to pick a card or Q plus enter to quit: ")
    if user_input != "Q":
        selected_card = random.choice(diamonds)
        diamonds.remove(selected_card)
        hand.append(selected_card)
        print("Your hand:", hand)
        print("Remaining cards", diamonds)
    else:
        break
if not diamonds:
    print("There are no more cards to pick")

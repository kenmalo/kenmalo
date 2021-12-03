import random

high_score = 0


def dice_game():
    roll_1 = random.randint(1,6)
    roll_2 = random.randint(1,6)
    global high_score
    while True:
        high_score = 0
        print("Current High Score:" , high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        player_choice = (input("Enter Your Choice: "))
        total = roll_1 + roll_2
        high_score = high_score + total

        if  player_choice == "1":
            print("You roll a", roll_1)
            print("You roll a", roll_2)
            print("You have rolled a total of:", total)
            print("New high score!\n")
        elif  player_choice == "2":
           print("Goodbye!")
        break
dice_game()

import random


def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)

    while tries > 0:
        print(tries, "Number of tires left")
        guess = int(input("Guess a number between {start} and {stop}: "))

        if random_number == guess:
            print("You guessed the correct number")
            return
        elif random_number < guess:
            print("Guess higher!")
        elif random_number > guess:
            print(" Guess lower!")
            break
        tries -= 1
        if tries == 0:
            print("you have lost")


def guess_random_num_linear(tries, start, stop):
    random_number = random.randint(start, stop)
    print("The number for the program to guess is: {random_number}")

    while tries > 0:
        for guess in range(tries, stop + 1):
            print("Number of tries left: {tries}")

            if random_number == guess:
                print("The computer has guessed the correct number!")
                return
            else:
                print("The computer is guessing...{guess}")

            tries -= 1
            if tries == 0:
                print("The computer has failed to guess the correct number.")
                return


def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    lower = start
    upper = stop
    print("Random number to find: {random_number}")

    while tries > 0:
        guess = (lower + upper) // 2

        if random_number == guess:
            print("Got  it! {random_number}")
            return
        elif random_number > guess:
            print("Try Guessing higher!")
            lower = guess + 1
        else:
            print("Try Guessing lower")
            upper = guess - 1

        tries -= 1
        if tries == 0:
            print("the computer failed to find the number")
            return


guess_random_num_binary(5, 1, 100)

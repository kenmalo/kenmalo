from random import randint
item_price = randint(500, 1000)
count = 0
guess_price = -1

while item_price != guess_price and count < 10:
    guess_price = int(input("Enter a guess price between 500 and 1000: "))
    if guess_price < item_price:
        print("Item Price is more than your guess")
    elif guess_price > item_price:
        print("item price is less than your guess")
    else:
        print("you guessed right")
    count += 1

if item_price == guess_price:
    print("Congrat's, You guessed it right")
elif count >= 3:
    print("Sorry you are out of luck")

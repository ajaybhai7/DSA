# Number guessing game

from random import randint

secret_number = randint(1, 10)


while True:
    user_guess = int(input("Guess a Number"))

    if user_guess < secret_number:
        print("Lower Number")
        
    elif user_guess > secret_number:
        print("Higer Number")

    if user_guess == secret_number:
        print("You guess the number")
        break

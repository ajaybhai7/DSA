# Number guessing game

from random import randint

secret_number = randint(1, 10)


while user_guess != secret_number:
    user_guess = int(input("Guess a Number"))


    if user_guess < secret_number:
        print("Lower Number")
        break
    elif user_guess > secret_number:
        print("Higer Number")
        break
    if user_guess == secret_number:
        print("You guess the number")
        break

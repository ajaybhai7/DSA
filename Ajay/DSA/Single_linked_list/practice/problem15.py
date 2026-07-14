# Number guessing game

from random import randint

secret_number = randint(1, 10)

total_guess = 0

while True:
    user_guess = int(input("Guess a Number: "))

    if user_guess < secret_number:
        print("Lower Number")
        total_guess += 1

    elif user_guess > secret_number:
        print("Higer Number")
        total_guess +=1

    if user_guess == secret_number:
        print(f"You guess the number\nyou guess in : {total_guess} Attemp")
        total_guess +=1
        break

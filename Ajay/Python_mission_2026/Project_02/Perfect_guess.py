# We are going to write a program that generate a random number
# and ask the user to guess it.
#
# if the player's guess is higer than the actual number, the program
# displays "Lower number please" Similarly, if the user's guess is
# too low, the program prints "Higer number please" When the user guesses the correct
# Number the program displays the number of guesses the player used to arrive the 
# Number 

# Hint-- Use the random Module

import random
n = random.randint(1, 100)
a = -1
guesses = 1
while a != n:
    a = int(input("Guess the Number : "))
    if (a>n):
        print("Lower Number please")
        guesses += 1
    elif (a<n):
        print("Higher Number please")
        guesses += 1

print(f"You have guesses the number {n} correctly in {guesses} attempt")
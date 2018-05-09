# Python Number Guessing Game
# Developed by Max Pertgen
# v1.0 5/9/18


import random

guesses = 0
number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 100! Can you guess it?")

while guesses < 10:

    theGuess = int(input("Your guess: "))
    if theGuess == number:
        print("Congratulations! You guessed the number in " + str(guesses) + " guesses!")
        break
    else:
        print("That is incorrect :( Please try again!")
        guesses += 1
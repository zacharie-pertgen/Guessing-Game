# Python Number Guessing Game
# Developed by Max Pertgen
# v1.0 5/9/18

import os
import random
import time


while True:
    numOfGuesses = 0
    number = random.randint(1, 2)
    guesses = []
    guesses_set = set(guesses)

    os.system('cls')
    level = input("Welcome to the Number Guessing game! Would you like to try Easy, Medium, or Hard mode?")
    

    print("I'm thinking of a number between 1 and 10! Can you guess it?")

    while numOfGuesses < 10:
        theGuess = int(input("Your guess: "))
        if theGuess in guesses:
            os.system('cls')
            print("Sorry, you already guessed that number! Try again!")
        elif theGuess not in range(1, 11):
            os.system('cls')
            print("Sorry, your guess is not between 1-10! Try again.")
            print("So far you have guessed: " + ",".join(map(str,guesses)))
        else:
            if theGuess == number:
                os.system('cls')
                print("Congratulations! You guessed the number in " + str(numOfGuesses) + " guesses!")
                #replay = input("Would you like to play again?: ")
                #if replay == 'yes' or 'Yes':
                #    print("Great! Here we go again!")
                #    time.sleep(2)
                raise SystemExit
                #if replay == 'no' or 'No':
                #    print ("Goodbye!")
                #    time.sleep(2)
                #    raise SystemExit
            else:
                guesses.append(theGuess)
                os.system('cls')
                print("That is incorrect :( Please try again!")
                print("So far you have guessed: " + ",".join(map(str,guesses)))
                numOfGuesses += 1   
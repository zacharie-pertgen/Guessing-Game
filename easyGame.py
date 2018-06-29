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
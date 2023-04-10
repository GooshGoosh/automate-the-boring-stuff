#!/usr/bin/env python3

# This is a guess the number game.

import random
import pyinputplus as pyip


def guess_number():
    # Obtain a random number between 1-20 (inclusive).
    secretNumber = random.randint(1, 20)
    print('\nI am thinking of a number between 1 and 20.')

    # Ask the player to guess 6 times.
    for guessesTaken in range(1, 7):
        print('Take a guess.')
        guess = pyip.inputNum(min=1, max=20)        # Obtain an integer from the user.

        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')
        else:
            break       # This condition is the correct guess.

    if guess == secretNumber:
        print('Good job! You guessed my number in {} guesses!'.format(guessesTaken))
    else:
        print('Nope. The number I was thinking of was {}'.format(secretNumber))




def main():
    guess_number()


if __name__ == "__main__":
    main()


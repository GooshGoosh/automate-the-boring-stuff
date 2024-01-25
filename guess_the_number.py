'''
Chapter 2 Project: Guess the Number

guess_the_number.py - Has the user guess a number between 1 and 20.
'''


import random
import pyinputplus as pyip


def guess_number():
    """Generates a random number and has the user try to guess the number 6 times.
    """
    # Obtain a random number between 1-20 (inclusive).
    secret_number = random.randint(1, 20)
    print('\nI am thinking of a number between 1 and 20.')

    # Ask the player to guess 6 times.
    for guesses_taken in range(1, 7):
        print('Take a guess.')
        guess = pyip.inputNum(min=1, max=20)

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break       # This condition is the correct guess.

    if guess == secret_number:
        print(f'Good job! You guessed my number in {guesses_taken} guesses!')
    else:
        print(f'Nope. The number I was thinking of was {secret_number}')




def main():
    """Main function to run the program.
    """
    guess_number()


if __name__ == "__main__":
    main()

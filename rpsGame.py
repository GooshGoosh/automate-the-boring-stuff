#!/usr/bin/env python3

import random
import sys

def main():
    # These variables keep track of the number of wins, losses, and ties.
    wins = 0
    losses = 0
    ties = 0

    while True:     # The main game loop.
        print('\n{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))
        
        while True:     # The player input loop.
            print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
            playerMove = input()
            if playerMove == 'q':
                sys.exit()      # Quit the program
            elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
                break       # Break out of the player input loop.
            print('\nType one of r, p, s, or q.')

        # Display what the player chose:
        if playerMove == 'r':
            print('\nROCK versus...')
        elif playerMove == 'p':
            print('\nPAPER versus...')
        elif playerMove == 's':
            print('\nSCISSORS versus...')

        # Display what the computer chose:
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'r'
            print('ROCK')
        elif randomNumber == 2:
            computerMove = 'p'
            print('PAPER')
        elif randomNumber == 3:
            computerMove = 's'
            print('SCISSORS')

        # Display and record the win/loss/tie:
        if playerMove == computerMove:
            print('It is a tie!')
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'p' and computerMove == 'r':
            print('You win!')
            wins = wins + 1
        elif playerMove == 's' and computerMove == 'p':
            print('You win!')
            wins = wins + 1
        elif playerMove == 'r' and computerMove == 'p':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print('You lose!')
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print('You lose!')
            losses = losses + 1


if __name__ == "__main__":
    main()


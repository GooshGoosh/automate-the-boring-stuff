#!/usr/bin/env python3

import random
import sys


def rps():
    """Simulates games of Rock-Paper-Scissors between the user and the computer.
    """
    wins = 0
    losses = 0
    ties = 0


    while True:     # The main game loop.
        print(f'\n{wins} Wins, {losses} Losses, {ties} Ties')

        while True:     # The player input loop.
            print('\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit')
            player_move = input()
            if player_move == 'q':
                sys.exit(0)
            elif player_move in ('r', 'p', 's'):
                break
            print('\nType one of r, p, s, or q.')

        # Display what the player chose:
        if player_move == 'r':
            print('\nROCK versus...')
        elif player_move == 'p':
            print('\nPAPER versus...')
        elif player_move == 's':
            print('\nSCISSORS versus...')

        # Display what the computer chose:
        random_num = random.randint(1, 3)
        if random_num == 1:
            computer_move = 'r'
            print('ROCK')
        elif random_num == 2:
            computer_move = 'p'
            print('PAPER')
        elif random_num == 3:
            computer_move = 's'
            print('SCISSORS')

        # Display and record the win/loss/tie:
        if player_move == computer_move:
            print('It is a tie!')
            ties = ties + 1
        elif player_move == 'r' and computer_move == 's':
            print('You win!')
            wins = wins + 1
        elif player_move == 'p' and computer_move == 'r':
            print('You win!')
            wins = wins + 1
        elif player_move == 's' and computer_move == 'p':
            print('You win!')
            wins = wins + 1
        elif player_move == 'r' and computer_move == 'p':
            print('You lose!')
            losses = losses + 1
        elif player_move == 'p' and computer_move == 's':
            print('You lose!')
            losses = losses + 1
        elif player_move == 's' and computer_move == 'r':
            print('You lose!')
            losses = losses + 1


def main():
    """Main function to run the program.
    """
    rps()


if __name__ == "__main__":
    main()

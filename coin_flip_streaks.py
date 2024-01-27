'''
Chapter 4 Project: Coin Flip Streaks

coin_flip_streaks.py - A program that performs a number of coin flips to determine
the probability of landing on "HEADS" or "TAILS".
'''


import random


def coin_flip(num_of_experiments):
    """Simulates 100 coin flips a given number of times. Tracks the number of
    6-streak chains of the same result and gives the percentage of how many
    times a 6-streak occurred throughout the experiments.

    Args:
        num_of_experiments (int): The number of experiments to run.
    """
    num_of_streaks = 0
    experiment_num = 0

    print(f'\nProcessing {num_of_experiments} experiment(s) of 100 coin flips...')

    # Loop to perform the number of experiemnts stated in the num_of_experiments variable.
    while experiment_num < num_of_experiments:
        experiment_num += 1
        result_of_flips = []
        streak_counter = 0
        flip_num = 0

        # Perform 100 coin flips and store the results in result_of_flips.
        while flip_num < 100:
            flip_num += 1
            if random.randint(0, 1) == 0:
                result_of_flips.append("H")
            else:
                result_of_flips.append("T")

        # Search for a 6-streak in the 100 flip results.
        for i in range(len(result_of_flips) - 1):
            if result_of_flips[i] == result_of_flips[i + 1]:
                streak_counter += 1
                if streak_counter == 6:
                    num_of_streaks += 1
                    break
            else:
                streak_counter = 0  # Reset the streak counter if the streak is broken.

    print(f'Chance of streak: {(num_of_streaks / (num_of_experiments / 100))}%')
    print(f'Number of streaks: {num_of_streaks}')


def main():
    """Main function to run the program.
    """
    # The number of experiments to run.
    experiments = 15000

    coin_flip(experiments)


if __name__ == "__main__":
    main()

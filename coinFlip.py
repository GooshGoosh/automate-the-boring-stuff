#!/usr/bin/env python3

# coinFlip.py - A program that performs a number of coin flip to determine
# the probability of landing on "HEADS" or "TAILS". 

import random


def coin_flip(numberOfExperiments):
    numberOfStreaks = 0             # Variable to track the number of streaks of 6.

    print("\nProcessing {} experiment(s) of 100 coin flips...".format(numberOfExperiments))
    
    # Loop to perform the number of experiemnts stated in the numberOfExperiments variable.
    for experimentNumber in range(numberOfExperiments):
        numOfFlips = []
        streakCounter = 0
        for flip in range(100):                 # Use a random selection of 0 or 1 to determine if the 
            if random.randint(0, 1) == 0:       # coin flip landed on heads or tails, respectively.
                numOfFlips.append("H")          # Add either an "H" or a "T" to the list numOfFlips
            else:
                numOfFlips.append("T")

        for i in range(len(numOfFlips) - 1):            # Iterate through the list to find if a streak of 6 occurred 
            if numOfFlips[i] == numOfFlips[i + 1]:      # during the 100 coin flips. 
                streakCounter += 1
                if streakCounter == 6:                  # If a 6-streak is found, then increase the numberOfStreaks 
                    numberOfStreaks += 1                # counter and break out of the current experiment. 
                    break
            else:
                streakCounter = 0       # Reset the streak counter if the streak is broken.
    
    print("Chance of streak: {}%".format((numberOfStreaks / (numberOfExperiments / 100))))
    print("Number of streaks: {}".format(numberOfStreaks))


def main():
    experiments = 15000     # Variable to represent the number of experiments to run.
    coin_flip(experiments)


if __name__ == "__main__":
    main()


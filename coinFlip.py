#!/usr/bin/env python3

# coinFlip.py - A program that performs a number of coin flip to determine
# the probability of landing on "HEADS" or "TAILS". 

import random

def main():
    numberOfStreaks = 0
    numberOfExperiments = 10000

    print("\nProcessing {} experiment(s) of 100 coin flips...".format(numberOfExperiments))
    for experimentNumber in range(numberOfExperiments):
        numOfFlips = []
        streakCounter = 0
        for flip in range(100):
            if random.randint(0, 1) == 0:
                numOfFlips.append("H")
            else:
                numOfFlips.append("T")

        for i in range(len(numOfFlips)):
            if i == 0:
                continue
            elif numOfFlips[i] == numOfFlips[i - 1]:
                streakCounter += 1
                if streakCounter == 6:
                    numberOfStreaks += 1
                    break
            else:
                streakCounter = 0
    
    print("Chance of streak: {}%".format((numberOfStreaks / 100)))


if __name__ == "__main__":
    main()


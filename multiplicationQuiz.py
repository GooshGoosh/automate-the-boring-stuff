#!/usr/bin/env python3

# multiplicationQuiz.py - Gives the user 10 randomly selected
# multiplication questions.

import pyinputplus as pyip
import random
import time


def quiz(numberOfQuestions):
    correctAnswers = 0

    for questionNumber in range(numberOfQuestions):
        # Pick two random numbers.
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        prompt = '\n#{}: {} x {} = '.format((questionNumber + 1), num1, num2)

        try:
            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            pyip.inputStr(prompt, allowRegexes=['^{}$'.format(num1 * num2)],
                          blockRegexes=[('.*', 'Incorrect!')],
                          timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            # This block runs if no exceptions were reaised in the try block.
            print('Correct!')
            correctAnswers += 1

        time.sleep(1)   # Brief pause to let user see the result.

    print('Score: {} / {}'.format(correctAnswers, numberOfQuestions))


def main():
    quiz(10)


if __name__ == "__main__":
    main()


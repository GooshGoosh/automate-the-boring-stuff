'''
Chapter 8 Project: Multiplication Quiz

multiplication_quiz.py - Gives the user a number of randomly selected
multiplication questions.
'''


import random
import time
import pyinputplus as pyip


QUESTIONS = 10

def quiz(num_of_questions):
    """Gives the user a specified number of multiplication questions.

    Args:
        num_of_questions (int): The number of questions to give the user.
    """
    correct_answers = 0

    for question_num in range(num_of_questions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        prompt = f'\n#{(question_num + 1)}: {num1} x {num2} = '

        try:
            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            pyip.inputStr(prompt, allowRegexes=[f'^{num1 * num2}$'],
                          blockRegexes=[('.*', 'Incorrect!')],
                          timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            print('Correct!')
            correct_answers += 1

        time.sleep(1)   # Brief pause to let user see the result.

    print(f'Score: {correct_answers} / {num_of_questions}')


def main():
    """Main function to run the program.
    """
    quiz(QUESTIONS)


if __name__ == "__main__":
    main()

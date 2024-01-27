'''
Chapter 9 Project: Generating Random Quiz Files

random_quiz_generator.py - Creates quizzes with questions and answers in random
order, along with the answer key.
'''


import random


NUM_TO_GENERATE = 35


def generate_quiz(quiz_num):
    """Generates a quiz file of the 50 states and their capitals.

    Args:
        quiz_num (int): The current number of the quizzes being generated.
    """
    # The quiz data. Keys are states and values are their capitals.
    capitals = {'Alabama':'Montgomery', 'Alaska': 'Juneau', 'Arizona':'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
                'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
                'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
                'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
                'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
                'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
                'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
                'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
                'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
                'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
                'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    #Create the quiz and answer key files
    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding='UTF-8')
    answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w', encoding='UTF-8')

    # Write out the header for the quiz.
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form{quiz_num + 1})')
    quiz_file.write ('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # Loop through all 50 states, making a question for each.
    for question_num in range(50):

        # Get right and wrong answers.
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)
        answer_options= wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        # Write the question and the answer options to the quiz file.
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        # Write the answer key to a file.
        answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}")

    # Close the generated files.
    quiz_file.close()
    answer_key_file.close()


def main():
    """Main function to run the program.
    """
    # Generate quiz files.
    for quiz in range(NUM_TO_GENERATE):
        generate_quiz(quiz)

    print("\nQuiz files generated")


if __name__ == "__main__":
    main()

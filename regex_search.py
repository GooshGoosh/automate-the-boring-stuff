'''
Chapter 9 Project: Regex Search

regex_search.py - Opens all .txt files in a given folder and searches for any line
that matches a user-supplied regular expression. The results are printed to the
screen.
'''


import re
import os
import sys


def search_directory(directory, regex):
    """Searches through the given directory for the specified regex in all .txt
    files. The results are printed to the screen.

    Args:
        directory (str): The path of the directory to search through.
        regex (str): The regular expression to search for.
    """
    if not os.path.isdir(directory):
        print(f'\nInvalid directory path: {directory}')
        sys.exit(1)

    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            continue
        if not os.path.join(directory, file).endswith('.txt'):
            continue

        with open(os.path.join(directory, file), 'r', encoding='UTF-8') as text_file:
            text = text_file.read()

        result = regex.search(text)
        if result is not None:
            print(f'\nMatch found: {file}')


def main():
    """Main function to run the program.
    """
    print('\nPlease enter the full path to a folder that you would like to search:\n')
    directory_to_search = input()

    print('\nPlease enter the text that you would like to search for:\n')
    search_text = re.compile(input())

    search_directory(directory_to_search, search_text)


if __name__ == "__main__":
    main()

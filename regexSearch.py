#!/usr/bin/env python3

# regexSearch.py - Opens all .txt files in a given folder and searches for
# any line that matches a user-supplied regular expression. The results should
# be printed to the screen.


import re
import os
import sys


def search_directory(directory, regex):
    if not os.path.isdir(directory):
        print('\nInvalid directory path: {}'.format(directory))
        sys.exit(1)

    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            continue
        elif not os.path.join(directory, file).endswith('.txt'):
            continue
        else:
            with open(os.path.join(directory, file), 'r') as textFile:
                text = textFile.read()
            textFile.close()

            result = regex.search(text)
            if result != None:
                print('\nMatch found: {}'.format(file))


def main():
    print('\nPlease enter the full path to a folder that you would like to search:\n')
    directoryToSearch = input()

    print('\nPlease enter the text that you would like to search for:\n')
    searchText = re.compile(input())

    search_directory(directoryToSearch, searchText)


if __name__ == "__main__":
    main()


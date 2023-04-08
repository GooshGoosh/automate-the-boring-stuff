#!/usr/bin/env python3

# selectiveCopy.py - Takes a file extension, a path to a current directory,
# and path to a directory, either an existing directory or a directory that
# the user wants created. The program then walks through the first given
# directory for files with the given file extension and copies them to
# to the destination of the second directory.


import os
import sys
import shutil
import pyinputplus as pyip


def main():
    # Ensure there are three command-line arguments given
    if len(sys.argv) != 4:
        print('\nUsage: selectiveCopy.py <file ext.> <search destination> <copy destination>')
        sys.exit(1)

    extension = sys.argv[1]
    searchDestination = os.path.abspath(sys.argv[2])
    copyDestination = os.path.abspath(sys.argv[3])

    # Ensure the search destination exists
    if not os.path.isdir(searchDestination):
        print('\nSearch destination "{}" does not exist!'.format(searchDestination))
        sys.exit(1)

    # Check if the copy destination exists and if not, ask the user if they
    # would like to create it.
    if not os.path.isdir(copyDestination):
        print('\nCopy destination "{}" does not exist.'.format(copyDestination))
        answer = pyip.inputYesNo(prompt='Would you like to create it? (Y/N)')
        if answer == 'no':
            print('Exiting program...')
            sys.exit(0)
        else:
            print('Creating copy destination {}...'.format(copyDestination))
            os.mkdir(copyDestination)

    for foldername, subfolders, filename

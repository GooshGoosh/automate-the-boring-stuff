#!/usr/bin/env python3

# findLargeFiles.py - Takes a path to a directory as a command-line argument then
# walks through the given directory and prints any files, as well as their absolute path,
# that are are more than 100 MB in size.


import os
import sys


def find_file_sizes(directory):
    # Walk through the given directory and loop through every file in each directory
    # that is stepped into.
    for folder, subfolders, filenames in os.walk(directory):
        for file in filenames:
            # Get the file size in MB rounded to the first decimal.
            filePath = os.path.join(folder, file)
            fileSize = round(os.path.getsize(filePath) / 1024**2, 1)

            # Print the file and path to the file if it is over 100 MB.
            if fileSize > 100.0:
                print('\nFile: {}'.format(file))
                print('Path: {}'.format(os.path.join(folder, file)))
            else:
                continue


def main():
    # Ensure there is only one command-line argument given.
    if len(sys.argv) != 2:
        print('\nUsage: findLargeFiles.py </path/to/directory>')
        sys.exit(1)

    # Ensure that the given directory exists and that it is a directory, not a file.
    searchDirectory = os.path.abspath(sys.argv[1])
    if not os.path.exists(searchDirectory):
        print('\nDirectory "{}" does not exist!'.format(searchDirectory))
        sys.exit(1)
    elif not os.path.isdir(searchDirectory):
        print('\nDirectory "{}" is not a directory!'.format(searchDirectory))
        sys.exit(1)
    else:
        print('\nWalking through {}'.format(searchDirectory))
        print('\nFiles greater than 100 MB: ')
        find_file_sizes(searchDirectory)


if __name__ == "__main__":
    main()


'''
Chapter 10 Project: Deleting Unneeded Files

find_large_files.py - Takes a path to a directory as a command-line argument then
walks through the given directory and prints any files, as well as their absolute
path, that are more than 100 MB in size.
'''


import os
import sys


def find_file_sizes(directory):
    """Walks through the given directory and searches for any files that are
    larger than 100 MB in size.

    Args:
        directory (str): Path to a directory to search through.
    """
    # Walk through the given directory and loop through every file in each directory
    # that is stepped into.
    for folder, subfolders, filenames in os.walk(directory):
        for file in filenames:
            # Get the file size in MB rounded to the first decimal.
            file_path = os.path.join(folder, file)
            file_size = round(os.path.getsize(file_path) / 1024**2, 1)

            # Print the file and path to the file if it is over 100 MB.
            if file_size > 100.0:
                print(f'\nFile: {file}')
                print(f'Path: {os.path.join(folder, file)}')
            else:
                continue


def main():
    """Main function to run the program.
    """
    # Ensure there is only one command line argument given.
    if len(sys.argv) != 2:
        print('\nUsage: find_large_files.py </path/to/directory>')
        sys.exit(1)

    # Ensure that the given directory exists and that it is a directory, not a file.
    search_directory = os.path.abspath(sys.argv[1])
    if not os.path.exists(search_directory):
        print(f'\nDirectory "{search_directory}" does not exist!')
        sys.exit(1)
    elif not os.path.isdir(search_directory):
        print(f'\nDirectory "{search_directory}" is not a directory!')
        sys.exit(1)
    else:
        print(f'\nWalking through {search_directory}')
        print('\nFiles greater than 100 MB: ')
        find_file_sizes(search_directory)


if __name__ == "__main__":
    main()

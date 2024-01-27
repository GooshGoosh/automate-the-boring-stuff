'''
Chapter 10 Project: Selective Copy

selective_copy.py - Takes a file extension, a path to a search directory,
and path to a target directory, either an existing directory or a directory
that the user wants created. The program then walks through the first given
directory for files with the given file extension and copies them to
to the destination of the second directory.
'''


import os
import sys
import shutil
import pyinputplus as pyip


def copy_directory(extension, search_dir, copy_dir):
    """Copies files with a given file extension from one directory to another.

    Args:
        extension (str): File extension to copy to the target directory.
        search_dir (str): Path of the target directory to search through.
        copy_dir (str): Path of the destination directory to copy files to.
    """
    for foldername, subfolders, filenames in os.walk(search_dir):
        print(f'\nSearching for files with a "{extension}" extension in {foldername}...\n')
        for filename in filenames:
            if filename.endswith(extension):
                old_file_path = os.path.join(foldername, filename)
                new_file_path = os.path.join(copy_dir, filename)
                print(f'Copying {filename} from {old_file_path} to {new_file_path}')
                shutil.copy(old_file_path, new_file_path)
            else:
                continue


def main():
    """Main function to run the program.
    """
    # Ensure there are three command line arguments given
    if len(sys.argv) != 4:
        print('\nUsage: selectiveCopy.py <file ext.> <search destination> <copy destination>')
        sys.exit(1)

    extension = sys.argv[1]
    search_dir = os.path.abspath(sys.argv[2])
    copy_dir = os.path.abspath(sys.argv[3])

    # Ensure the search destination exists
    if not os.path.isdir(search_dir):
        print(f'\nSearch destination "{search_dir}" does not exist!')
        sys.exit(1)

    # Check if the copy destination exists and if not, ask the user if they
    # would like to create it.
    if not os.path.isdir(copy_dir):
        print(f'\nCopy destination "{copy_dir}" does not exist.')
        answer = pyip.inputYesNo(prompt='Would you like to create it? (Y/N): ')
        if answer == 'no':
            print('Exiting program...')
            sys.exit(0)
        else:
            print(f'Creating copy destination {copy_dir}...')
            os.mkdir(copy_dir)

    copy_directory(extension, search_dir, copy_dir)


if __name__ == "__main__":
    main()

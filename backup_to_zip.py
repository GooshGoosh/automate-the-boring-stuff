'''
Chapter 10 Project: Backing Up a Folder into a ZIP File

backup_to_zip.py - Copies an entire folder and its contents into a ZIP file with
the current date appended. Takes a single command-line argument in the form of
the path of the folder that the user wants to back up.
'''


import zipfile
import os
import datetime
import sys


def backup_zip(directory):
    """Backs up the given directory into a ZIP file with the current date appended
    to the file name.

    Args:
        directory (str): Absolute path of a directory to be backed up.
    """
    # Get the current date in MM/DD/YYYY format.
    today = datetime.date.today()
    format_today = today.strftime("-%m-%d-%Y")

    # Back up the entire contents of the given folder into a ZIP file.
    parent_dir = os.path.dirname(directory)
    zip_filename = os.path.join(parent_dir, os.path.basename(directory)) + format_today + '.zip'

    # Ensure the folder exists.
    if not os.path.exists(directory):
        print(f'\nFolder "{directory}" does not exist!')
        sys.exit(1)

    # Check if there is already a ZIP backup saved for the same date.
    if os.path.exists(directory + format_today):
        print(f'\nBackup ZIP of "{directory}" for {format_today} already exists!')
        sys.exit(1)

    # Create the ZIP file.
    print(f'\nCreating {zip_filename}...')
    backup_zip_file = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(directory):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backup_zip_file.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(directory) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue    # Don't back up the backup ZIP files.
            backup_zip_file.write(os.path.join(foldername, filename))
    backup_zip_file.close()
    print('Done.')


def main():
    """The main function to run the program.
    """
    # Ensure there is only one command line argument given.
    if len(sys.argv) != 2:
        print('\nUsage: backup_to_zip </path/to/folder>')
        sys.exit(1)

    backup_dir = os.path.abspath(sys.argv[1])
    backup_zip(backup_dir)


if __name__ == "__main__":
    main()

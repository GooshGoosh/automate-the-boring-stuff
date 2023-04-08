#!/usr/bin/env python3

# backupToZip.py - Copies an entire folder and its contents into 
# a ZIP file with the current date appended.
# Takes a single command-line argument in the form of the 
# path of the folder that the user wants to back up.


import zipfile
import os
import datetime
import sys


def main():
    # Ensure there is only one command-line argument given.
    if len(sys.argv) != 2:
        print('\nUsage: backupToZip </path/to/folder>')
        sys.exit(1)

    # Get the current date in MM/DD/YYYY format.
    today = datetime.date.today()
    formatToday = today.strftime("-%m-%d-%Y")

    # Back up the entire contents of the given folder into a ZIP file.
    folder = os.path.abspath(sys.argv[1])   # Ensure folder is absolute
    parentDir = os.path.dirname(folder)
    zipFilename = os.path.join(parentDir, os.path.basename(folder)) + formatToday + '.zip'

    # Ensure the folder exists.
    if not os.path.exists(folder):
        print('\nFolder "{}" does not exist!'.format(folder))
        sys.exit(1)

    # Check if there is already a ZIP backup saved for the same date.
    if os.path.exists(folder + formatToday):
        print('\nBackup ZIP of "{}" for {} already exists!'.format(folder, formatToday))
        sys.exit(1)

    # Create the ZIP file.
    print('\nCreating {}...'.format(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue    # Don't back up the backup ZIP files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


if __name__ == "__main__":
    main()


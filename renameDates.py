#!/usr/bin/env python3

# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY


# import shutil
import os
import re


def rename_dates():
    # Create a regex that matches files with the American date format.
    datePattern = re.compile(r"""^(.*?)     # All text before the date
        ((0|1)?\d)-                         # One or two digits for the month
        ((0|1|2|3)?\d)-                     # One or two digits for the day
        ((19|20)\d\d)                       # Four digits for the year
        (.*?)$                              # All text after the date
        """, re.VERBOSE)

    # Loop over the files in the working directory.
    for amerFilename in os.listdir('.'):
        mo = datePattern.search(amerFilename)

        # Skip files without a date.
        if mo == None:
            continue

        # Get the different parts of the filename.
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

        # Form the European-style filename.
        euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

        # Get the full, absolute file paths.
        absWorkingDir = os.path.abspath('.')
        amerFilename = os.path.join(absWorkingDir, amerFilename)
        euroFilename = os.path.join(absWorkingDir, euroFilename)

        # Rename the files.
        print(f'\nRenaming "{amerFilename}" to "{euroFilename}"...')
        # shutil.move(amerFilename, euroFilename)   # Uncomment after testing.


def main():
    rename_dates()


if __name__ == "__main__":
    main()


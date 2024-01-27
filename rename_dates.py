'''
Chapter 10 Project: Renaming Files with American-Style Dates to
European-Style Dates

rename_dates.py - Rename filenames with American MM-DD-YYYY date format to
European DD-MM-YYYY date format.
'''


#import shutil
import os
import re


def rename_dates():
    """Searches for American-Style dates in filenames and converts them into
    European-Style dates.
    """
    # Create a regex that matches files with the American date format.
    date_pattern = re.compile(r"""^(.*?)            # All text before the date
                             ((0|1)?\d)-            # One or two digits for the month
                             ((0|1|2|3)?\d)-        # One or two digits for the day
                             ((19|20)\d\d)          # Four digits for the year
                             (.*?)$                 # All text after the date
                             """, re.VERBOSE)

    # Loop over the files in the working directory.
    for amer_filename in os.listdir('.'):
        mo = date_pattern.search(amer_filename)

        # Skip files without a date.
        if mo is None:
            continue

        # Get the different parts of the filename.
        before_part = mo.group(1)
        month_part = mo.group(2)
        day_part = mo.group(4)
        year_part = mo.group(6)
        after_part = mo.group(8)

        # Form the European-style filename.
        euro_filename = before_part + day_part + '-' + month_part + '-' + year_part + after_part

        # Get the full, absolute file paths.
        abs_working_dir = os.path.abspath('.')
        amer_filename = os.path.join(abs_working_dir, amer_filename)
        euro_filename = os.path.join(abs_working_dir, euro_filename)

        # Rename the files.
        print(f'\nRenaming "{amer_filename}" to "{euro_filename}"...')
        # shutil.move(amer_filename, euro_filename)   # Uncomment after testing.


def main():
    """Main function to run the program.
    """
    rename_dates()


if __name__ == "__main__":
    main()

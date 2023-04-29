#!/usr/bin/env python3

# blankRowInserter.py - Takes two integers and a filename string as command-line
# arguments. The first integer (N) is the starting row and the second integer (M)
# is the number of blank rows to insert. The filename should be the path to
# a spreadsheet file. Example: blankRowInserter.py 3 5 /path/to/spreadsheet will
# insert 5 blank rows starting with row 3 in the spreadsheet located at the 
# /path/to/spreadsheet destination.


import openpyxl
import sys
from pathlib import Path


def insert_blank_rows(N, M, spreadsheetFile):
    validExtensions = ['.xlsx', '.xlsm', '.xltx', '.xltm']  # List of valid Excel extensions.

    # Set the path of the spreadsheet and ensure it exists.
    spreadsheet = Path(spreadsheetFile)
    if not spreadsheet.exists():
        print('\nFile path {} does not exist!\nExiting...'.format(spreadsheet))
        sys.exit(1)
    elif not spreadsheet.is_file():
        print('\nThe path {} is not a file!\nExiting...'.format(spreadsheet))
        sys.exit(1)
    elif spreadsheet.suffix not in validExtensions:
        print('\nFile {} is not a valid spreadsheet file!\nExiting...'.format(spreadsheet.name))
        sys.exit(1)


def main():
    if len(sys.argv) != 4:
        print('\nUsage: blankRowInserter.py <integer> <integer> <path/to/spreadsheet')
        sys.exit(1)

    startingRow = sys.argv[1]
    rowsToAdd = sys.argv[2]
    spreadsheet = sys.argv[3]

    insert_blank_rows(startingRow, rowsToAdd, spreadsheet)


if __name__ == "__main__":
    main()


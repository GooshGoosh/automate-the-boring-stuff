'''
Chapter 13 Project: Blank Row Inserter

blank_row_inserter.py - Takes two integers and a filename string as command line
arguments. The first integer (starting_row) is the starting row and the second
integer (rows_to_add) is the number of blank rows to insert. The filename should
be the path to a spreadsheet file.

Example: blankrow_inserter.py 3 5 /path/to/spreadsheet will insert 5 blank rows
starting with row 3 in the spreadsheet located at the /path/to/spreadsheet destination.
'''


import sys
from pathlib import Path
import openpyxl


def insert_blank_rows(starting_row, rows_to_add, spreadsheet_file):
    """Inserts blank rows into the given spreadsheet file. The blank rows start
    at the given starting row and ends after the given number of rows to add has
    been added to the file.

    Args:
        starting_row (int): The row in the file to start the blank rows.
        rows_to_add (int): The number of blank rows to add to the file.
        spreadsheet_file (str): Path to the spreadsheet file to add blank rows to.
    """
    # List of valid Excel extensions.
    valid_ext = ['.xlsx', '.xlsm', '.xltx', '.xltm']

    # Set the path of the spreadsheet and ensure it exists.
    spreadsheet = Path(spreadsheet_file)
    if not spreadsheet.exists():
        print(f'\nFile path {spreadsheet} does not exist!\nExiting...')
        sys.exit(1)
    elif not spreadsheet.is_file():
        print(f'\nThe path {spreadsheet} is not a file!\nExiting...')
        sys.exit(1)
    elif spreadsheet.suffix not in valid_ext:
        print(f'\nFile {spreadsheet.name} is not a valid spreadsheet file!\nExiting...')
        sys.exit(1)

    print('\nLoading workbook...')
    wb = openpyxl.load_workbook(spreadsheet)
    sheet = wb.active
    print(f'Inserting {rows_to_add} blank rows at row {starting_row}...')
    sheet.insert_rows(starting_row, amount=rows_to_add)

    parent_path = spreadsheet.parent                # Set the parent path.
    filename = str(spreadsheet.stem)                # Get the basename of the spreadsheet.
    new_filename = filename + '-inserted-rows.xlsx' # Create new filename for spreadsheet.
    wb.save(parent_path / new_filename)

    print('Done!')
    print(f'File saved as {new_filename} in {parent_path}')


def main():
    """Main function to run the program.
    """
    # Ensure the correct number of command line arguments.
    if len(sys.argv) != 4:
        print('\nUsage: blankRowInserter.py <integer> <integer> <path/to/spreadsheet')
        sys.exit(1)

    try:
        starting_row = int(sys.argv[1])
        rows_to_add = int(sys.argv[2])
        spreadsheet = sys.argv[3]
        insert_blank_rows(starting_row, rows_to_add, spreadsheet)
    except ValueError:
        print('\nPlease enter a whole number (integer) for the first two arguments...')
        print('Exiting...')
        sys.exit(1)


if __name__ == "__main__":
    main()

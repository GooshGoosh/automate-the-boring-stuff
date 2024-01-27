'''
Chapter 13 Project: Text Files to Spreadsheet

text_to_spreadsheet.py - Takes multiple text files as command line arguments
as well as a final argument for the name of the spreadsheet file that
is created. The text files are read line-by-line and are placed into the
spreadsheet where each file is in a separate column and each line from
the file is placed into each row.
'''


import sys
import openpyxl


def read_text_files(list_of_files):
    """Reads the data for a given list of text files.

    Args:
        list_of_files (list): List of files to read the data from.

    Returns:
        dict: Dictionary of data from each of the given text files.
    """
    file_lines = {}  # Dictionary to hold the lines for each file.

    # Loop through the lines in each file and add the list of file lines
    # to the file_lines dictionary.
    for text_file in list_of_files:
        with open(text_file, 'r', encoding='UTF-8') as file:
            lines = file.readlines()
            file_lines[text_file] = lines

    return file_lines


def write_spreadsheet(dict_of_lines, spreadsheet_name):
    """Writes the data from the given dictionary to the given spreadsheet.

    Args:
        dict_of_lines (dict): Dictionary of data from lines of text files.
        spreadsheet_name (str): New filename to save the text file data into.
    """
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']

    print('\nWriting text files to spreadhseet...')
    # Loop through the dictionary to get the column for the spreadsheet.
    for i in range(1, (len(dict_of_lines.keys()) + 1)):
        # Loop through the lines in each dictionary value and add them
        # to the spreadsheet.
        for j in range(len(dict_of_lines[i-1])):
            sheet.cell(row=j+1, column=i).value = str(dict_of_lines[i-1][j]).strip()

    print(f'Saving spreadsheet as {spreadsheet_name}')
    wb.save(spreadsheet_name)


def main():
    """Main function to run the program.
    """
    if len(sys.argv) < 3:
        print('\nUsage: textToSpreadsheet.py <text files> <spreadsheet name>')
        sys.exit(1)

    files = [sys.argv[i] for i in range(1, (len(sys.argv) - 1))]
    spreadsheet = sys.argv[-1]
    file_lines = read_text_files(files)
    write_spreadsheet(file_lines, spreadsheet)


if __name__ == "__main__":
    main()

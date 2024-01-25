#!/usr/bin/env python3

# textToSpreadsheet.py - Takes multiple text files as command-line arguments
# as well as a final argument for the name of the spreadsheet file that
# is created. The text files are read line-by-line and are placed into the
# spreadsheet where each file is in a separate column and each line from
# the file is placed into each row.


import openpyxl
import sys


def read_text_files(listOfFiles):
    fileLines = {}  # Dictionary to hold the lines for each file.

    # Loop through the lines in each file and add the list of file lines
    # to the fileLines dictionary.
    for i in range(len(listOfFiles)):
        with open(listOfFiles[i]) as file:
            lines = file.readlines()
            fileLines[i] = lines
            file.close()

    return fileLines


def write_spreadsheet(dictOfLines, spreadsheetName):
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']

    print('\nWriting text files to spreadhseet...')
    # Loop through the dictionary to get the column for the spreadsheet.
    for i in range(1, (len(dictOfLines.keys()) + 1)):
        # Loop through the lines in each dictionary value and add them
        # to the spreadsheet.
        for j in range(len(dictOfLines[i-1])):
            sheet.cell(row=j+1, column=i).value = str(dictOfLines[i-1][j]).strip()

    print('Saving spreadsheet as {}'.format(spreadsheetName))
    wb.save(spreadsheetName)


def main():
    if len(sys.argv) < 3:
        print('\nUsage: textToSpreadsheet.py <text files> <spreadsheet name>')
        sys.exit(1)

    files = [sys.argv[i] for i in range(1, (len(sys.argv) - 1))]
    spreadsheet = sys.argv[-1]
    fileLines = read_text_files(files)
    write_spreadsheet(fileLines, spreadsheet)


if __name__ == "__main__":
    main()


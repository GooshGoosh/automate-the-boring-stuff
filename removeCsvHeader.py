#!/usr/bin/env python3

# removeCsvHeader.py - Finds all the CSV files in the current working directory
# and write all the contents of each file, skipping the first line, to a new
# CSV file.


import csv
import os


def main():
    os.makedirs('header-removed', exist_ok=True)   # Create a new directory.

    # Loop through every file in the current working directoru.
    for csvFilename in os.listdir('.'):
        if not csvFilename.endswith('.csv'):
            continue    # Skip non-csv files.

        print('Removing header from {}...'.format(csvFilename))

        # Read the CSV file in (skipping first row).
        csvRows = []
        csvFileObj = open(csvFilename)
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue    # Skip the first row.
            csvRows.append(row)
        csvFileObj.close()

        # Write out the CSV file.
        csvFileObj = open(os.path.join('header-removed', csvFilename), 'w',
                         newline='')
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()

if __name__ == "__main__":
    main()


'''
Chapter 16 Project: Removing the Header from CSV Files

remove_csv_header.py - Finds all the CSV files in the current working directory
and writes all the contents of each file, skipping the first line, to a new
CSV file.
'''


import csv
import os


def main():
    """Main function to run the program.
    """
    # Create a new directory.
    os.makedirs('automate-online-materials/header-removed', exist_ok=True)

    # Loop through every file in the current working directoru.
    for csv_filename in os.listdir('.'):
        if not csv_filename.endswith('.csv'):
            continue    # Skip non-csv files.

        print(f'Removing header from {csv_filename}...')

        # Read the CSV file in (skipping first row).
        csv_rows = []
        with open(csv_filename, 'r', encoding='UTF-8') as csv_file_obj:
            reader_obj = csv.reader(csv_file_obj)
            for row in reader_obj:
                if reader_obj.line_num == 1:
                    continue    # Skip the first row.
                csv_rows.append(row)

        # Write out the CSV file.
        with open(os.path.join('header-removed', csv_filename), 'w',
                  encoding='UTF-8', newline='',) as csv_file_obj:
            csv_writer = csv.writer(csv_file_obj)
            for row in csv_rows:
                csv_writer.writerow(row)


if __name__ == "__main__":
    main()

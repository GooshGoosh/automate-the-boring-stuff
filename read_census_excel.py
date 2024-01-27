'''
Chapter  13 Project: Reading Data from a Spreadsheet

read_census_excel.py - Tabulates population and number of census tracts for each county.
'''


import pprint
import openpyxl


def read_census(census):
    """Reads an Excel file filled with Census data and outputs it to a Python file.

    Args:
        census (str): Path to an Excel file.
    """
    print('\nOpening workbook...')
    wb = openpyxl.load_workbook(census)
    sheet = wb['Population by Census Tract']
    county_data = {}

    # Fill in county_data with each county's population and tracts.
    print('Reading rows...')
    for row in range(2, sheet.max_row + 1):
        # Each row in the spreadsheet has data for one census tract.
        state = sheet['B' + str(row)].value
        county = sheet['C' + str(row)].value
        pop = sheet['D' + str(row)].value

        # Make sure the key for this state exists.
        county_data.setdefault(state, {})
        # Make sure the key for this county exists.
        county_data[state].setdefault(county, {'tracts': 0, 'pop': 0})

        # Each row represents one census tract, so increment by one.
        county_data[state][county]['tracts'] += 1
        # Increase the county pop by the pop in this census tract.
        county_data[state][county]['pop'] += int(pop)

    # Open a new text file and write the contents of county_data to it.
    print('Writing results...')
    with open('automate-online-materials/census2010.py', 'w', encoding='UTF-8') as result_file:
        result_file.write('all_data = ' + pprint.pformat(county_data))
    print('Done.')


def main():
    """Main function to run the program.
    """
    census_file = 'automate-online-materials/censuspopdata.xlsx'
    read_census(census_file)


if __name__ == "__main__":
    main()

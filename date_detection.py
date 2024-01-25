'''
Chapter 7 Project: Date Detection

date_detection.py - Takes content stored in the clipboard and detects any dates 
in the DD/MM/YYYY format that are stored in the clipboard. The program then
determines if the dates detected are valid or invalid dates.

April, June, September, and November have 30 days, February has 28 days, and
the rest of the months have 31 days. February has 29 days in leap years.
Leap years are years divisible by 4, except years evenly divisible by 100, unless
the year is also evenly divisible by 400.
'''




import re
import pyperclip


def detect_dates(clipboard_text):
    """Detects dates in the format DD/MM/YYYY in text that is copied to the clipboard.

    Args:
        clipboard_text (str): Text to find dates in.

    Returns:
        list: List of dates found in the given text.
    """
    # A regex to detect dates from content pulled from clipboard.
    date_regex = re.compile(r'''
                           (\d{2})?     # Day of month
                           (/)         # Separator
                           (\d{2})?     # Month
                           (/)         # Separator
                           (\d{4})?     # Year
                           ''', re.VERBOSE)

    matches = []
    for groups in date_regex.findall(clipboard_text):
        date = groups[0], groups[2], groups[4]
        matches.append(date)

    return matches


def check_dates(dates):
    """Checks the given dates to see if they are valid dates.

    Args:
        dates (list): List of dates to validate.

    Returns:
        list, list: A list of valid dates and a list of invalid dates
    """
    valid_dates = []
    invalid_dates = []

    # Valid days for February.
    twenty_eight_days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                         '21', '22', '23', '24', '25', '26', '27', '28']

    # Valid days for April, June, September, November.
    thirty_days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                   '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

    # Valid days for January, March, May, July, August, October, December.
    thirty_one_days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                       '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    # Valid dates for a month.
    months = {'01':thirty_one_days, '02':twenty_eight_days, '03':thirty_one_days,
              '04':thirty_days, '05':thirty_one_days, '06':thirty_days,
              '07':thirty_one_days, '08':thirty_one_days, '09':thirty_days,
              '10':thirty_one_days, '11':thirty_days, '12':thirty_one_days}



    # Loop through the dates found with the regex.
    for date in dates:
        day = date[0]
        month = date[1]
        year = int(date[2])

        # Check if the date is the extra day for the Leap Year.
        if month == '02' and day == '29':
            if check_leap_year(year):
                valid_dates.append('/'.join(date) + ' (Leap Year)')
                continue
            else:
                invalid_dates.append('/'.join(date))
                continue

        # Check if the month date is a valid month.
        if month not in months:
            if check_leap_year(year):
                invalid_dates.append('/'.join(date) + ' (Leap Year)')
                continue
            else:
                invalid_dates.append('/'.join(date))
                continue

        # Check if the day date is a valid day in the given month.
        if day not in months[month]:
            if check_leap_year(year):
                invalid_dates.append('/'.join(date) + ' (Leap Year)')
                continue
            else:
                invalid_dates.append('/'.join(date))
                continue

        # Check if the date year is valid and if it is a Leap Year.
        if year > 999 and year < 3000:
            if check_leap_year(year):
                valid_dates.append('/'.join(date) + ' (Leap Year)')
            else:
                valid_dates.append('/'.join(date))
        else:
            invalid_dates.append('/'.join(date))

    return valid_dates, invalid_dates


def check_leap_year(year):
    """Checks if the given year is a leap year.

    Args:
        year (int): The year to check for a leap year.

    Returns:
        bool: Returns whether or not the year is a leap year.
    """
    if year % 4 != 0:
        return False

    if year % 100 == 0 and year % 400 != 0:
        return False

    return True


def main():
    """Main function to run the program.
    """
    text = str(pyperclip.paste())
    date_list = detect_dates(text)
    valid, invalid = check_dates(date_list)

    print('\nFormat: DD/MM/YYYY')
    print('\nValid Dates:\n')
    for date in valid:
        print(date)

    print('\nInvalid Dates:\n')
    for date in invalid:
        print(date)


if __name__ == "__main__":
    main()

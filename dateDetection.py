#!/usr/bin/env python3

# dateDetection.py - Takes content stored in the clipboard and detects any
# dates in the DD/MM/YYYY format that are stored in the clipboard. The program
# then determines if the dates detected are valid or invalid dates.
#
# April, June, September, and November have 30 days, February has 28 days, and
# the rest of the months have 31 days. February has 29 days in leap years.
# Leap years are years divisible by 4, except years evenly divisible by 100, unless
# the year is also evenly divisible by 400.


import re
import pyperclip


def detect_dates(clipboardText):
    # A regex to detect dates from content pulled from clipboard.
    dateRegex = re.compile(r'''
                           (\d{2})?     # Day of month
                           (/)         # Separator
                           (\d{2})?     # Month
                           (/)         # Separator
                           (\d{4})?     # Year
                           ''', re.VERBOSE)

    matches = []
    for groups in dateRegex.findall(clipboardText):
        date = groups[0], groups[2], groups[4]
        matches.append(date)

    return matches 


def check_dates(dates):
    # Code to check if the found dates are valid or invalid.
    validDates = []     # A list to hold all valid dates found.
    invalidDates = []   # A list to hold all invalid dates found.

    # Valid days for February.
    twentyEightDays = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                       '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                       '21', '22', '23', '24', '25', '26', '27', '28']
    
    # Valid days for April, June, September, November.
    thirtyDays = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                 '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                 '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']

    # Valid days for January, March, May, July, August, October, December.
    thirtyOneDays = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                     '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                     '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

    # Valid dates for a month.
    months = {'01':thirtyOneDays, '02':twentyEightDays, '03':thirtyOneDays,
              '04':thirtyDays, '05':thirtyOneDays, '06':thirtyDays,
              '07':thirtyOneDays, '08':thirtyOneDays, '09':thirtyDays,
              '10':thirtyOneDays, '11':thirtyDays, '12':thirtyOneDays}

    
    
    # Loop through the dates found with the regex.
    for date in dates:
        day = date[0]
        month = date[1]
        year = int(date[2])

        # Check if the date is the extra day for the Leap Year.
        if month == '02' and day == '29':
            if check_leap_year(year):
                validDates.append('/'.join(date) + ' (Leap Year)')
                continue
            else:
                invalidDates.append('/'.join(date))
                continue

        # Check if the month date is a valid month.
        if month not in months:
            if check_leap_year(year):
                invalidDates.append('/'.join(date) + ' (Leap Year)')
                continue
            else:
                invalidDates.append('/'.join(date))
                continue

        # Check if the day date is a valid day in the given month.
        if day not in months[month]:
            if check_leap_year(year):
                invalidDates.append('/'.join(date) + ' (Leap Year)')
                continue
            else:
                invalidDates.append('/'.join(date))
                continue

        # Check if the date year is valid and if it is a Leap Year.
        if year > 999 and year < 3000:
            if check_leap_year(year):
                validDates.append('/'.join(date) + ' (Leap Year)')
            else:
                validDates.append('/'.join(date))
        else:
            invalidDates.append('/'.join(date))

    return validDates, invalidDates


def check_leap_year(year):
    if year % 4 != 0:
        return False

    if year % 100 == 0 and year % 400 != 0:
        return False

    return True


def main():
    text = str(pyperclip.paste())
    dateList = detect_dates(text)
    valid, invalid = check_dates(dateList)

    print('\nFormat: DD/MM/YYYY')
    print('\nValid Dates:\n')
    for date in valid:
        print(date)

    print('\nInvalid Dates:\n')
    for date in invalid:
        print(date)
    

if __name__ == "__main__":
    main()


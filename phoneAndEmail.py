#!/usr/bin/env python3

# phoneAndEmail.py - Fidns phone numbers and email addresses on the clipboard.

import pyperclip
import re


def find_phone_and_email(text):
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # Area code
        (\s|-|\.)?                      # Separator
        (\d{3})                         # First 3 digits
        (\s|-|\.)                       # Separator
        (\d{4})                         # Last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
        )''', re.VERBOSE)

    # Create email regex:
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # Username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # Domain name
        (\.[a-zA-Z]{2,4})   # Dot-something
        )''', re.VERBOSE)

    # Find matches in clipboard text:
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    # Copy Results to the clipboard:
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


def main():
    # Grab text from clipboard.
    clipText = str(pyperclip.paste())

    find_phone_and_email(clipText)


if __name__ == "__main__":
    main()


'''
Chapter 7 Project: Phone Number and Email Address Extractor

phone_and_email.py - Finds phone numbers and email addresses on the clipboard.
'''


import re
import pyperclip


def find_phone_and_email(text):
    """Finds phone numbers and email addresses in the text that is in the clipboard.
    Any found phone numbers and email addresses are copied to the clipboard when the
    program is finished.

    Args:
        text (str): The text to search through to find phone numbers and emails.
    """
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # Area code
        (\s|-|\.)?                      # Separator
        (\d{3})                         # First 3 digits
        (\s|-|\.)                       # Separator
        (\d{4})                         # Last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
        )''', re.VERBOSE)

    # Create email regex:
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # Username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # Domain name
        (\.[a-zA-Z]{2,4})   # Dot-something
        )''', re.VERBOSE)

    # Find matches in clipboard text:
    matches = []
    for groups in phone_regex.findall(text):
        phone_num = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phone_num += ' x' + groups[8]
        matches.append(phone_num)

    for groups in email_regex.findall(text):
        matches.append(groups[0])

    # Copy Results to the clipboard:
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')


def main():
    """Main function to run the program.
    """
    # Grab text from clipboard.
    clip_text = str(pyperclip.paste())

    find_phone_and_email(clip_text)


if __name__ == "__main__":
    main()

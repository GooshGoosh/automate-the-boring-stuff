#!/usr/bin/env python3

# strongPasswordCheck.py - Takes input from the user and checks if the input
# given would make a strong password. A strong password contains at least eight
# characters, both uppercase and lowercase characters, and has at least one digit.


import re


def check_password(password):
    uppercaseRegex = re.compile(r'''[A-Z]+''')
    lowercaseRegex = re.compile(r'''[a-z]+''')
    digitRegex = re.compile(r'''\d+''')

    if len(password) < 8:
        return '\nPassword too short!'

    if not uppercaseRegex.search(password):
        return '\nNo uppercase characters!'

    if not lowercaseRegex.search(password):
        return '\nNo lowercase characters!'

    if not digitRegex.search(password):
        return '\nNo digit characters!'

    return '\nThis is a strong password!'


def main():
    text = input('\nPlease input a password: ')
    print(check_password(text))


if __name__ == "__main__":
    main()


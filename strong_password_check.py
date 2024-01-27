'''
Chapter 7 Project: Strong Password Detection

strong_password_check.py Takes input from the user and checks if the input given
would make a strong password. A strong password contains at least eight characters,
both uppercase and lowercase characters, and has at least one digit.
'''


import re


def check_password(password):
    """Checks if the given password would make a strong password.

    Args:
        password (str): The password to check for strength.

    Returns:
        str: Returns a statement if the password is strong or not.
    """
    uppercase_regex = re.compile(r'''[A-Z]+''')
    lowercase_regex = re.compile(r'''[a-z]+''')
    digit_regex = re.compile(r'''\d+''')

    if len(password) < 8:
        return '\nPassword too short!'

    if not uppercase_regex.search(password):
        return '\nNo uppercase characters!'

    if not lowercase_regex.search(password):
        return '\nNo lowercase characters!'

    if not digit_regex.search(password):
        return '\nNo digit characters!'

    return '\nThis is a strong password!'


def main():
    """Main function to run the program.
    """
    text = input('\nPlease input a password: ')
    print(check_password(text))


if __name__ == "__main__":
    main()

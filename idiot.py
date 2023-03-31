#!/usr/bin/env python3

# idiot.py - Keeps an idiot busy for hours.


import pyinputplus as pyip


def main():
    while True:
        prompt = '\nWant to know how to keep an idiot busy for hours?\n'
        response = pyip.inputYesNo(prompt)

        if response == 'no':
            break

    print('\nThank you! Have a nice day!')


if __name__ == "__main__":
    main()


#!/usr/bin/env python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip


def main():
    text = pyperclip.paste()

    # Separate lines and add stars.
    lines = text.split('\n')
    for i in range(len(lines)):     # Loop through all indexes in the "lines" list.
        lines[i] = '* ' + lines[i]  # Add a start to each string in the "lines" list.

    text = '\n'.join(lines)     # Add the lines together with a newline character.
    pyperclip.copy(text)

    print('\nBullet points added!')


if __name__ == "__main__":
    main()


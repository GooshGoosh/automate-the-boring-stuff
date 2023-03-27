#!/usr/bin/env python3

# mclip.py - A mulit-clipboard program.


import sys
import pyperclip


def main():
    text = {'agree': """Yes, I agree. That sounds fine to me.""",
            'busy': """Sorry, can we do this later this week or next week?""",
            'upsell': """Would you consider making this a monthly donation?"""}

    if len(sys.argv) < 2:
        print('Usage: py mclip.py [keyphrase] - copy phrase text')
        sys.exit()

    keyphrase = sys.argv[1]     # The first command line arg is the keyphrase.

    if keyphrase in text:
        pyperclip.copy(text[keyphrase])
        print("Text for '{}' copied to clipboard".format(keyphrase))
    else:
        print("There is no text for '{}'".format(keyphrase))


if __name__ == "__main__":
    main()


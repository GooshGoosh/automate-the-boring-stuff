'''
Chapter 6 Project: Multi-Clipboard Automatic Messages

mclip.py - A multi-clipboard program. Copies an automatic message to the clipboard
based on a keyphrase given at the command line.
'''


import sys
import pyperclip


def copy_keyphrase(keyphrase):
    """Copy text to the clipboard based on the keyphrase given.
    
    Args:
        keyphrase (str): Key for an automatic message in the dictionary.
    """
    text = {'agree': """Yes, I agree. That sounds fine to me.""",
            'busy': """Sorry, can we do this later this week or next week?""",
            'upsell': """Would you consider making this a monthly donation?"""}

    if keyphrase in text:
        pyperclip.copy(text[keyphrase])
        print(f"Text for '{keyphrase}' copied to clipboard")
    else:
        print(f"There is no text for '{keyphrase}'")


def main():
    """Main function to run the program.
    """
    if len(sys.argv) < 2:
        print('Usage: mclip.py [keyphrase] - copy phrase text')
        sys.exit(1)

    phrase = sys.argv[1]
    copy_keyphrase(phrase)


if __name__ == "__main__":
    main()

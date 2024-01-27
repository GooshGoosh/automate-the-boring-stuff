'''
Chapter 9 Project: Updatable Multi-Clipboard

mcb.pyw - Saves and loads pieces of text to the clipboard.

Usage: mcb.pyw save <keyword> - Saves clipboard to keyword.
       mcb.pyw <keyword> - Loads keyword to clipboard.
       mcb.pyw list - Loads all keywords to clipboard.
       mcb.pyw delete <keyword> - Deletes keyword.
       mcb.pyw delete - Deletes all keywords.
'''


import sys
import shelve
import pyperclip


def main():
    """Main function to run the program.
    """
    mcb_shelf = shelve.open('mcb')

    # Save clipboard content.
    if len(sys.argv) == 3 and sys.argv[1].lower() =='save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # Delete keyword from shelf file.
    elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
        del mcb_shelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        # List keywords and load content.
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcb_shelf.keys())))
        elif sys.argv[1] in mcb_shelf:
            pyperclip.copy(mcb_shelf[sys.argv[1]])
    else:
        print('\nUsage:\n\
              mcb.pyw save <keyword> - Saves clipboard to keyword.\n\
              mcb.pyw <keyword> - Loads keyword to clipboard.\n\
              mcb.pyw list - Loads all keywords to clipboard.\n\
              mcb.pyw delete <keyword> - Deletes keyword.\n')

    mcb_shelf.close()


if __name__ == "__main__":
    main()

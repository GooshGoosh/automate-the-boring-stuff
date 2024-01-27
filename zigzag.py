'''
Chapter 3 Project: Zigzag

zigzag.py - Creates a small back-and-forth, zigzag pattern on the screen until
the user stops the program.
'''

import time
import sys

def main():
    """The main function to run the program.
    """
    indent = 0      # How many spaces to indent.
    indent_increasing = True     # Whether the indentation is increasing is not.

    try:
        while True:     # The main program loop.
            print(' ' * indent, end='')
            print('********')
            time.sleep(0.1)     # Pause for 1/10 of a second.

            if indent_increasing:
                # Increase the number of spaces:
                indent = indent + 1
                if indent == 20:
                    # Change direction:
                    indent_increasing = False
            else:
                # Decrease the number of spaces:
                indent = indent - 1
                if indent == 0:
                    # Change direction:
                    indent_increasing = True
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()

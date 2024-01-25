'''
Chapter 6 Project: Adding Bullets to Wiki Markup

bullet_point_adder.py - Adds Wikipedia bullet points to the start of each line
of text on the clipboard.
'''


import pyperclip


def add_bullet_point(text):
    """Adds bullet points (*) to the beginning of each line in the given text.

    Args:
        text (str): Lines of text to add bullet points (*) to.
    """
    # Separate lines and add stars to each line in the list.
    lines = text.split('\n')
    for i, line in enumerate(lines):
        lines[i] = '* ' + line

    text = '\n'.join(lines)
    pyperclip.copy(text)

    print('\nBullet points added!')


def main():
    """Main function to run the program.
    """
    clip_text = pyperclip.paste()
    add_bullet_point(clip_text)


if __name__ == "__main__":
    main()

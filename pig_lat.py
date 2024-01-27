'''
Chapter 6 Project: Pig Latin

pig_lat.py - Takes a message from the user and translates the message into
Pig Latin.
'''


def pig_latin(text):
    """Translates a given message into Pig Latin.

    Args:
        text (str): The message to be translated into Pig Latin.
    """
    vowels = ('a', 'e', 'i', 'o', 'u', 'y')

    pig_latin_text = []   # A list of the words in Pig Latin.

    for word in text.split():
        # Separate the non-letters at the start of the word:
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]

        if len(word) == 0:
            pig_latin_text.append(prefix_non_letters)
            continue

        # Separate the non-letters at the end of this word:
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters += word[-1]
            word = word[:-1]

        # Remember if the word was in uppercase or title case.
        was_upper = word.isupper()
        was_title = word.istitle()

        word = word.lower() # Make the word lowercase for the translation.

        # Separate the consonants at the start of this word:
        prefix_consonants = ''
        while len(word) > 0 and not word[0] in vowels:
            prefix_consonants += word[0]
            word = word[1:]

        # Add the Pig Latin ending to the word:
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        # Set the word back to uppercase or title case:
        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        # Add the non-letters back to the start or end of the word.
        pig_latin_text.append(prefix_non_letters + word + suffix_non_letters)

    # Join all the words back together into a single string:
    print('\nTranslation: ',end='')
    print(' '.join(pig_latin_text))


def main():
    """Main function to run the program.
    """
    print('\nEnter the English message to translate into Pig Latin: ')
    message = input()

    pig_latin(message)


if __name__ == "__main__":
    main()

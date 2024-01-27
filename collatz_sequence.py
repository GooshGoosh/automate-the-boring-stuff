'''
Chapter 3 Project: The Collatz Sequence

collatz_sequence.py - Performs the Collatz sequence on a given integer.
'''


def collatz(number):
    """Performs the Collatz sequence on the given number.

    Args:
        number (int): The number to perform the Collatz sequence on.

    Returns:
        int: The result of the Collatz sequence.
    """
    if number % 2 == 0:         # If the number is even, then divide
        print(number // 2)      # the number by 2.
        return number // 2
    elif number % 2 == 1:           # If the number is odd, then multiply
        print((3 * number) + 1)     # multiply the number by 3 and then add 1.
        return (3 * number) + 1


def main():
    """The main function to run the program.
    """
    # Get an integer from the user, but print an error message if the user
    # enters anything that is not an integer.
    try:
        num = int(input('\nPlease enter a number: '))
        while num != 1:
            num = collatz(num)
    except ValueError:
        print('\nEnter a number!')


if __name__ == "__main__":
    main()

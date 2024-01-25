'''
Chapter 4 Project: Character Picture Grid

character_picture_grid.py - Outputs a picture using text and nested lists.
'''


def main():
    """Main function to run the program.
    """
    # List of lists containing the characters to print a picture.
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for i in range(6):          # Loop through each space in the inside lists.
        for k in range(9):      # Loop through each list in the list of lists.
            if k == 8:
                # Print a newline at the end of a row of characters.
                print(grid[k][i])
            else:
                # Insert an empty space after every print.
                print(grid[k][i], end='')


if __name__ == "__main__":
    main()

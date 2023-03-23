#!/usr/bin/env python3

def main():
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
                print(grid[k][i])               # Print a newline at the end of a row of characters.
            else:
                print(grid[k][i], end='')       # Insert an empty space after every print.


if __name__ == "__main__":
    main()


'''
Chapter 4 Project: Conway's Game of Life

conway.py - Simulates Conway's Game of Life
'''


import random
import time
import copy
import sys


ROW_WIDTH = 60
COL_HEIGHT = 42


def main():
    """Main function to run the program.
    """
    # Create a list of lists of the cells
    next_cells = []
    for x in range(ROW_WIDTH):
        column = []     # Create a new column.
        for y in range(COL_HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#')  # Add a living cell.
            else:
                column.append(' ')  # Add a dead cell.
        next_cells.append(column)

    # Main program loop.
    while True:
        # Separate each step with newlines.
        print('\n\n\n\n\n')
        current_cells = copy.deepcopy(next_cells)

        # Print current_cells on the screen:
        for y in range(COL_HEIGHT):
            for x in range(ROW_WIDTH):
                print(current_cells[x][y], end='')   # Print the # or space.
            print()

        # Calculate the next step's cells based on current step's cells:
        for x in range(ROW_WIDTH):
            for y in range(COL_HEIGHT):
                # Get neighboring coordinates:
                # '% ROW_WIDTH' ensures left_coord is always between 0 and ROW_WIDTH - 1
                left_coord = (x - 1) % ROW_WIDTH
                right_coord = (x + 1) % ROW_WIDTH
                above_coord = (y - 1) % COL_HEIGHT
                below_coord = (y + 1) % COL_HEIGHT

                # Count number of living neighbors:
                num_neighbors = 0

                if current_cells[left_coord][above_coord] == '#':
                    num_neighbors += 1   # Top-left neighbor is alive.
                if current_cells[x][above_coord] == '#':
                    num_neighbors += 1   # Top neighbor is alive.
                if current_cells[right_coord][above_coord] == '#':
                    num_neighbors += 1   # Top-right neighbor is alive.
                if current_cells[left_coord][y] == '#':
                    num_neighbors += 1   # Left neighbor is alive.
                if current_cells[right_coord][y] == '#':
                    num_neighbors += 1   # Right neighbor is alive.
                if current_cells[left_coord][below_coord] == '#':
                    num_neighbors += 1   # Bottom-left neighbor is alive.
                if current_cells[x][below_coord] == '#':
                    num_neighbors += 1   # Bottom neighbor is alive.
                if current_cells[right_coord][below_coord] == '#':
                    num_neighbors += 1   # Bottom-right neighbor is alive.

                # Set cell based on Conway's Game of Life rules:
                if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    next_cells[x][y] = '#'
                elif current_cells[x][y] == ' ' and num_neighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    next_cells[x][y] = '#'
                else:
                    # Everything else dies or stays dead:
                    next_cells[x][y] = ' '

        # Add a 1-second pause to reduce flickering.
        time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

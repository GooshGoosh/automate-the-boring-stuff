'''
Chapter 6 Project: Table Printer

table_printer.py - Prints a list of lists of strings as a well-organized table
with each column right-justified.
'''

def print_table(table):
    """Prints a given list of lists as a well-organized table with each column
    right-justified.

    Args:
        table (list): List of lists of strings.
    """
    # Find the number of inner lists in the table.
    col_widths = [0] * len(table)

    # Find the longest word in the table to use as the width for the rjust method.
    for i in range(len(col_widths)):
        for j in range(len(table[i])):
            if len(table[i][j]) > col_widths[i]:
                col_widths[i] = len(table[i][j])

    width = max(col_widths)  # Set the width for the rjust method.

    # Loop through the table and print the values at the same index for each inner list.
    for i in range(len(table[0])):
        for j in range(len(table)):
            if j == (len(table) - 1):
                print(table[j][i].rjust(width))
            else:
                print(table[j][i].rjust(width),end='')


def main():
    """Main function to run the program.
    """
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == "__main__":
    main()

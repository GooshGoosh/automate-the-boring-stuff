#!/usr/bin/env python3

def printTable(table):
    # Find the number of inner lists in the table.
    colWidths = [0] * len(table)

    # Find the longest word in the table to use as the width for the rjust method.
    for i in range(len(colWidths)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])

    width = max(colWidths)  # Set the width for the rjust method.

    # Loop through the table and print the values at the same index for each inner list.
    for i in range(len(table[0])):
        for j in range(len(table)):
            if j == (len(table) - 1):
                print(table[j][i].rjust(width))
            else:
                print(table[j][i].rjust(width),end='')


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)


if __name__ == "__main__":
    main()


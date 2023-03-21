#!/usr/bin/env python3

# commaCode.py - A simple function that takes a list value as an argument
# and returns a string with all the items separated by a comma and a
# space, with "and" inserted before the last item.


def comma(list):
    if len(list) == 0:
        return "This list is empty!"
    elif len(list) == 1:
        return list[0]
    else:
        newList = [str(item) for item in list]
        newList[-1] = "and " + newList[-1]
        return ", ".join(newList)


def main():
    zeroList = []
    oneList = ["One"]
    myList = [1, 2, 3, 4, 5]
    longList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15]

    print(comma(zeroList))
    print(comma(oneList))
    print(comma(myList))
    print(comma(longList))

if __name__ == "__main__":
    main()


'''
Chapter 4 Project: Comma Code

comma_code.py - A simple function that takes a list value as an argument
and returns a string with all the items separated by a comma and a space,
with "and" inserted before the last item.
'''


def comma(item_list):
    """Join each item in the given list with a comma and space (, ) with "and"
    inserted before the last item.

    Args:
        item_list (list): List of items to join together.

    Returns:
        list: New list of joined items.
    """
    if len(item_list) == 0:
        return "This list is empty!"
    elif len(item_list) == 1:
        return list[0]
    else:
        # Create a new list and convert each element to a string.
        new_list = [str(item) for item in item_list]
        new_list[-1] = "and " + str(new_list[-1])
        return ", ".join(new_list)


def main():
    """Main function to run the program.
    """
    zero_list = []
    one_list = ["One"]
    sampe_list = [1, 2, 3, 4, 5]
    long_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15]

    print(comma(zero_list))
    print(comma(one_list))
    print(comma(sampe_list))
    print(comma(long_list))

if __name__ == "__main__":
    main()

'''
Chapter 5 Project: Fantasy Game Inventory

inventory.py - Outputs a simulated fantasy game inventory to the screen.
'''

def display_inventory(inventory):
    """Outputs the given dictionary to the screen. Displays the quantity of each
    item in the inventory and the total amount of items in the inventory.

    Args:
        inventory (dict): Dictionary of fantasy game items.
    """
    print("\nInventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print(f'\nTotal number of items: {item_total}')


def add_to_inventory(inventory, added_items):
    """Adds a given list of items to the given dictionary.

    Args:
        inventory (dict): Dictionary of fantasy game items.
        added_items (list): List of fantasy game items to add to the inventory.

    Returns:
        dict: The updated dictionary of fantasy game items.
    """
    print('\nUpdating inventory...')
    for item in added_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def main():
    """Main function to run the program.
    """
    stuff = {'Rope': 1, 'Torch': 6, 'Gold Coin': 42, 'Dagger': 1, 'Arrow': 12}
    dragon_loot = ['Gold Coin', 'Dagger', 'Gold Coin', 'Ruby']

    display_inventory(stuff)

    stuff = add_to_inventory(stuff, dragon_loot)
    display_inventory(stuff)


if __name__ == "__main__":
    main()

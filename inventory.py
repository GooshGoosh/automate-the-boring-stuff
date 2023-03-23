#!/usr/bin/env python3

def display_inventory(inventory):
    print("\nInventory:")
    itemTotal = 0                       # Variable to track the total number of items in the inventory.
    for k, v in inventory.items():      # Loop through the items in the given dictionary
        print("{} {}".format(v, k))     # and print the quantity held followed by the item.
        itemTotal += v                  # Increase the total number of items by the current item quantity.
    print("\nTotal number of items: {}".format(itemTotal))


def add_to_inventory(inventory, addedItems):
    print('\nUpdating inventory...')
    for item in addedItems:                 # Loop through the items in the given list.
        if item in inventory.keys():        # If the current item in the list is already in the dictionary,
            inventory[item] += 1            # then add 1 to the value of the key that matches the current item.
        else:
            inventory[item] = 1     # If the item is not in the dictionary, then add the item to the dictionary.

    return inventory        # Return the updated dictionary.


def main():
    stuff = {'Rope': 1, 'Torch': 6, 'Gold Coin': 42, 'Dagger': 1, 'Arrow': 12}
    dragonLoot = ['Gold Coin', 'Dagger', 'Gold Coin', 'Ruby']

    display_inventory(stuff)
    
    stuff = add_to_inventory(stuff, dragonLoot)
    display_inventory(stuff)


if __name__ == "__main__":
    main()


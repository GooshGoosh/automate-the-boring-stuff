#!/usr/bin/env python3

def display_inventory(inventory):
    print("\nInventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        itemTotal += v
    print("\nTotal number of items: {}".format(itemTotal))


def add_to_inventory(inventory, addedItems):
    print('\nUpdating inventory...')
    for item in addedItems:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory


def main():
    stuff = {'Rope': 1, 'Torch': 6, 'Gold Coin': 42, 'Dagger': 1, 'Arrow': 12}
    dragonLoot = ['Gold Coin', 'Dagger', 'Gold Coin', 'Ruby']

    display_inventory(stuff)
    
    stuff = add_to_inventory(stuff, dragonLoot)
    display_inventory(stuff)


if __name__ == "__main__":
    main()


#!/usr/bin/env python3

def displayInventory(inventory):
    print("\nInventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print("{} {}".format(v, k))
        itemTotal += v
    print("\nTotal number of items: {}".format(itemTotal))


def main():
    stuff = {'Rope': 1, 'Torch': 6, 'Gold Coin': 42, 'Dagger': 1, 'Arrow': 12}

    displayInventory(stuff)


if __name__ == "__main__":
    main()


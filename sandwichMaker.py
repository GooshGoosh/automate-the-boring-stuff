#!/usr/bin/env python3

# sandwichMaker.py - Gives the user several menu options to choose 
# the different components that they would like to add to their sandwich.
# The menu options include: bread type, protein type, cheese, as well
# as various condiments and other additions. The user is then asked how
# many sandwiches they would like with their order.
# A total cost for the order is displayed once the user has placed their order.


import pyinputplus as pyip
import time
import sys


def sandwich_menu():
    breadOptions = {'Wheat':0.50, 'White':0.50, 'Sourdough':1.00}                   # Bread options.
    proteinOptions = {'Chicken':2.00, 'Turkey':2.00, 'Ham':2.00, 'Tofu':1.50}       # Protein options.
    cheeseOptions = {'Cheddar':0.50, 'Swiss':0.75, 'Mozzarella':0.50}               # Cheese options.
    extraOptions = ['Mayo', 'Mustard', 'Lettuce', 'Tomato']                         # Condiments, etc.
    cost = 0

    answer = pyip.inputYesNo(prompt='\nHello, would like you place an order?\n')

    # Exit the program if the user does not want to place an order.
    if answer == 'no':
        print('\nHave a nice day!')
        sys.exit(0)
    else:
        bread = pyip.inputMenu(list(breadOptions.keys()), prompt='\nWhat bread would you like?\n',
                               numbered=True)
        cost = cost + breadOptions[bread]

        protein = pyip.inputMenu(list(proteinOptions.keys()), prompt='\nWhat protein would you like?\n',
                                 numbered=True)
        cost = cost + proteinOptions[protein]

        answer = pyip.inputYesNo(prompt='\nWould you like cheese?\n')
        if answer == 'yes':
            cheese = pyip.inputMenu(list(cheeseOptions.keys()), prompt='\nWhat cheese would you like?\n',
                                    numbered=True)
            cost = cost + cheeseOptions[cheese]
        else:
            cheese = 'None'

        answer = pyip.inputYesNo(prompt='\nWould you like any condiments/extras?\n')
        extras = ''
        if answer == 'yes':
            while answer == 'yes':
                if extras == '':
                    extras = pyip.inputMenu(list(extraOptions), prompt='\nWhat would you like to add?\n',
                                            numbered=True)
                else:
                    extras = extras + ', ' + pyip.inputMenu(list(extraOptions), prompt='\nWhat would you like to add?\n',
                                                            numbered=True)
                answer = pyip.inputYesNo(prompt='\nWould you like to add more?\n')

        sandwichCount = pyip.inputNum(prompt='\nHow many sandwiches would you like to order?\n', min=1)

        print('\nProcessing order...')
        time.sleep(2)

        print('\nYour sandwich:')
        print('Bread: {}'.format(bread))
        print('Protein: {}'.format(protein))
        print('Cheese: {}'.format(cheese))
        print('Extras: {}'.format(extras))
        print('\nNumber of sandwiches: {}'.format(sandwichCount))
        print('Total = ${:.2f}'.format(cost * sandwichCount))
        print('\nThank you! Come again!\n')


def main():
    sandwich_menu()


if __name__ == "__main__":
    main()


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


def main():
    breadOptions = ['Wheat', 'White', 'Sourdough']             # Bread options.
    proteinOptions = ['Chicken', 'Turkey', 'Ham', 'Tofu']      # Protein options.
    cheeseOptions = ['Cheddar', 'Swiss', 'Mozzarella']         # Cheese options.
    extraOptions = ['Mayo', 'Mustard', 'Lettuce', 'Tomato']    # Condiments, etc.

    answer = pyip.inputYesNo(prompt='\nHello, would like you place an order?\n')

    # Exit the program if the user does not want to place an order.
    if answer == 'no':
        print('\nHave a nice day!')
    else:
        bread = pyip.inputMenu(breadOptions, prompt='\nWhat bread would you like?\n',
                               numbered=True)

        protein = pyip.inputMenu(proteinOptions, prompt='\nWhat protein would you like?\n',
                                 numbered=True)

        answer = pyip.inputYesNo(prompt='\nWould you like cheese?\n')
        if answer == 'yes':
            cheese = pyip.inputMenu(cheeseOptions, prompt='\nWhat cheese would you like?\n',
                                    numbered=True)
        else:
            cheese = 'None'

        answer = pyip.inputYesNo(prompt='\nWould you like any condiments/extras?\n')
        extras = ''
        if answer == 'yes':
            while answer == 'yes':
                if extras == '':
                    extras = pyip.inputMenu(extraOptions, prompt='\nWhat would you like to add?\n',
                                             numbered=True)
                else:
                    extras = extras + ', ' + pyip.inputMenu(extraOptions, prompt='\nWhat would you like to add?\n',
                                                   numbered=True)
                answer = pyip.inputYesNo(prompt='\nWould you like to add more?\n')

        sandwichCount = pyip.inputNum(prompt='\nHow many sandwiches would you like to order?\n')

        print('\nProcessing order...')
        time.sleep(2)

        print('Your sandwich:')
        print('Bread: {}'.format(bread))
        print('Protein: {}'.format(protein))
        print('Cheese: {}'.format(cheese))
        print('Extras: {}'.format(extras))
        print('\nNumber of sandwiches: {}'.format(sandwichCount))
        print('\nThank you! Come again!\n')
    


if __name__ == "__main__":
    main()


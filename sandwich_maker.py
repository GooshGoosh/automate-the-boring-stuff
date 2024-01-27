'''
Chapter 8 Project: Sandwich Maker

sandwichMaker.py - Gives the user several menu options to choose 
the different components that they would like to add to their sandwich.
The menu options include: bread type, protein type, cheese, as well
as various condiments and other additions. The user is then asked how
many sandwiches they would like with their order.

A total cost for the order is displayed once the user has placed their order.
'''


import time
import sys
import pyinputplus as pyip


def sandwich_menu():
    """Asks the user if they would like to make a sandwich and, if so, takes them
    through the ingredient selection process to build their sandwich. Prints out
    the user's order and cost once they are finished.
    """
    bread_options = {'Wheat':0.50, 'White':0.50, 'Sourdough':1.00}
    protein_options = {'Chicken':2.00, 'Turkey':2.00, 'Ham':2.00, 'Tofu':1.50}
    cheese_options = {'Cheddar':0.50, 'Swiss':0.75, 'Mozzarella':0.50}
    extra_options = ['Mayo', 'Mustard', 'Lettuce', 'Tomato']
    cost = 0

    answer = pyip.inputYesNo(prompt='\nHello, would like you place an order?\n')

    # Exit the program if the user does not want to place an order.
    if answer == 'no':
        print('\nHave a nice day!')
        sys.exit(0)
    else:
        bread = pyip.inputMenu(list(bread_options.keys()), prompt='\nWhat bread would you like?\n',
                               numbered=True)
        cost = cost + bread_options[bread]

        protein = pyip.inputMenu(list(protein_options.keys()),
                                 prompt='\nWhat protein would you like?\n',
                                 numbered=True)
        cost = cost + protein_options[protein]

        answer = pyip.inputYesNo(prompt='\nWould you like cheese?\n')
        if answer == 'yes':
            cheese = pyip.inputMenu(list(cheese_options.keys()),
                                    prompt='\nWhat cheese would you like?\n',
                                    numbered=True)
            cost = cost + cheese_options[cheese]
        else:
            cheese = 'None'

        answer = pyip.inputYesNo(prompt='\nWould you like any condiments/extras?\n')
        extras = []
        if answer == 'yes':
            while answer == 'yes':
                if not extras:
                    extras.append(pyip.inputMenu(list(extra_options),
                                            prompt='\nWhat would you like to add?\n',
                                            numbered=True))
                else:
                    extras.append(pyip.inputMenu(list(extra_options),
                                                 prompt='\nWhat would you like to add?\n',
                                                 numbered=True))
                answer = pyip.inputYesNo(prompt='\nWould you like to add more?\n')

        sandwich_count = pyip.inputNum(
            prompt='\nHow many sandwiches would you like to order?\n', min=1)

        print('\nProcessing order...')
        time.sleep(2)

        print('\nYour sandwich:')
        print(f'Bread: {bread}')
        print(f'Protein: {protein}')
        print(f'Cheese: {cheese}'.format(cheese))
        print(f'Extras: {", ".join(extras)}')
        print(f'\nNumber of sandwiches: {sandwich_count}')
        print(f'Total = ${cost * sandwich_count:.2f}')
        print('\nThank you! Come again!\n')


def main():
    """Main function to run the program.
    """
    sandwich_menu()


if __name__ == "__main__":
    main()

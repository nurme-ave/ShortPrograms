"""
Simple program to model a banking system.
Author: Ave Nurme
Created on: August 24th, 2020
Pylint: "Your code has been rated at 10.00/10"
Passed the JetBrains Academy automated check.
"""

from random import randint

# store the card number and PIN-code here
store_data = []


def show_main_menu():
    """
    Create the menu as a dictionary.
    Loop over the items for output.
    """
    print()
    menu = {
        1: "Create an account",
        2: "Log into account",
        0: "Exit",
    }

    for key, value in menu.items():
        print(f"{key}. {value}")


def function_call_main_menu():
    """
    Ask for user input.
    Dispatch using a dictionary.
    More info here:
    https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s07.html
    """
    show_main_menu()
    choice = input()

    menu_dict = {
        '1': create_account,
        '2': log_into_account,
        '0': exit_program,
    }

    function_to_call = menu_dict[choice]
    function_to_call()


def create_the_card():
    """
    Create the card by concatenating 'iin' and 'account_identifier.
    For the latter the 'random' library is used to generate the
    rest of the 10 digits.
    Store the number in an array 'store_data' and return it.
    """
    iin = 400000
    account_identifier = randint(1000000000, 9999999999)
    card_nr = f'{iin}{account_identifier}'
    store_data.append(int(card_nr))

    return card_nr


def validate():
    """
    Validate the card number created in 'create_the_card()'.
    Validation is done based on the Luhn algorithm.
    More info here -> https://en.wikipedia.org/wiki/Luhn_algorithm
    """
    card_nr = create_the_card()
    copy_card_nr = int(card_nr)

    # convert the card number into a list of integers
    to_digits = [int(num) for num in str(card_nr)]

    # save the last digit of the list (we're going to need it later)
    last_digit = to_digits[-1]

    # a list comprehension for multiplying odd digits by 2,
    # excluding the last digit
    multiply_odd_digits = [int(num) * 2
                           if i % 2 == 0
                           else int(num)
                           for i, num in enumerate(to_digits[:-1])]

    # a list comprehension for subtracting 9 if the digit is over 9
    subtract_nine = [int(num) - 9
                     if int(num) > 9
                     else int(num)
                     for num in multiply_odd_digits]

    # add all numbers, including the last digit
    sum_all_numbers_incl_last_digit = sum(subtract_nine) + last_digit

    # check if the result is a multiple of 10
    result = sum_all_numbers_incl_last_digit % 10

    # print a message if the number is valid according to the
    # Luhn algorithm or start all over again
    if result == 0:
        print(f"\nYour card has been created\n"
              f"Your card number:\n"
              f"{copy_card_nr}")
    else:
        validate()


def create_pin_code():
    """
    Generate the pin code using the 'random' library.
    Store the number in an array 'store_data' and print it.
    """
    pin_code = randint(1000, 9999)
    store_data.append(pin_code)

    print(f"Your card PIN:\n"
          f"{pin_code}")


def log_into_account():
    """
    Check if the user input conforms with
    the validated card number and generated PIN-code.
    Take action based on the check results.
    """
    ask_card_nr = int(input("\nEnter your card number: \n"))
    ask_pin_code = int(input("Enter your PIN: \n"))

    if ask_card_nr == store_data[-2] and ask_pin_code == store_data[-1]:
        print("\nYou have successfully logged in!")
        function_call_balance_menu()
    elif ask_card_nr != store_data[-2] or ask_pin_code != store_data[-1]:
        print("\nWrong card number or PIN!")
        function_call_main_menu()


def show_balance_menu():
    """
    Create the menu as a dictionary.
    Loop over the items for output.
    """
    print()
    balance_menu = {
        1: "Balance",
        2: "Log out",
        0: "Exit",
    }

    for key, value in balance_menu.items():
        print(f"{key}. {value}")


def function_call_balance_menu():
    """
    Ask for user input.
    Dispatch using a dictionary.
    More info here:
    https://www.oreilly.com/library/view/python-cookbook/0596001673/ch01s07.html
    """
    show_balance_menu()
    choice = input()

    balance_dict = {
        '1': show_balance,
        '2': log_out,
        '0': exit_program,
    }

    function_to_call = balance_dict[choice]
    function_to_call()


def create_account():
    """Create the account."""
    validate()
    create_pin_code()
    function_call_main_menu()


def show_balance():
    """Show the current balance."""
    print("\nBalance: 0")
    function_call_balance_menu()


def log_out():
    """Log out."""
    print("You have successfully logged out!")
    function_call_main_menu()


def exit_program():
    """Exit the program."""
    print("\nBye!")


def main():
    """Run the program."""
    function_call_main_menu()


main()

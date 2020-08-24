"""
Simple program to model a banking system - a project at JetBrains Academy - stage 2 of 4.
Author: Ave Nurme
Created on: August 24th, 2020
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
    main_menu = {
        1: "Create an account",
        2: "Log into account",
        0: "Exit",
    }

    for key, value in main_menu.items():
        print(f"{key}. {value}")


def user_input_before_logging_in():
    """
    Ask for the user input prior to creating an account and logging in.
    Take action based on the user input.
    """
    choice = int(input())

    if choice == 1:
        create_account()
    elif choice == 2:
        log_into_account()
    elif choice == 0:
        exit_program()


def create_the_card():
    """
    Create the card by concatenating 'iin' and 'account_identifier.
    For the latter the 'random' library is used to generate the rest of the 10 digits.
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

    # a list comprehension for multiplying odd digits by 2, excluding the last digit
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

    # print a message if the number is valid according to the Luhn algorithm or start all over again
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
        show_balance_menu()
        user_input_after_logging_in()
    elif ask_card_nr != store_data[-2] or ask_pin_code != store_data[-1]:
        print("\nWrong card number or PIN!")
        show_main_menu()
        user_input_before_logging_in()


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


def user_input_after_logging_in():
    """
    Ask for the user input after logging in.
    Take action based on the user input.
    """
    choice = int(input())

    if choice == 1:
        show_balance()
    elif choice == 2:
        log_out()
    elif choice == 0:
        exit_program()


def create_account():
    """Create the account."""
    validate()
    create_pin_code()
    show_main_menu()
    user_input_before_logging_in()


def show_balance():
    """Show the current balance."""
    print("\nBalance: 0")
    show_balance_menu()
    user_input_after_logging_in()


def log_out():
    """Log out."""
    print("You have successfully logged out!")
    show_main_menu()
    user_input_before_logging_in()


def exit_program():
    """Exit the program."""
    print("\nBye!")


def main():
    """Run the program."""
    show_main_menu()
    user_input_before_logging_in()


main()

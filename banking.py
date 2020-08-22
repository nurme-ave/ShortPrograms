"""
Project at JetBrains Academy - stage 1 of 4.
A program to model a simple banking system.
Passed the JetBrains automated check.
"""

from random import randint


# an array to store the card number and the PIN-code
store_data = []


# show the client the menu of options before logging in
def show_menu():
    print()
    menu = {
        1: "Create an account",
        2: "Log into account",
        0: "Exit",
    }

    for key, value in menu.items():
        print(f"{key}. {value}")


# ask for the user input before logging in
def user_input_before_logging_in():
    choice = int(input())

    if choice == 1:
        create_the_card()
        create_pin_code()
        show_menu()
        user_input_before_logging_in()
    elif choice == 2:
        log_into_account()


# create the card if the client has chosen to create an account
def create_the_card():
    iin = 400000
    account_identifier = randint(100000000, 999999999)
    checksum = 5
    card_nr = f'{iin}{account_identifier}{checksum}'
    store_data.append(int(card_nr))

    print(f"Your card has been created\n"
          f"Your card number:\n"
          f"{card_nr}")


# create the card's PIN code if the client has chosen to create an account    
def create_pin_code():
    pin_code = randint(1000, 9999)
    store_data.append(pin_code)

    print(f"Your card PIN:\n"
          f"{pin_code}")


# check if the client has entered the correct card number and PIN code
def log_into_account():
    ask_card_nr = int(input("Enter card number: "))
    ask_pin_code = int(input("Enter PIN-code: "))

    if ask_card_nr == store_data[0] and ask_pin_code == store_data[1]:
        print("You have successfully logged in!")
        show_balance()
        user_input_after_logging_in()
    elif ask_card_nr != store_data[0] or ask_pin_code != store_data[1]:
        print("Wrong card number or PIN!")
        store_data.clear()
        show_menu()
        user_input_before_logging_in()


# show the client the menu of options after logging in
def user_input_after_logging_in():
    choice = int(input())

    if choice == 1:
        print("Your current balance is 0.")
        user_input_after_logging_in()
    elif choice == 2:
        print("You have successfully logged out!")
    elif choice == 0:
        print()
        print("Bye!")


# show the client the menu of options after logging in
def show_balance():
    print()
    bal_menu = {
        1: "Balance",
        2: "Log out",
        0: "Exit",
    }

    for key, value in bal_menu.items():
        print(f"{key}. {value}")


def main():
    show_menu()
    user_input_before_logging_in()


main()

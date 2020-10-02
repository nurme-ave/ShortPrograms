"""
University of Tartu - Introduction to Programming II (LTAT.TK.001 - 3 EAP) - final project.

This program checks the validity of the user's ID code and returns the result based on user input.
Information on how to check the validity of the ID code can be found here -> https://et.wikipedia.org/wiki/Isikukood
Author: Ave Nurme

EXAMPLE 1 (valid ID-code):

Please type in your name: Ave
Please type in your ID code: [here the user enters his/her ID-code]
{'Ave': '1234567****'}
Good news! -> Your ID code is valid. CSV-file written successfully!

EXAMPLE 2 (invalid ID-code):

Please type in your name: Ave
Please type in your ID code: 12345678912
Invalid ID code or invalid input - no CSV-file written!

"""

name = input("Please type in your name: ").capitalize()  # ask for the user's name and capitalize it
id_code = input("Please type in your ID code: ")  # ask for the user's ID code


def check_your_id(id_code):
    """
    Firstly, check the length of given ID code and if it consists of digits only.
    Secondly, if the first check is passed check the validity of different parts of the ID code.
    Thirdly, if the second check is also passed return the result as a dictionary.
    """

    if len(id_code) == 11 and id_code.isdigit():

        # check if different parts/numbers of the ID code are valid using slicing
        gender_number_validity = check_gender_number(int(id_code[0]))
        year_number_two_digits_validity = check_year_number_two_digits(int(id_code[1:3]))
        month_number_validity = check_month_number(int(id_code[3:5]))
        day_number_validity = check_day_number(int(id_code[1:2]), int(id_code[3:5]), int(id_code[5:7]))
        born_order_validity = check_born_order(int(id_code[7:10]))
        control_number_validity = check_control_number(str(id_code))
        dict = create_dict(name, id_code)

        # if the ID code is valid return the result to the user as a dictionary
        if gender_number_validity and \
                year_number_two_digits_validity and \
                month_number_validity and \
                day_number_validity and \
                born_order_validity and \
                control_number_validity:

            return dict


def check_gender_number(gender_number):
    """Check if given value is correct for gender number in ID code."""

    return gender_number in range(1, 7)


def check_year_number_two_digits(year_number):
    """Check if given value is correct for year number in ID code."""

    return 0 <= year_number <= 99


def check_month_number(month_number):
    """Check if given value is correct for month number in ID code."""

    return 0 < month_number <= 12


def check_leap_year(year_number):
    """
    Check if given year is a leap year.
    More information on this can be found here -> https://en.wikipedia.org/wiki/Leap_year#Algorithm
    """

    return year_number % 4 == 0 and (year_number % 400 == 0 or year_number % 100 != 0)


def check_day_number(year_number, month_number, day_number):
    """Check if given value is correct for day number in ID code."""

    if month_number == 2 and check_leap_year(year_number) is True and day_number <= 29:
        return True
    elif month_number in [1, 3, 5, 7, 8, 10, 12] and 0 < day_number <= 31:
        return True
    elif month_number in [4, 6, 9, 11] and 0 < day_number <= 30:
        return True
    return False


def check_born_order(born_order):
    """
    Check if given value is correct for born order number in ID code.
    More information on this can be found here -> https://et.wikipedia.org/wiki/Isikukood#Järjekorranumber
    """

    return 0 <= born_order <= 999


def check_control_number(id_code):
    """
    Check if given value is correct for control number in ID code.
    More information on this can be found here -> https://et.wikipedia.org/wiki/Isikukood#Kontrollnumber
    """

    id_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0]
    id_list_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 0]
    # convert the ID code (string) into a list, for example "37605030299" -> [3, 7, 6, 0, 5, 0, 3, 0, 2, 9, 9]
    id_code = list(map(int, id_code))

    result = sum([id_list[i] * id_code[i]
                  for i in range(len(id_list))])  # list comprehension for summing the products of two lists
    if result % 11 == 10:
        result = sum([id_list_2[i] * id_code[i] for i in range(len(id_list_2))])
        if result % 11 == 10:
            return 0
        return True
    elif result % 11 == id_code[10]:
        return True
    return False


def create_dict(name, id_code):
    """
    Create a dictionary where the key is the person's name and the value is his/her ID code.
    For security reasons the last 4 digits are hidden.
    """

    dict = {}
    dict[name] = id_code[:7] + '****'

    return dict


def write_to_file(result):
    """
    Firstly, get the result from the function check_your_id.
    Secondly, check if the result is a dictionary or not. If dictionary is returned create a simple .csv-file
    based on the users input, else display an error message and no file is created.
    """

    result = check_your_id(id_code)

    if isinstance(result, dict):
        print(result)
        with open('data.csv', 'w') as f:
            f.write(f'{name},{id_code}')
        return 'Good news! -> Your ID code is valid. CSV-file written successfully!'
    return 'Invalid ID code or invalid input - no CSV-file written!'


print(write_to_file(dict))

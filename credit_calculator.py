"""
Modelling a simple credit calculator - stage 3/4.

Let's compute all the parameters of the credit.
There are at least two kinds of credit loans: those with annuity payment and those with differentiated payment.
At this stage, we're going to calculate only the annuity payment that is fixed during the whole credit term.

Author: Ave Nurme
Date: Sept 08th, 2020
"""


import math


class CreditCalculator:
    """Initialize."""

    def __init__(self):
        self.parameter = input("What do you want to calculate?\n"
                               "type 'n' for number of monthly payments,\n"
                               "type 'a' for annuity monthly payment amount,\n"
                               "type 'p' for credit principal: ").lower()

    def calculation(self):
        """
        Based on the parameter the user wishes to calculate call the correct function.
        Instead of if-elif-else I am using dictionary dispatch here. I find
        this a lot cleaner approach and easier to read, too.
        """

        menu = {
            'n': self.calculate_number_of_monthly_payments,
            'a': self.calculate_annuity_monthly_payment,
            'p': self.calculate_credit_principal,
        }

        function_to_call = menu[self.parameter]

        return function_to_call()

    def calculate_nominal_interest_rate(self):
        """
        Since we need to calculate the nominal interest rate in more than one
        method I found it useful to perform the calculation in a separate
        method so we can just call it whenever we need to.
        """
        self.interest_rate = float(input("Enter the credit interest: "))
        self.nominal_interest_rate = self.interest_rate / 1200

        return self.nominal_interest_rate

    def calculate_number_of_monthly_payments(self):
        """
        If the user opted for 'n' calculate the number of monthly payments.
        """
        principal = int(input("Enter the credit principal: "))
        monthly_payment = int(input("Enter the monthly payment: "))
        nominal_interest_rate = self.calculate_nominal_interest_rate()

        # count of periods
        base = 1 + nominal_interest_rate
        x = monthly_payment / (monthly_payment - nominal_interest_rate * principal)
        count_of_periods_n = math.ceil(math.log(x, base))

        # converting months into years & months
        self.convert = divmod(count_of_periods_n, 12)  # divmod(98, 12) -> (8, 2) -> 8 yrs & 2 months
        result = self.correct_output_when_converting()

        return result

    def calculate_annuity_monthly_payment(self):
        """
        If the user opted for 'a' calculate the annuity monthly payment.
        """
        principal = int(input("Enter the credit principal: "))
        number_of_periods = int(input("Enter the monthly payment: "))
        nominal_interest_rate = self.calculate_nominal_interest_rate()

        one_plus_i_raised_to_n = math.pow(1 + nominal_interest_rate, number_of_periods)

        annuity_monthly_payment = math.ceil(principal *
                                            ((nominal_interest_rate * one_plus_i_raised_to_n) / (
                                                    one_plus_i_raised_to_n - 1)))

        return f'Your monthly payment = {annuity_monthly_payment}!'

    def calculate_credit_principal(self):
        """
        if the user opted for 'p' calculate the credit principal.
        """
        annuity_payment = float(input("Enter the annuity payment: "))
        number_of_periods = int(input("Enter the number of periods: "))
        nominal_interest_rate = self.calculate_nominal_interest_rate()

        one_plus_i_raised_to_n = math.pow(1 + nominal_interest_rate, number_of_periods)

        credit_principal = math.floor(
            annuity_payment / ((nominal_interest_rate * one_plus_i_raised_to_n) / (one_plus_i_raised_to_n - 1)))

        return f'Your credit principal = {credit_principal}!'

    def correct_output_when_converting(self):
        """
        When calculating the number of monthly payments which are returned in
        years & months it is important to make sure we have the correct output.
        For instance, this will convert:
        0 years & 5 months -> 5 months
        5 years & 0 months -> 5 years
        This method also takes note of singular & plural forms of 'year' & 'month'.
        """
        if self.convert[0] == 0 and self.convert[1] == 1:
            return f'It will take {self.convert[1]} month to repay this credit!'
        elif self.convert[0] == 0 and self.convert[1] > 1:
            return f'It will take {self.convert[1]} months to repay this credit!'
        elif self.convert[1] == 0 and self.convert[0] == 1:
            return f'It will take {self.convert[0]} year to repay this credit!'
        elif self.convert[1] == 0 and self.convert[0] > 1:
            return f'It will take {self.convert[0]} years to repay this credit!'
        else:
            return f'It will take {self.convert[0]} years and {self.convert[1]} months to repay this credit!'


if __name__ == '__main__':
    INST1 = CreditCalculator()
    INST2 = INST1.calculation()
    print(INST2)

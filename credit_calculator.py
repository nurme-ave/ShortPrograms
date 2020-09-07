"""
Modelling a simple credit calculator: stage 2/4

Let's make some calculations for the installments.
The user might know the number of periods (months) and want to
calculate the monthly payment. Or, the user might know the
amount of monthly payment and wonder how many periods it
would take to repay the installments.

Author: Ave Nurme
Date: Sept 07th, 2020
"""

from math import ceil


class CalculatePayments:
    """Initialize."""

    def __init__(self):
        self.credit_principal = int(input("Enter the credit principal: "))
        self.payment_type = input("What do you want to calculate?\n"
                                  "type 'm' for number of monthly payments,\n"
                                  "type 'p' for the monthly payment: ").lower()

    def calculation(self):
        """
        Based on the payment type return the correct calculation.
        """
        if self.payment_type == "m":
            return self.calculate_number_of_monthly_payments()
        elif self.payment_type == "p":
            return self.calculate_monthly_payment()
        else:
            return "Wrong input"

    def calculate_number_of_monthly_payments(self):
        """
        If the user opted for 'm' calculate the number of monthly payments.
        """
        monthly_payment = int(input("Enter the monthly payment: "))
        result = ceil(self.credit_principal / monthly_payment)

        if result == 1:
            return f"It will take {result} month to repay the credit"
        return f"It will take {result} months to repay the credit"

    def calculate_monthly_payment(self):
        """
        If the user opted for 'p' calculate the monthly payment.
        """
        number_of_monthly_payments = int(input("Enter the number of months: "))
        result = ceil(self.credit_principal / number_of_monthly_payments)

        # Since we are rounding up the result using 'ceil'
        # we need to make sure the last payment is correct
        # and does not differ from the rest of the payments
        last_payment = self.credit_principal - \
            ((number_of_monthly_payments - 1) * result)
        exceeds = result * number_of_monthly_payments

        if exceeds > self.credit_principal:
            return f"Your monthly payment = {result} " \
                   f"and the last payment = {last_payment}."
        return f"Your monthly payment = {result}"


if __name__ == '__main__':
    INST1 = CalculatePayments()
    INST2 = INST1.calculation()
    print(INST2)
